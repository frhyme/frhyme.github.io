---
title: neo4j의 Graph를 networkx로 가져오기.
category: python-libs
tags: database nosql sql graphdb cypher networkx python-libs 
---

## 물론, 굳이 networkx로 가져올 필요가 있는가? 

- 물론, 기본적으로 DB에 잘 정리되어 있는 데이터를, 그리고 심지어 보통 이곳에 있는 데이터들은 로컬로 가져오기에는 지나치게 큰 크기의 데이터인 경우가 대부분인데, 이 데이터를 로컬로 가져와서 그것도 `networkx`로 분석을 하는 것이 큰 의미가 있을까 싶기는 합니다. 
- 다만, 그러함에도 이유를 찾아보자면, 
    1) 저는 DB에서 데이터를 직접 분석 비슷하게 하는 것이 불안하게 느껴지거든요. 혹시나 DB에 문제를 발생시키지는 않을까, 싶고, DB위에서 돌리는 것이 어떤 의미로든 과부하의 원인이 될 수 있으니까 가능하면 분리시켜서 다양한 분석 및 실험을 해보는 것이 훨씬 효율적으로 느껴지고. 
    2) Neo4j에서 그래프에 대한 웬만한 알고리즘을 제공하기는 하지만, 여전히 python 위에서 돌아가는 다른 머신러닝 라이브러리들과 비교하면 그 양이 현저하게 적죠. 가령, 머신러닝 패키지들과 함께 이용하려면 아무래도 일단 python으로 가져와서 쓰는 것이 훨씬 편하기마저 합니다. 즉, 이를 위해서라도 networkx로 가져오는 것이 필요할 수 있죠. 
- 아무튼, 그래서 가져와서 써보기로 했씁니다. 일단 가져온다면 그 다음부터는 큰 어려움이 없어지죠.

## networkx로 가져옵시다.

- 기본 얼개는 cypher로 쿼리하여 neo4j에서 데이터를 가져옵니다. 쿼리문은 다음의 형식이 되겠죠. 

```
input_query = """
MATCH (n1)-[e]->(n2)
RETURN n1, e, n2
LIMIT 100
"""
```

- 그리고 DB의 세션을 열어서 다음처럼 쿼리를 날리고 결과를 가져옵니다. 

```python
# pip install neo4j-driver

import networkx as nx

from neo4j.v1 import GraphDatabase, basic_auth

## 
IP_ADDRESS =""
BOLT_PORT  = ""
USER_NAME = ""
PASSWORD = ""
##

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

# 다음과 같이 쿼리하여, 노드, 엣지, 노드를 모두 가져온다.
# 그래도 전체를 다 가져오는 경우 부하가 많이 걸리므로, 100로 제한하여 가져와 본다.
input_query = """
MATCH (n1)-[e]->(n2)
RETURN n1, e, n2
LIMIT 100
"""

results = run_query(input_query)
```

- 자, 이제 쿼리의 결과가 `results`에 저장되어 있죠. 간단히 말하면, `n1`, `e`, `n2`의 칼럼에 각 값들이 저장되어 있다고 보시면 됩니다.
- 이제 긁어온 쿼리에서 필요한 정보만 뽑아내어 다음처럼 그래프에 넣어줍니다. 약간의 특이사항은 `id`, `label`은 내부 변수로 접근해야 하고, `properties`는 딕셔너리처럼 접근해야 하죠.

```python
# 긁어온 쿼리를 다음의 방향성이 있는 그래프에 넣어준다.
DG = nx.DiGraph()

for i, path in enumerate(results):
    # 앞서, 쿼리에서 변수명을 n1, n2, e, 로 가져왔으므로 각 값에 할당된 것을 변수에 추가로 넣어준다.
    n1, n2, e = path['n1'], path['n2'], path['e']
    # 그리고, 보통 노드의 경우는 id, labels, properties 로 나누어 정보가 저장되어 있다.
    # 이를 가져오기 편하게, dictionary로 변경한다. 
    n1_dict = {
        'id': path['n1'].id, 
        'labels':path['n1'].labels, 
        'properties':dict(path['n1'])
    }
    n2_dict = {
        'id': path['n2'].id, 
        'labels':path['n2'].labels, 
        'properties':dict(path['n2'])
    }
    # 마찬가지로, edge의 경우도 아래와 같이 정보를 저장한다.
    e_dict = {
        'id':path['e'].id, 
        'type':path['e'].type, 
        'properties':dict(path['e'])
    }
    # print(e_dict)
    # 해당 노드를 넣은 적이 없으면 넣는다.
    if n1_dict['id'] not in DG:
        DG.add_nodes_from([
            (n1_dict['id'], n1_dict)
        ])
    # 해당 노드를 넣은 적이 없으면 넣는다.
    if n2_dict['id'] not in DG:
        DG.add_nodes_from([
            (n2_dict['id'], n2_dict)
        ])
    # edge를 넣어준다. 노드의 경우 중복으로 들어갈 수 있으므로 중복을 체크해서 넣어주지만, 
    # edge의 경우 중복을 체크하지 않아도 문제없다.
    DG.add_edges_from([
        (n1_dict['id'], n2_dict['id'], e_dict)
    ])
```

