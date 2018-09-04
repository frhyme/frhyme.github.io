---
title: python으로 블록체인 만들기 
category: python-lib
tags: python python-lib hashlib blockchain 
---

## introduction 

- [Go로 구현하는 블록체인](https://mingrammer.com/building-blockchain-in-go-part-1/)을 참고하여 정리했습니다. 만약 제 포스트가 유용하다면, 이는 제가 참고한 블로그 덕분임을 미리 밝힙니다. 

- 또한 해당 블로그는 블록체인에서의 몇 가지 개념을 다음과 같이 매우 명쾌하게 설명하고 있습니다. 

> 블록체인에서 **블록이란 가치있는 정보를 저장하는 데이터 구조**이다. 

- 물론 여기서 '가치있는'정보라는 말이 좀 이상할 수 있습니다. 블록은 약간 작업증명알고리즘에 따라서 일정 주기에 일정하게 생성되는 개념입니다. 따라서 한 블록에 동일한 가치를 발생시키는 데이터들이 들어있다거나, 트랜잭션 수가 같다거나 그렇지는 않아요. 그저, 일정 이상의 시간이 지나면 자동으로 정보를 담은 블록이 생성된다. 라고만 생각하셔도 될것 같아요. 
- 또한 여기서 말하는 '정보'는 어떤 데이터라도 상관없습니다. 단, 해당 데이터가 serialization이 되어야 합니다. 그래야 bytes형태로 변환할 수 있고 그래야 hash되는 것이 가능하니까요. 물론 대부분의 데이터는 json, xml등으로 시리얼라이제이션이 되니까, 상관없죠. python의 경우는 경우에 따라서 `pickle`을 활용해서 serialization해서 사용하면 매우 유용하지 않을까 싶습니다. 

> **블록체인은 본질적으로 특정한 구조를 지닌 데이터베이스일 뿐이며 순서가 지정된 링크드 리스트**이다. 즉, 블록은 삽입 순서대로 저장되며 각 블록은 이전 블록과 연결된다. 이러한 구조 덕분에 최신 블록을 빠르게 가져올 수 있고 해시로 블록을 (효율적으로) 검색할 수 있다.

- 제가 지금은 아주 간단한 블록체인 구조만 보고 있는데, graphDB처럼 네트워크의 형태로 값이 저장되어 있는 것이 아니고, linearly 연결된 linked list라고 생각하시면 됩니다. 이전 블록의 hash값을 참고해서 다음 블록에서 새로운 해쉬를 생성해냅니다. 즉, 바로 앞의 블록에 대해서만 연결되어 있다고 생각하시면 되요. 

- 또한 파이썬 코드의 경우는 [Let’s Build the Tiniest Blockchain](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)라는 포스트를 참고했음을 밝힙니다.

## class Block 

- 즉, block은 하나의 정보단위를 말합니다. 보통 DB에서 말하는 ACID를 갖춘 transaction이라고 생각해도 일단은 상관없습니다. 다만 DB에서 transaction은 거의 real-time에 적용되는 반면, 블록체인에서는 transaction이 발생할때마다 새로운 블록이 생긴다기보다는, 일정 이상의 transaction이 쌓인 다음 그 데이터들이 한번에 블록으로 만들어진다, 정도로 보시는 게 더 좋을 것 같습니다. 

- 아무튼, 어떤 주기로 block이 생성되는지에 대한 부분은 나중에 만들고, 일단은 단일 블록을 클래스로 설계합니다. 
    - 아래 코드에서 보시는 바와 같이, `index`, `timestamp`, `data`, `previous_hash`를 모두 합쳐서 string으로 만들고, 이 스트링을 bytes로 encoding하여 hash 값을 찾아줍니다. 
    - 이렇게 만들어진 hash 값이 해당 블록의 hash값이 됩니다. 
    - 또한 여기서 정의된 data가 해당 블록의 핵심, 즉 정보가 되는데, 여기는 무엇이든 들어갈 수 있습니다. serialization만 되면 되겠죠. 
- 만드는 블록들은 경우에 따라 달라질 수 있겠지만, 기본적으로는 생성번호, 생성인덱스, 데이터, 이전 해쉬값, 이 네 가지를 이용해서 해쉬값을 찾아주는 클래스를 구현하면 됩니다. 

```python
import datetime as dt
import hashlib ## hash function 이용

class Block(object):
    """
    index, 블록 생성 시간, 데이터, 이전 hash value 등을 이용해서 새로운 hash를 가지는 블록을 만들어줌 
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data ## can be anything, this is important
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    def hash_block(self):
        ## 아래 hash 함수를 보면 이전 block의 hash를 가져와서 다시 hash함수를 만듬 
        ## 즉, 새롭게 hash 값을 만들 때 이전 블록의 hash값을 참고해서 만들기 때문에 이를 활용해서 무결성이 확보될 수 있음
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(new_str_bin.encode())
        return sha.hexdigest()
```

- 그리고 다음과 같은 몇 가지 함수를 추가로 정의하는 것이 필요합니다. 
    - linked list에서도 맨 처음의 node를 선언해주는 것이 필요했죠. 마찬가지로 블록체인에서도 창세기 블록, genesis_block를 만들어주는 것이 필요합니다. 
    - 두번째로, 새롭게 block을 만들어주는 함수를 선언합니다. 해당 함수는 기존의 블록체인에서 마지막 노드에 자동으로 이어붙습니다. 자동으로 이어붙는다는 말은, 기존 블록체인의 마지막 노드의 hash값을 참고하여 본인의 hash값을 만든다는 이야기죠. 

```python
def create_genesis_block():## 창세기 블록 만들기. 
    return Block(0, dt.datetime.now(), data='genesis block', previous_hash="0")
def next_block(last_block):
    ## 지난번에 생성된 last_block에 이어붙일 새로운 블록을 만들어서 리턴한다.
    return Block(index = last_block.index+1, 
                 timestamp = dt.datetime.now(), 
                 data = f"Hey, I am block {last_block.index+1}",
                 previous_hash = last_block.hash)
```

## main code 

- 이걸 실행하면 대략 다음과 같죠. 원래는 일정주기(작업증명 알고리즘을 활용하여 주기 조절)에 따라서 새로운 블록을 생성해줘야 하는데, 여기서는 그냥 loop로 계속 생성해주게 만들었습니다. 


```python
## 블록체인이기는 한데, linear 한 linked structure라고 생각해도 됨. 
## 따라서 각 주소값을 리스트에 넣어서 관리해도 편함. 
blockchain = [create_genesis_block()]
previous_block = blockchain[-1]

num_of_block_to_add = 10
for i in range(0, num_of_block_to_add):
    ## 이전 블록에 이어서(이전 hash 값을 이용해서 새로운 hash값을 생성) 새로운 블록을 생성 
    block_to_add = next_block(previous_block) 
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
    print(f"Block {previous_block.index:2d} has been added to blockchain")
    print(f"hash value: {previous_block.hash}")
```

```
Block  1 has been added to blockchain
hash value: f3bc8a888795e90240e62378feaec8adf46a17c6cd7f29774fadda61ebcbbebe
Block  2 has been added to blockchain
hash value: e343cf03d9410c9e2b618a9a805d609bdb99f2cc653c2feecaa3778b92ffa9f9
Block  3 has been added to blockchain
hash value: 8681e49fd3a423c710ab53be558f0712fce5a9998b0d4434367e74445e910f83
Block  4 has been added to blockchain
hash value: 920f34f4f1233581cececac008ad9def293a0bc46774d409383b48dce1aa5eed
Block  5 has been added to blockchain
hash value: 7921a830f2aedcbd224af563fb9a061d0aabfe6d6d152b2aa509af60edce21b9
Block  6 has been added to blockchain
hash value: bbe82e9d4c0b1836df7f695bf1dd98b0ce3fc09dd256e5e4b1165303d6f30e76
Block  7 has been added to blockchain
hash value: 7ec2c16111ad53b6319e43693cca51a11f38ce1921d093d0dc67909b7e168f89
Block  8 has been added to blockchain
hash value: 79cb1e009af1c268ce7116c30d965d7df05058ce802883e8b98ddc3276e53876
Block  9 has been added to blockchain
hash value: 8a20852309195b697a71c25d98f03568a80fcd5e8e548f74b8e26a9a91e20707
Block 10 has been added to blockchain
hash value: 0b7085544ef330704b7aa4474625b63c63b435341d5a1588ebf532241299bb83
```

## wrap-up

- 일단은 여기서 끊어봅니다. 다음에는 [Let’s Make the Tiniest Blockchain Bigger: Part 2: With More Lines of Python](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d)을 참고해서 더 추가하려고 해요. 
- 앞서 말한 바와 같이, 현재는 블록체인이 제 로컬 시스템 내에 분산되어 있습니다. 실질적인, decentralized system이라고 하기 어려워요. 
- 또한, 앞서 말한 바와 같이 일정 주기에 따라 블록이 생성되도록 해야 하는데, 지금은 그냥 쭉 생성됩니다. 
- 따라서 다음에는 이 두 부분을 고려하여 수정하여 진행하도록 하겠습니다. 



## reference

- <http://lukious.com/2017/12/27/1%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EA%B5%AC%EC%A1%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/>

- <https://github.com/dvf/blockchain/blob/master/blockchain.py>
- <https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d>
- <https://medium.com/caulink/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-part-1-4386dbc735e>
- <https://mingrammer.com/building-blockchain-in-go-part-2/>


## raw code 

```python
import hashlib
import datetime as dt 

class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data ## can be anything, this is important
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    def hash_block(self):
        ## 아래 hash 함수를 보면 이전 block의 hash를 가져와서 다시 hash함수를 만듬 
        ## 즉, 새롭게 hash 값을 만들 때 이전 블록의 hash값을 참고해서 만들기 때문에 이를 활용해서 무결성이 확보될 수 있음
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(new_str_bin.encode())
        return sha.hexdigest()

def create_genesis_block():## 창세기 블록 만들기. 
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

num_of_block_to_add = 10
for i in range(0, num_of_block_to_add):
    ## 이전 블록에 이어서(이전 hash 값을 이용해서 새로운 hash값을 생성) 새로운 블록을 생성 
    block_to_add = next_block(previous_block) 
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
    print(f"Block {previous_block.index:2d} has been added to blockchain")
    print(f"hash value: {previous_block.hash}")
```