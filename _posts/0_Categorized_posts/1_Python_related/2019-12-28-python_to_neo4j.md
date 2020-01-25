---
title: python에서 neo4j 데이터베이스 접근하기.
category: python-libs
tags: python-basic python python-libs database neo4j graphdb networkx
---

## intro. 

- 본문에서는 python에서 GraphDB인 neo4j와 어떻게 연결하고, 쿼리를 전송하고 그 응답을 받는 기본적인 방식을 정리하였습니다.
python을 GraphDB인 neo4j와 연결하여 처리하는 방법을 정리합니다.
- 참고로 저는 neo4j의 유료모델을 사용하지 않고, 며칠동안만 쓸 수 있는 sandbox를 사용하고 있습니다. 

## Background

### install neo4j 

- 우선 `neo4j-driver`를 pip를 통해 설치합니다. 의존성이 있는 기타 다른 라이브러리들도 함께 설치가 되죠.

```bash
pip install neo4j-driver
```

### What is Bolt? 

- 물론 꼭 알아야 하는 것은 아니지만, neo4j에 접근하기 위해서는 Bolt라는 통신 프로토콜 방식을 사용해야 합니다. 직접 우리가 프로토콜에 맞춰서 데이터를 주고 받을 것은 아니지만, 대충 설명하자면.
- [Bolt](https://en.wikipedia.org/wiki/Bolt_(network_protocol)는 Connection-oriented 네트워크 프로토콜이라고 하며, database application에서 client-server 통신에 사용되는 프로토콜입니다. TCP connection이나 WebSocket위에서 동작하고요. 일단은 그냥 Neo4j에서 사용하기 위해 만들어진 독자적인 프로토콜이라고 생각해도 큰 문제는 없을 것 같아요. 

## do it. 

- 자 이제 해봅니다. 코드는 대략 다음과 같아요. 

```python
# pip install neo4j-driver

from neo4j.v1 import GraphDatabase, basic_auth

## DB에 접근하기 위해서 필요한 정보는 다음 네가지죠.
IP_ADDRESS ="#.##.###.###"
BOLT_PORT  = "#####"
USER_NAME = "#####"
PASSWORD = "#### "
##

# bolt protocol로 DB의 ip에 port로 접근하여, ID, PASSWORD를 입력합니다.
driver = GraphDatabase.driver(
    # bolt protocol로 내 DB의 IP에 BOLT_PORT로 접근하고 
    uri=f"bolt://{IP_ADDRESS}:{BOLT_PORT}", 
    # 주어진 USER_ID와 패스워드로 들어감.
    auth=basic_auth(
        user=USER_NAME, 
        password=PASSWORD)
    )

def run_query(input_query):
    """
    - input_query를 전달받아서 실행하고 그 결과를 출력하는 함수입니다.
    """
    # 세션을 열어줍니다.
    with driver.session() as session: 
        # 쿼리를 실행하고 그 결과를 results에 넣어줍니다.
        results = session.run(
            input_query,
            parameters={}
        )
        return results
####################################

# 쿼리를 작성합니다.
# 아래와 같은 Cypher 쿼리를 실행하면 그 결과로 테이블의 형태로 데이터가 리턴됩니다. 
# 그런데, 이 때, 아래 쿼리에서는 필요한 값만 가져온 것이 아니라, 모든 값을 그냥 그대로, 
# 그리고 AS와 같은 명령어로 칼럼의 이름을 확정하지도 않고 그대로 가져왔죠. 
# 이렇게 할 경우, 각 셀에 딕셔너리가 있는 형태가 되죠. 
print("=="*30)
cypher_query1 = '''
MATCH (p:Person)
RETURN p
'''
print("Cypher_query")
print(cypher_query1)
print("=="*30)
for i, each in enumerate(run_query(cypher_query1)):
    # each는 <class 'neo4j.Record'> 
    # 딕셔너리와 유사하다고 생각하면 됨.
    if i>=2:
        break
    print('--'*30)
    print(f"each              ==> {each}")
    print(f"each['p']         ==> {each['p']}")# 딕셔너리.
    print(f"each['p'].id      ==> {each['p'].id}")
    print(f"each['p'].labels  ==> {each['p'].labels}")
    # property는 다음의 형식으로
    print(f"each['p']['name'] ==> {each['p']['name']}")
print('=='*30)

# 만약, 이렇게 하지 않고, 일일이 원하는 칼럼에 대해서 이름을 명시해주면 더 깔끔하게 접근하는 것이 가능하죠.
cypher_query2 = '''
MATCH (p:Person)
RETURN p.name AS Name, p.born AS Born_year
'''
print("Cypher_query")
print(cypher_query2)
print("=="*30)
for i, each in enumerate(run_query(cypher_query2)):
    print("--"*30)
    if i>2:
        break
    print(f"each              ==> {each}")
    print(f"each['Name']      ==> {each['Name']}")
    print(f"each['Born_year'] ==> {each['Born_year']}")
print("=="*20)
```

```
============================================================
Cypher_query

MATCH (p:Person)
RETURN p

============================================================
------------------------------------------------------------
each              ==> <Record p=<Node id=1 labels={'Person'} properties={'name': 'Keanu Reeves', 'born': 1964}>>
each['p']         ==> <Node id=1 labels={'Person'} properties={'name': 'Keanu Reeves', 'born': 1964}>
each['p'].id      ==> 1
each['p'].labels  ==> frozenset({'Person'})
each['p']['name'] ==> Keanu Reeves
------------------------------------------------------------
each              ==> <Record p=<Node id=2 labels={'Person'} properties={'name': 'Carrie-Anne Moss', 'born': 1967}>>
each['p']         ==> <Node id=2 labels={'Person'} properties={'name': 'Carrie-Anne Moss', 'born': 1967}>
each['p'].id      ==> 2
each['p'].labels  ==> frozenset({'Person'})
each['p']['name'] ==> Carrie-Anne Moss
============================================================
Cypher_query

MATCH (p:Person)
RETURN p.name AS Name, p.born AS Born_year

============================================================
------------------------------------------------------------
each              ==> <Record Name='Keanu Reeves' Born_year=1964>
each['Name']      ==> Keanu Reeves
each['Born_year'] ==> 1964
------------------------------------------------------------
each              ==> <Record Name='Carrie-Anne Moss' Born_year=1967>
each['Name']      ==> Carrie-Anne Moss
each['Born_year'] ==> 1967
------------------------------------------------------------
each              ==> <Record Name='Laurence Fishburne' Born_year=1961>
each['Name']      ==> Laurence Fishburne
each['Born_year'] ==> 1961
------------------------------------------------------------
========================================
```

## wrap-up

- 우선 왜 Bolt라는 새로운 통신 프로토콜을 만드는 것이 필요했는가? 라는 의문은 듭니다. 제 입장에서는 이게 반드시 필요한 것인지, 모르겠거든요. 우선은, '이게 반드시 필요한 일이었는가?'를 알면 좋은데, 통신 쪽에 대해서는 저의 백그라운드가 약해서 다음에 시간이 있을 때 좀 더 정리해보도록 하겠습니다. 
- 데이터가 관리되는 방식은 '그래프'라고 할지라도, 쿼리문을 통해서 나오는 그 결과는 '테이블'의 형태로 나오게 됩니다. 내가 필요로 하는 정확한 값이 무엇인지를 쿼리 문에서 정확하게 명시하고, 그 값만을 가져와서 처리하는 것이 필요하죠.
- 흐음. 그런데요. 파이썬의 경우 `networkx`라는 좋은 라이브러리가 있습니다. 이 라이브러리를 사용해서 네트워크 분석을 하는 일이 많은데, 만약 neo4j를 사용하는 상태에서 필요한 데이터를 가져와서, networkx를 사용해서 변환하려면 네트워크 ==> 테이블 ==> 네트워크 의 번잡스러운 변환 과정을 거치게 되죠. 즉, "그래프 투 그래프"로 훨씬 효율적으로 가져올 수는 없는걸까요?