## wrap-up

- 뭐, 생각보다는 간단한 것 같습니다. 결국은 테이블의 형태로 쿼리 결과를 가져온 다음 그 데이터를 사용해서 그래프를 다시 만들어주는 형식인 것이죠. 
- 결국 이는 그래프(Neo4j) ==> 테이블 ==> 그래프(networkx)로 변환됩니다. 중간에 테이블로 변환하는 것을 빼고, 더 빠르게 graph to graph로 변환하는 방법이 가능하다면 훨씬 효율적일 것 같은데요, 아직은 이걸 어떻게 해야 하는지 선명하게 보이지는 않네요. 

## raw code

```python
import networkx as nx
# pip install neo4j-driver
from neo4j.v1 import GraphDatabase, basic_auth

## 
IP_ADDRESS =""
BOLT_PORT  = ""
USER_NAME = ""
PASSWORD = ""
##

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

# 다음과 같이 쿼리하여, 노드, 엣지, 노드를 모두 가져온다.
# 그래도 전체를 다 가져오는 경우 부하가 많이 걸리므로, 100로 제한하여 가져와 본다.
input_query = """
MATCH (n1)-[e]->(n2)
RETURN n1, e, n2
LIMIT 100
"""

results = run_query(input_query)
# result => neo4j.BoltStatementResult object
print(results)
print(type(results))
print("=="*30)

# 긁어온 쿼리를 다음의 방향성이 있는 그래프에 넣어준다.
DG = nx.DiGraph()

for i, path in enumerate(results):
    # 앞서, 쿼리에서 변수명을 n1, n2, e, 로 가져왔으므로 각 값에 할당된 것을 변수에 추가로 넣어준다.
    n1, n2, e = path['n1'], path['n2'], path['e']
    # 그리고, 보통 노드의 경우는 id, labels, properties 로 나누어 정보가 저장되어 있다.
    # 이를 가져오기 편하게, dictionary로 변경한다. 
    n1_dict = {
        'id': path['n1'].id, 
        'labels':path['n1'].labels, 
        'properties':dict(path['n1'])
    }
    n2_dict = {
        'id': path['n2'].id, 
        'labels':path['n2'].labels, 
        'properties':dict(path['n2'])
    }
    # 마찬가지로, edge의 경우도 아래와 같이 정보를 저장한다.
    e_dict = {
        'id':path['e'].id, 
        'type':path['e'].type, 
        'properties':dict(path['e'])
    }
    # print(e_dict)
    # 해당 노드를 넣은 적이 없으면 넣는다.
    if n1_dict['id'] not in DG:
        DG.add_nodes_from([
            (n1_dict['id'], n1_dict)
        ])
    # 해당 노드를 넣은 적이 없으면 넣는다.
    if n2_dict['id'] not in DG:
        DG.add_nodes_from([
            (n2_dict['id'], n2_dict)
        ])
    # edge를 넣어준다. 노드의 경우 중복으로 들어갈 수 있으므로 중복을 체크해서 넣어주지만, 
    # edge의 경우 중복을 체크하지 않아도 문제없다.
    DG.add_edges_from([
        (n1_dict['id'], n2_dict['id'], e_dict)
    ])
print("=="*30)
print("==: network is generated")
for n in DG.nodes(data=True):
    print(n, n[1]['labels'], n[1]['properties'])
    print("--"*30)
for e in DG.edges(data=True):
    print(e)
    
```