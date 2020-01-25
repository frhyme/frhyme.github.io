---
title: python으로 블록체인 만들기 - 2편
category: python-lib
tags: python python-lib hashlib blockchain datetime hash sha256
---

## intro 

- 지난번에 아주 간단한 블록체인을 만들었습니다. 물론 1) 블록의 생성주기도 컨트롤되지 않고 2) http등을 통해서 다른 서버들에게 블록이 나누어져 저장되고 있지도 않으면서, 과연 이것을 블록체인이라고 부를 수 있나? 싶지만 뭐 그래도 정보를 담는 "블록" 이 있고, 해시값을 이용해서 체인이 구성되니까, 아주 간단한 레벨의 블록체인이라고 부를 수 있을 것도 같아요. 

- 아무튼 [lets make the tiniest blockchain bigger](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d)을 참고하여 진행하기 전에 이전에 만들었던 코드를 다시 한 번 복기해보겠습니다. 
    - 추가로, 1편과 달리 2편에서는 난이도가 급증합니다. 

## simple blockchain 

```python
import hashlib ## hash 값을 찾기 위해 사용하는 라이브러리 
import datetime as dt ##보통 block이 생성되었을 때 해당 값을 같이 저장하고, 그 값을 참조하여 hash를 생성 

class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data ## can be anything, this is important
        self.previous_hash = previous_hash
        self.hash = self.hash_block()## 값을 넣고, init하면 자동으로 해쉬값이 만들어짐. 
    def hash_block(self):
        ## 아래 hash 함수를 보면 이전 block의 hash를 가져와서 다시 hash함수를 만듬 
        ## 즉, 새롭게 hash 값을 만들 때 이전 블록의 hash값을 참고해서 만들기 때문에 이를 활용해서 무결성이 확보될 수 있음
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        ## hash할 때 string이 아니라 bytes로 넘기는 것을 명시 
        sha.update(new_str_bin.encode())
        return sha.hexdigest()

def create_genesis_block():
    ## 창세기 블록 만들기. 
    return Block(0, dt.datetime.now(), data='genesis block', previous_hash="0")

def next_block(last_block):
    ## 지난번에 생성된 last_block에 이어붙일 새로운 블록을 만들어서 리턴한다.
    return Block(index = last_block.index+1, 
                 timestamp = dt.datetime.now(), 
                 data = f"Hey, I am block {last_block.index+1}",
                 previous_hash = last_block.hash)

## 블록체인이기는 한데, linear 한 linked structure라고 생각해도 됨. 
## 따라서 각 주소값을 리스트에 넣어서 관리해도 편함. 
blockchain = [create_genesis_block()]
previous_block = blockchain[-1]

## 즉 아래에서는 그냥 반복문에 따라서 연속으로 블록을 10개 죽 생성함. 
num_of_block_to_add = 10
for i in range(0, num_of_block_to_add):
    ## 이전 블록에 이어서(이전 hash 값을 이용해서 새로운 hash값을 생성) 새로운 블록을 생성 
    block_to_add = next_block(previous_block) 
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
    print(f"Block {previous_block.index:2d} has been added to blockchain")
    print(f"hash value: {previous_block.hash}")
```

## make it bigger

- 이제 확장해봅시다. 우선, 기존의 우리가 설계한 블록체인에서는 데이터로 입력되는 것이 그냥 스트링이었습니다. 

```python
def next_block(last_block):
    ## 지난번에 생성된 last_block에 이어붙일 새로운 블록을 만들어서 리턴한다.
    return Block(index = last_block.index+1, 
                 timestamp = dt.datetime.now(), 
                 data = f"Hey, I am block {last_block.index+1}",## 그냥 스트링을 기본 데이터로 가짐 
                 previous_hash = last_block.hash)

```

- 하지만 이제는 이 데이터를 `list of transaction`으로 고려합니다. 

### transaction?? 

- 블록체인을 보고 계시는 분들은 아마도 다들 DB를 기본적으로는 알고 계실텐데 굳이 transaction에 대한 설명을 추가해야하는지는 약간 헷갈리기는 합니다. 
- 아무튼, [`transaction`](https://en.wikipedia.org/wiki/Database_transaction)은 DB에서 발생하는 일관적이고, 고립되고, 영속적인 일의 단위 라고 생각하시면 됩니다. 자세한 내용은 [링크](https://en.wikipedia.org/wiki/Database_transaction)를 보시면 좋구요.
- 보통 transaction에 대한 예시를 들때 금융거래를 많이 예로 듭니다. 뭐, 만약 A가 B라는 사람에게 돈을 500억원 보낸다고 해봅시다. 이를 위해서는 A의 계좌에서 돈을 빼야 하고, B의 계좌에 돈을 넣어야 하는 일련의 연속적인 업무(정확히는 **query**)가 포함되어 있죠. 
- 이 쿼리들은 적용될 경우 모두 적용되어야 합니다(만약 A의 계좌에서 돈을 빼기만 하고, B의 계좌에 돈을 넣지 않으면 안되죠). 약간 이런 식으로 Atomic, Consistent, Isolated, Durability(ACID)를 따르는 일련의 업무단위를 transaction이라고 칭합니다. 

- 아무튼 간에 앞서 말한대로 저희의 블록체인 네트워크에서 하나의 블록에 담기는 데이터는 transaction list입니다. 하나의 transaction은 다음과 같이 정의됩니다. 누구에게서 누구에게 어느정도의 돈이 움직였느냐, 라는 기록해둔 것이죠. 이런 것이 하나의 transaction이 됩니다. 

```json
{
  "from": "71238uqirbfh894-random-public-key-a-alkjdflakjfewn204ij",
  "to": "93j4ivnqiopvh43-random-public-key-b-qjrgvnoeirbnferinfo",
  "amount": 3
}
```

- 흠...보다보니 오히려 [이 포스트]가 좀 괜찮은 것처럼 보이기도 합니다. (https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)가 더 상세하게 설명되어 있는 것 같기도 합니다. 

## wrap-up

- 갑작스럽게 멈추었습니다. 
- 앞서 작성한 바와 같이 [이 포스트](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)가 훨씬 잘 작성되어 있습니다. 제가 본 글에서 참고한 글에서는 블록체인이 분산화되어 있을때 어떻게 작동하는지에 대한 부분이 약간 부족하게 설명되어 있는 반면, 여기서는 그 부분을 좀 명쾌하게 설명하고 있는 것 같아요. 
- 반복한다고 생각하고, 새로 해당 포스트 내용을 기본으로 다시 작성해보도록 하겠습니다. 

## reference 

