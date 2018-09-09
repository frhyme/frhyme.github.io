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
    