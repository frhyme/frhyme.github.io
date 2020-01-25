---
title: (very basic)blockchain 다시 공부하고 완성하기.
category: others
tags: python python-lib blockchain bit-coin database consensus hash urllib hashlib json datetime requests uuid flask bit-coin 
---

## 우선

- 본 포스트는 전적으로 [Learn Blockchains by Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)을 참고하여 진행됩니다. 이 포스트에 아주 작은 도움이라도 받았다면 그 모든 고마움은 제가 참고한 포스트에서 모든 것을 가지고 있음을 다시 말합니다. 
    - 또한 해당 포스트의 코드는 모두 [여기에 있습니다](https://github.com/dvf/blockchain/blob/master/blockchain.py). 
    - 미묘하게 포스트의 내용과는 조금 다릅니다. 마지막에 consensus 알고리즘에서는 잘 안되는 경우도 있었던 것 같아요. 

- 또한 저는 블록체인알못입니다 하하핫. 이렇게 남이 쓴 포스트를 보면서 코딩하면서 다시 써야 제대로 이해하는 상상력이 부족한 두뇌를 가졌기 때문에 다른 사람들이 만들어놓은 정보를 딛고 올라가려 합니다. 
- 개념을 하나씩 정리해보겠습니다. 

## 개념들

### 블록체인 

- **블록체인은 본질적으로 특정한 구조를 지닌 데이터베이스일 뿐이며 순서가 지정된 링크드 리스트**입니다. 
- 블록이 연결된 리스트이구요. 보통 이 블록은 선형적으로, 마지막에 생성된 블록이 제일 끝에 위치하는 식으로 연결됩니다. 
- 많은 곳에서 복잡하게 설명하는 것 같습니다. 개념을 다시 하나씩 정리하자면, 

### blockchain is Database  

- 블록체인은 데이터를 저장한 데이터베이스입니다. 
- 어떤 데이터도, serialization하고 binary로 변형하여 hash값을 생성해낼 수 있다면, 모두 블록체인으로 표현할 수 있습니다. 

### block and hash

- **블록이란 가치있는 정보를 저장하는 데이터 구조**입니다. 또한 하나의 데이터베이스를 일정 시간에 따라서 겹치지 않게 여러 data-set으로 분리합니다. 그때 각각의 data-set이 블록을 의미합니다. 
- 하나의 블록에는 다음과 같은 정보들이 보통 담깁니다. 
    - `index`: 해당 블록의 번호, 라고 생각하면 됩니다. 
    - `timestamp`: 언제 만들어졌는가? 
    - `proof`: 이는 나중에 제가 다시 설명하도록 하겠슨비다. 
    - `previous_hash`: 이전 block(블록체인에서 가장 최근에 만들어진 block)의 hash 값 
    - `data`: 가장 중요한, '가치있는 정보'에 포함되는 부분이죠. 특히 data에는 아무 정보가 마구 넣을 수는 없습니다. 보통 비트코인에서는 transaction들의 묶음(list)를 data로써 넣는데요, transaction list를 json 등의 형태(string)로 변경되고, 다시 이를 bytes로 변환하여 인코딩이 되어야 합니다. 그래야 hash가 되니까요. 

- 또한, 여기서 `previous_hash` 값을 참조하는 것이 중요합니다. 이 값이 바로 blockchain의 immutability(불변성)을 보장해줍니다. 새로운 블록이 자신을 hash할 때 이전 `previous_hash`를 사용하기 때문에, 이 값이 임의로 바뀔 경우에는 이를 빠르게 파악할 수 있습니다. 

### mining

- 블록체인에서는 mining을 해야 코인을 받습니다. 
- 여기서 `mining`이라는 것은, 블록체인에서 새로운 블록을 생성해낼 때, 이 블록이 기여했다는 것을 말합니다.
- blockchain의 무결성을 지켜주는 것으로 `hash`와 `proof`라는 두 가지 값이 있습니다. 
- 우선 `hash`의 경우는 새로 생성되는 블록에게 부여되는 값으로, 이전 블록의 hash값과 현재 데이터의 timestamp와 다른 정보를 모두 serialization하고 이의 hash값을 찾아줍니다. 현재 블록의 데이터와, 이전 블록의 hash값을 모두 가지고 있습니다. 따라서 중간에 새로운 블록을 집어넣을경우 block의 hash값이 달라지고, 이는 전체 블록체인의 무결성을 보장해주는 장치로서 작동하게 됩니다. 
- proof를 말하기 전에 우선 PoW(Proof of Work)를 먼저 정리해야 합니다. 블록체인은 앞서 말한바와 같이 데이터베이스이기도 하지만, 일종의 화페이기도 합니다. 하나의 블록에 대해서 일반적으로 하나의 코인이 주어지게 되는데, 많은 사람들이 참여하고(컴퓨팅 파워가 커지고), 따라서 블록의 생성이 매우 빨라지고, 코인이 폭증하고(하나의 코인의 단위가치가 매우 떨어지고) 하는 등의 상황을 아무도 원하지 않습니다. 
- 따라서, 시간이 지나면서 생성되는 블록의 양을 컨트롤할 수 있도록 제한해야 합니다. 이를 위해 PoW가 필요합니다. 
- PoW는 간단히 '내가 일을 했다'라는 것을 증명하는 것인데, 이 것이 증명되면, 블록이 생성됩니다. 즉, 시간이 지나면서 점점 PoW의 난이도를 어렵게 만들어야(많은 컴퓨팅 파워가 필요하도록) 블록생성이 점점 어려워지죠. 
- 블록체인에서 보통 이 PoW는 다음과 같은 형태로 만들어집니다. 
    - 현재 hash값+proof 를 했을 때 어떤 조건(만들어지는 스트링의 맨 앞에 0 4개)를 만족하는 proof를 찾아라. 
    - 난이도를 조절하려면 0의 개수를 늘리면 됩니다. 
    - proof값을 알고 있다면, 해당 조건을 만족하는지 여부는 쉽게 알 수 있지만, 모를 경우에 이 값을 구하는 것은 꽤 큰 컴퓨팅 파워를 요구합니다. 
    - 이 proof를 구하도록 하는 것은 해당 블록체인에서 화폐가 마구 생겨나지 않도록 막음과 동시에 해당 블록이 유효한지 도 검증하기 위해 사용될 수 있습니다. proof값도 해쉬되어서 사용되기 때문에, 블록체인의 특정 블록을 임의로 고쳐서 집어넣는 것은 매우 어렵습니다. 
- 서론이 길었습니다만, 여기서 해당 블록에 적합한 proof를 찾는 것을 mining이라고 합니다. 즉, 해당 블록체인이 무결성있게, 잘 유지될 수있도록 해당 컴퓨터가 서포트하고 있다, 라는 의미를 가지게 됩니다. 
- 따라서 블록이 만들어지면, 해당 블록에 "이 miner에게 코인을 준다"라는 transaction 정보를 넣어서 만들게 됩니다. 

### decentralization 

- 블록체인은 Data center처럼 하나의 공간에서 모든 데이터를 저장하고 관리하는 것이 아니라, 여러 컴퓨터(노드)들에서 동시에 데이터베이스가 존재한다고 할 수 있습니다. 이것이 흔히 말하는 블록체인의 탈중앙화, 분산화된 시스템인 것이죠. 
- git에서의 clone과 비슷하다고 볼 수 있습니다. git에서 처음에는 서로 다른 컴퓨터에 repository를 clone해서 가져올 수 있습니다. 이 시점에서 모든 repository는 서로 동일하다고 볼 수 있습니다. 
- 그런데, 시간이 지나면 각 컴퓨터(node)에 존재하는 개별 리퍼지토리들은 서로 다른 형태로 존재하게 됩니다. 어떤 것은 처음과 거의 같을 수도 있고, 다른 것은 계속 코드를 생성(블록을 생성)해 내서 처음과는 서로 다른 리퍼지토리로 존재할 수도 있는 것이죠. 

### consensus 

- 보통은 이럴 때, 오픈소스 프로젝트에서는 해당 프로젝트의 maintainer가 일정한 규율에 맞춰서 pull request를 허용하는 식으로 버전을 관리하게 됩니다. 
- 그런데 블록체인에서는 다릅니다. 서로 다른 버전의 블록체인이 여러 node에서 마구 존재할 때, 이를 합의할 수 있는 알고리즘이 존재하고, 거기에 맞춰서 전체 블록체인을 수정해줍니다. 
- 예를 들면, **"가장 긴 블록체인을 표준 블록체인으로 정한다"**는 식으로(이건 마구잡이식이지만) 알파 블록체인을 정한다고 볼 수 있어요. 

## operation in blockchain

- flask를 이용해서 각각의 서버의 동작을 다음 5가지에 대해서 정의합니다. 

```python
## 해당 node에서 새로운 block을 생성합니다
## 물론 생성하기 위해 PoW도 수행해야 합니다. 
## mine에 성공하면(블록을 생성하면), 보상을 받습니다. 
@app.route('/mine', methods=['GET'])
def mine():
    pass
  
## 해당 node에 새로운 transaction data를 만들어줍니다. 
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    pass

## 해당 node에 저장되어 있는 blockchain을 리턴해줍니다.
@app.route('/chain', methods=['GET'])
def full_chain():
    pass

## 해당 node에 새로운 node가 있다는 것을 알려줍니다. 
## 여기에 node가 등록되어 있지 않으면, consensus알고리즘을 구현할 때 해당 node를 제외하고 구현하게 됩니다. 
## 이는 각각의 node에 대해서 다 수행해줘야 합니다. 
## 예를 들어, 어떤 node A에 node B를 등록했다면, node B에도 node A를 등록해줘야 합니다. 
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    pass

## 개별 블록체인 서버(이를 Node A라 하자)에서 아래 url에 접근하면, 
## Node A에 등록되어 있는 nodes들을 모두 읽고, 
## 제일 긴 블록체인의 노드를 찾아서 현재 블록체인을 변경해줍니다. 
## consensus 방식은 상황에 따라서 다를 수 있습니다. 여기서는 간단하게, 가장 긴 블록이 알파다, 라는 식으로 진행합니다. 
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    pass
```


## attribute and method in class

- 

```python
class Blockchain(object):
    def __init__(self):
        self.chain = []## 블록 리스트 
        self.current_transactions = []## 블록이 생성되면 들어갈 트랜잭션(데이터)
        self.nodes = set()## 현재 이 블록체인 노드가 인지하고 있는 다른 블록체인 노드들
        self.create_genesis_block()## 블록체인이 생성되면, 우선, 여기서 새로운 창세기 블록을 만들어줌 

    def register_node(self, address):
        ## 현재 노드에 새로운 노드를 등록해줌 
        pass

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        pass

    def create_genesis_block(self):
        ## create a genesis block.
        pass
        
    def new_block(self, proof, previous_hash=None):
        ## 새로운 블록을 만들고, 현재 transaction 리스트는 초기화 
        pass
    
    @staticmethod
    def hash(block):
        ## 블록을 json으로 serialization하고 hash
        pass
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        # @property를 붙여서, method지만, attribute처럼 접근
        pass
    
    def proof_of_work(self, last_proof):
        ## last_poof에 대해서 valid_proof를 만족하는 proof를 찾아서 리턴함. 
        pass
    
    @staticmethod
    def valid_proof(last_proof, proof):
        ## last_proof, proof를 섞었을 때, 우리가 원하는 조건(맨 앞 4개가 0)을 만족하는지 판단
        pass
    
    def valid_chain(self, chain):
        ## 현재 블록체인을 제일 앞부터 순차적으로 읽으면서, 유효한지 검증하고 T/F를 리턴
        ## 현재 hash가 이전 hash를 고려해서 만들어졌는지
        ## proof는 모두 유효한지 등 
        pass

    def resolve_conflicts(self):
        ## 블록체인은 여러 node에서 동시에 돌아감. 
        ## 어떤 시점에서 각각의 node들에 존재하는 블록체인들은 서로 다르게 되는데, 
        ## 서로 다른지를 파악하고, 전체 노드 네트워크에서 현재 내가 가지고 있는 node의 코드(혹은 데이터)가 
        ## 알파 코드가 아닐 경우에 현재 블록체인의 데이터를 알파 블록체인으로 변경해줌 
        pass
```

## raw code 

- 전체 코드는 하나의 파일에 대해서 만들었습니다. 
- 가능한 자세하게 주석을 달려고 노력했습니다. 여러분을 위해서도 있는데, 그보다는 내일의 저를 위해서...
- 이를 서버로 돌리려면, `python aaa.py`로 터미널에서 돌리면 됩니다. 

```python
import hashlib ## hash하기 위해 사용하는 라이브러리 
import json
import datetime as dt 
import requests 

## 단순히 url을 특정 정보에 따라서 나누어주는 함수
from urllib.parse import urlparse

## 분산환경에서 여러 노드가 있을때 개별 node에 대해 식별키를 만들어주기 위해서 사용합니다. 
## 여기서 uuid는 충돌하지 않도록 임의로 만들어주는 값이며, 
## 실제로 블록체인에서 이렇게 임의로 만들어줄 경우에는 문제가 생길 수 있을 것 같습니다. 
## 만약 서버를 껐다가, 다시 켰을대, 이 uuid가 바뀌게 되면, 그동안 mining한 돈들이 모두 날아가게 되는것이니까요. 
from uuid import uuid4

## flask는 마이크로아키텍쳐 프레임웍이며, 
## mine, chain 등 블록체인서버에서 필요로 하는 각각의 operation을 구현하기 위해 사용됩니다. 
from flask import Flask, jsonify, request

## 블록체인 클래스를 정의합니다. 
class Blockchain(object):
    def __init__(self):
        ## 블록 리스트
        self.chain = []
        ## 새로운 블록이 생성되면, 해당 블록에 포함될 transaction들입니다. 
        ## 앞서 말한 바와 같이, 새로운 블록은 hash될 수 있어야 하고, 따라서 모두 serialization되어야 합니다. 
        ## 즉, 여기에는 모두 json으로 변환될 수 있는 데이터구조만 들어오게 되죠. 
        self.current_transactions = []
        ## blockchain은 탈중앙화 시스템이죠. 즉, 현재 관련된 node들(블록체인에 포함된 컴퓨터들)의 관리체계가 필요합니다. 
        ## 간단하게 set로 만들고, 다른 컴퓨터가 생성되면 여기에 업데이트를 합니다. 
        self.nodes = set() 
        ## 맨처음에는 아무 블록이 없기 때문에 genesis_block를 만들어야 함 
        self.create_genesis_block()

    def register_node(self, address):
        ## node는 현재 해당 블록체인을 구동중인 서버를 말합니다. 
        ## 실제 블록체인에서는 자동으로 node address를 등록하도록 하고 있을 수 있지만
        ## 여기서는 수동으로 등록하도록 구현했습니다. 
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        ## netloc는 보통 192.168.0.5 같은 값을 말합니다. 
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')
    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        # 일단, transaction은 항상 sender, recipient, amount로 표현된다는 것이 정의되어 있습니다. 
        # 각각 str, str, int로 표현되죠. 
        # 여기서 sender, recipient는 모두 node의 uuid와 같아야 합니다. 
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        ## 얘는 뭔가, 왜 last_block의 index에 1을 더하여 리턴하는가?? 
        ## 왜 거래가 추가될 block의 index를 리턴하는가?? 
        return self.last_block['index'] + 1

    def create_genesis_block(self):
        ## create a genesis block.
        self.new_block(previous_hash=1, proof=100)
        
    def new_block(self, proof, previous_hash=None):
        ## 새로운 블록을 만들어줍니다. 
        ## 만약, 새로운 객체를 만들고, 제가 객체들도 포함된 형태로 블록이 생성될 경우 
        ## pickle등 다른 방법으로 serialization하는 것이 좋을 수 있습니다. 
        block = {
            'index': len(self.chain) + 1,## timestamp의 경우 string으로 넣을 수도 있으나, UNIX time으로 넣어야 이후 후처리가 쉬움. 
            'timestamp': dt.datetime.timestamp(dt.datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            ## 블록체인의 무결성을 유지하기 위해서 이전 블록의 hash값을 함께 넣어줍니다. 
            'previous_hash': self.hash(self.chain[-1]) if previous_hash is None else previous_hash, 
        }
        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    @staticmethod## staticmethod는 그저 클래스 내부에 존재할 뿐이지 외부에 있는 함수처럼 작동합니다(class or class instance의 어떤 정보도 참조하지 않습니다. )
    def hash(block):
        # Hashes a Block
        # 이 블록체인에서는 각각의 block이 json으로 변형되기 쉽도록, dictionary, int, string으로만 구성되어 있습니다. 
        # sort_keys=True를 넘겨주지 않아도 기본적으로 json에서 ordering이 유지됨. 
        block_json = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_json).hexdigest()
    
    @property## @property 데코레이터는 해당 함수를 마치 attribute처럼 접근할 수 있게 해줍니다(또한 read-only)
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
        """
        간단한 Proof of work algorithm: 
        - last_proof와 어떤 값(proof)를 합쳐서 넣었을 때, 우리가 원하는 조건을 충족했는지(valid_proof)를 파악하고,
        - 충족할때의 proof를 찾아서 리턴함. 
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        hash(last_proof, proof)의 제일 앞 네 byte가 0인지를 파악한다. 
        - last_proof는 previous block의 proof고, 
        - 이를 섞은 다음 proof of work를 찾는 놈에게 다음 block를 만들 수 있는 자격이 주어짐. 
        """
        guess = f'{last_proof}{proof}'.encode() ## string ==> binary 
        guess_hash = hashlib.sha256(guess).hexdigest()
        ## 제일 앞 네 개가 0인지 파악함, 물론 보통 시간이 지나면서 이 0의 개수를 늘리는 식으로 진행함. 
        return guess_hash[:4] == "0000"
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        blockchain의 validity를 검증한다는 것은, 블록을 순차적으로 읽어가면서, 
        - 이전 블록의 hash를 고려해서 현재 hash값이 생성되었는지
        - 이전 블록의 proof와 현재 블록의 proof를 계산해보니 validity가 맞는지 등을 확인하는 것을 의미한다. 
        - 만약 이 과정에서 문제가 생긴다면, 검증이 깨지게 됨. 
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1
        ## for 문으로 변경하는 것이 더 깔끔할 것 같은데. 일단 나중에 변경하겠음. 
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        앞서 말한 바와 같이 블록체인은 분산화된 시스템이다.
        맨 처음에는 하나의 컴퓨터에서만 구현되지만, 점점 여러 node에서 chain들이 만들어진다. 
        '조절'하지 않으면, 점점 모든 노드들에서 개별 블록체인들이 마구 생겨날 수 있는데, 
        이때 전체 블록체인을 일관성있게 조절해주기 위해서는 주기적으로 모든 node에 있는 블록체인을 확인하고, 
        어떤 블록체인을 표준 혹은 일관적인 블록체인(알파 블록체인)으로 선정해줄 것인지를 정해야 한다. 
        다양한 방법이 있을 수 있으나, 여기서는 모든 노드 중에서 '가장 긴' 블록체인을 알파 블록체인으로 정한다. 
        이 함수의 경우는 전체 노드에 개별적으로 존재하는 블록체인을 읽어와서, conflict가 발생하는지를 파악하고 
        발생했을 경우 alpha blockchain을 찾아주는 메소드다. 
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes ## 현재 blockchain에 기여하고 있는 컴퓨터들
        new_chain = None 

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            ## status code 200 means 'ok'
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
    
#######################
# flask로 서버를 운영합니다. 
app = Flask(__name__)

# node에 대한 식별자를 무작위로 만들어줍니다. 이때 uuid4를 사용함. 
# mine()에서 이 변수를 사용함. 
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # mine에 성공하면, 해당 block을 유지하는데 기여했으므로 리워드를 줌
    
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    ## where is identifier?
    blockchain.new_transaction(
        sender="0",
        ## node_identifier는 블록체인 서버를 구현했을때 해당 서버(node)에 주어지는 값을 말함. 
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200
  
## 새로운 transaction data를 만들어줍니다. 
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    # transcation에는 위 세 가지 정보 sender, recipient, amount가 모두 있어야 함. 
    # 하나라도 없을 경우 에러 발생.
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

## 현재 전체 blockchain을 리턴해줍니다.
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

## 새로운 node를 등록합니다. 
## 여기에 node가 등록되어 있지 않으면, consensus알고리즘을 구현할 때 해당 node를 제외하고 구현하게 됩니다. 
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


## 개별 블록체인 서버(이를 Node A라 하자)에서 아래 url에 접근하면, 
## Node A에 등록되어 있는 nodes들을 모두 읽고, 
## 제일 긴 블록체인의 노드를 찾아서 현재 블록체인을 변경해줍니다. 
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200

if __name__ == '__main__':
    ## 저의 경우는 여러 node를 동시에 돌리기 위해서, 
    ## 3개의 python file을 만들고, port값을 변경하여 터미널에서 따로 돌렸습니다. 
    app.run(host='0.0.0.0', port=5000)
    
```

## reference

- <https://hackernoon.com/learn-blockchains-by-building-one-117428612f46>