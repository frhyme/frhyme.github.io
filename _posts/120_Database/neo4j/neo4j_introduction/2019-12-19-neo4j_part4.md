---
title: neo4j - part4 - cypher
category: others
tags: database nosql sql graphdb cypher
---

## intro 

- [neo4j의 online-training course에서 cypher, 즉 그래프 쿼리언어에 대한 설명이 정리된 내용](https://neo4j.com/graphacademy/online-training/introduction-to-neo4j/part-4/)을 가져와서, 번역했습니다. 

## Introduction to Cypher(번역)

### About this module

- Cypher는 Neo4j DB로부터 데이터를 검색/작성/업데이트 등을 하기 위해 사용되는 질의어(Query Language)입니다. 흠, 왜 delete는 안 써있을까요. 물론 사소한 일이기는 합니다만. 
- 그리고, Cypher에 대한 보다 자세한 documentation은 [이 링크](https://neo4j.com/docs/cypher-manual/current/)에 있습니다. 따라서, 이 글에서는 비교적 간단하게만 정리되어 있습니다.
- 또 여담이지만, 'Cypher'는 힙합 문화에서 서로 돌아가며 프리스타일 랩을 하는 것을 의미합니다. 


### What is Cypher?

- Cypher는 선언적인 질의 언어(declarative query language)이며 그래프 데이터에 대하여 표현력이 풍부하고, 효율적인 질의를 가능하도록 한다. Cypher를 사용하면, 복잡한 디비 쿼리도 쉽게 표현되어지며, 일반적인 DB언어들은 문법을 고려하다가 길을 잃는데, Cypher는 단순하고, 효과적이기 때문에, 해야 할 일에만 집중할 수 있다. 
- 여기서, 'declarative'는 procedural에 반대되는 말입니다. 쉽게 말하자면, C, C++과 같은 procedural 한 언어들로 작성된 코드를 보면 '어떤 일을 달성하기 위해서 어떻게 해야 하는지'에 대해서 자세하게 작성되어 있습니다. 하지만, '선언형'의 경우는 '어떻게 해야 하는 것보다, 무엇을 해야 하는지에 대해서' 좀 더 정확하게 서술되어 있습니다. 즉, SQL과 여기서 말하는 Cypher와 같은 언어들은 가령, 디비의 테이블에서 어떻게 루프 문을 짜고, 이런 세부적인 동작에 집중하는 것이 아니라, '무엇'을 해야 하는지 그 목적을 선명하게 드러내도록 작성이 된다는 것이죠. 어찌 보면, 일종의 고도의 캡슐화 등으로 세부적인 동작과 같은 것들은 뒤에서, 다 돌아가고, 앞에서는 선언적으로 '어떻게 하면 된다'만 결정해주면 알아서 해석해서 진행된다, 라는 것으로 생각하시면 될 것 같네요.

#### Cypher is ASCII art

- 사람들에게 읽혀지는 것에 맞춰서 최적화하기 위해서, Cypher의 구조는 질의어를 그 자체로 의미가 그대로 드러나도록, 자명하도록(self-explanatory) 만들기 위해, 영어의 산문체(prose)와 도상학(iconography)을 사용하였다. 
- 어렵게 되어있지만, 그냥 최대한 자연어에 가깝게 가령, 주어-동사-목적어 의 형태가 될 수 있도록 설계하였으며, 그 모양 또한 그래프 틱 하게 나타나도록 하였다, 라고 해석하면 될 것 같네요. 여기서 말하는 ascii art는 아래 그림과 같은 것을 말합니다. 

```
H   H EEEEE L     L      OOO       W   W  OOO  RRRR  L     DDDD  !!
H   H E     L     L     O   O      W W W O   O R   R L     D   D !! 
HHHHH EEEEE L     L     O   O      W W W O   O RRRR  L     D   D !! 
H   H E     L     L     O   O  ,,   W W  O   O R   R L     D   D    
H   H EEEEE LLLLL LLLLL  OOO  ,,    W W   OOO  R   R LLLLL DDDD  !!
```

- 아무튼 그래서, Cypher의 예를 보면 다음과 같습니다. 딱 보면 매우 직관적으로 보이는 것을 알 수 있습니다. 다만, 1) 노드와 엣지 사이에 공백이 있어도 커맨드가 문제없이 동작하는지, 2) 지금 모든 텍스트가 대문자인데, 항상 그래야 하는 것인지, 등의 것들이 조금 궁금하기는 하네요.

```
(A)-[:LIKES]->(B)
(A)<-[:LIKES]-(B)
(A)<-[:LIKES]-(B)-[:LIKES]->(C)
```

- Cypher는 데이터베이스를 명령적이고(imperative), 프로그래밍적인 관점에서 접근하는 다른 API 들과는 다르다. 이러한 접근은 physical database 구조가 변경되었기 때문에, 모든 순회(traversal)를 업데이트할 필요가 없어지므로, 개발자들에게 부담을 주는 대신, 쿼리 최적화나 구현을 세부적으로 할 수 있도록 하게 할 것입니다.
- 그러니까, 기존의 procedural language들의 경우(특히 RDBMS)는 데이터베이스의 기존 스키마가 달라지거나 할 경우 다른 모든 관련된 명령어들, 특히 그래프를 순회하기 위해 만들어놓은 많은 프로시져를 고쳐야 하는데, 여기서 제시하는 Cypher의 경우는 선언적이며, 무엇을 어떻게 해야 하는지를 중심으로 작성되어 있기 때문에, 유지 보수 측면에서 훨씬 안정적이라는 것이겠죠.

- Cypher는 수많은(a number of) 다른 접근법들로부터 영감을 받았으며, 표현력 높은 질의어(expressive querying)를 위해 잘 설립된 실행예제(established practices)들로부터 만들어졌다. 
- WHERE, ORDER BY와 같은 Cypher의 단어들은 SQL로부터 전해졌다. 그리고, Cypher의 패턴 매칭 기능은 SPARQL로부터 컨셉을 가져왔고, 다른 collections semantics 들은 haskell이나 python으로부터 가져왔다. 
- collections semantics이라는 말이 조금 낯설게 느껴질 수 있는데, 그냥 list/dictionary/enumerate/array 아무튼 뭐 그런 종류의 합해서 처리하는 일종의 컨테이너 같은 것이라고 할 수 있습니다.

- Cypher 언어는 GQL(Graph Query Language)를 first-class로 개발하는 측면에서, 수년간의 노력과 경험의 이득을 어떤 데이터베이스 공급자, 연구자, 다른 파티티들이 획득할 수 있도록(reap) openCypher를 통해 많은 사람들이 사용하고 구현할 수 있도록 가용되어 왔다.
- openCypher를 통해 구현되고 사용될 수 있으며, 어떤 데이터베이스 벤더나, 연구자, 다른 관심있는 사람들에게 모두 열려 있다. 
- [opencypher-projects](https://www.opencypher.org/projects)에 들어가보면, cypher를 폭넓게 사용하기 위해서 만들어진 많은 프로젝트들이 있습니다. 가령, RDBMS에 대해서 GRAPH적인 접근과 테이블적인 접근을 동시에 가능하도록 하기 위한 프로젝트라거나 아무튼 다양한 것들이 있습니다.

#### Nodes

- Cypher는 노드를 표현하기 위하여, 괄호(parentheses)인 `()`나 `(n)`사용합니다. 다시 말하지만, Node는 우리 영역에서 대상 개체(entity)를 의미합니다. 쿼리 프로세싱(query processing) 중에 특별한 제한(restriction)들이 없다면, 익명 노드 또한, `()`의 형식으로 존재할 수 있습니다. 이 부분의 경우 해석을 해보자면, 필요에 따라서 익명 노드가 필요할 수도 있을 것 같습니다. 물론, 진짜 필요한 use-case를 제가 아직 찾지는 못했구요. 쿼리 프로세싱 과정에서, 특히, 기존 DB에서 Constraint와 같은 방식으로 제한하는 것이 없다면, 여기서도 익명 노드를 만들 수 있다, 이런 말인 것 같네요.
- 그리고, 다른 방식으로 `(n)`의 형태로 노드를 정의하면, 쿼리 프로세서에게 이 쿼리는 `n`이라는 값을 이름으로 노드를 만든다는 것을 말하죠. 

#### Labels

- 그래프에서 노드는 labeled되어 있는데, label은 노드를 그룹화하거나, 그래프에 대해서 쿼리를 graph에 대해서 query를 filtering하는데 사용된다. 즉, label은 쿼리를 최적화하기 위해서 사용되는데, 만약 영화 DB가 구축되어 있다면, 이 영화 그래프에서 노드는 영화(Movie)나 사람(Person)과 같은 두 가지 유형의 노드를 표현하기 위해서 사용된다.
- 데이터 분석을 위해서 키워드를 구축할 때는 보통, 하나의 라벨만 존재하게 하는 경우가 많습니다. 가령, 제가 자주 연구하는 키워드 네트워크의 경우에는 제가 구축한 네트워크의 모든 노드의 label은 '키워드'일 뿐이죠. 물론, 더 정확하게 모델링하려면, '논문', '키워드', '저자'와 같이 많은 개체(entity)를 함께 네트워크로 표현할 수 있습니다. 즉, 이런 클래스명 과 같은 것이 모두 label이죠. 
- 그런데, 이러한 다양한 개체가 함께 존재한다고 보면, 여기서부터 다양한 sub-network를 뽑아낼 수 있습니다. 즉, 키워드 네트워크만 뽑거나, 저자 네트워크만 뽑는 식으로 처리하는 것이 가능하죠. 여기서 말한, 'label'을 사용해서 쿼리를 최적화한다는 것은, 결국 필요에 따라 맞는 라벨을 가진 노드만 구분하여 그래프에 대한 쿼리를 빠르게 처리하게 할 수 있다는 것이죠.

- 따라서, 내가 쿼리하는 노드의 유형별로 필터링을 할 수 있고, 동시에 node는 0개 혹은 여러 개의 라벨을 동시에 가질 수도 있습니다. 아래는 노드의 라벨에 대한 간단한 문법을 말하죠. 
- 아래 문법을 보면, 이름도 없고 label도 없는 것도 가능하고, 이름만 있거나, 라벨만 있는 것도 가능하고, 라벨이 여러 개 있는 것도 가능합니다. 다만 이름이 여러 개인 경우는 안되는 것이죠(물론 이건 너무 당연한 것이기는 하죠). 
- 그리고, 추가로 생각해보자면, '라벨이 여러개가 될 수 있다는 것'이 경우에 따라서 너무 자유분방해질 수 있습니다. 라벨을 일관적인 어떤 기준에 따라서 설정하지 않는다면, 이는 이후 그래프 자체의 정확도를 현저하게 떨어뜨리는 원인이 될 수 있습니다. 비슷한 예로는 인스타그램 태그 같은 것을 말할 수 있을 것 같아요. 만약 인스타그램 태그가 모든 글에 아주 정확하게 달려 있다면, 해당 글들을 아주 효과적으로 필터링할 수 있죠. 하지만, 이미 아시겠지만 인스타그램의 글들에 달려 있는 태그들은 아주 천차만별입니다. 어떤 글에는 몇 개 안 달려 있고 어떤 글에는 수십개가 달려있죠. 똑같이, 태그만으로 글들을 프로세싱한다면, 꽤 정확하지 않은 결과가 나올 수 있죠. 
- 따라서, label들이 지금 어떤 기준으로 작성되어 있고, 이것이 이후에 어떤 문제가 될 수 있다 라는 것을 방지할 수 있는 어떤 기능과 같은 것이 Neo4j에 존재하는지 혹은 DB에서 Constraint와 같은 방식으로 label의 관계를 제한할 수 이는지 궁금하네요.

```
()
(variable)
(:Label)
(variable:Label)
(:Label1:Label2)
(variable:Label1:Label2)
```

- 노드는 반드시 `()`를 가져야 한다. 그리고, `label`, `variable`은 모두 선택사항이며, 아래의 예는 노드를 정의하기 위한 Cypher의 예시다. 

```
()                  // anonymous node not be referenced later in the query
(p)                 // variable p, a reference to a node used later
(:Person)           // anonymous node of type Person
(p:Person)          // p, a reference to a node of type Person
(p:Actor:Director)  // p, a reference to a node of types Actor and Director
A node can have multiple labels. For example a node can be created with a label of Person and that same node can be modified to also have the label of Actor and/or Director.
```


#### Comments in Cypher

- Cypher에서는 comment를 `//`를 사용해서 표현한다. 


### Examining the data model

- 만약, 그래프에서의 데이터를 처음 배운다면, 그래프의 데이터 모델을 검사하는 것이 도움이 된다. 이 것은 `CALL db.schema`를 실행함으로써, 도움이 되는데, 이는 현재 노드, label, relationship에 대한 정보를 리턴해준다. 
- 원래 링크에는 그림도 포함되어 있는데, 노드, 라벨, 관계등을 시각화해서 보여줌으로써, 현재 데이터 모델이 어떤 형태로 구성되어 있는지를 보여줍니다.


### Using MATCH to retrieve nodes

> In this video, you will be introduced to using the MATCH statement to retrieve nodes from the graph in Neo4j Browser.
- 비디오에서는 그래프에서 노드를 검색하기 위해서 `MATCH`를 사용하는 것을 소개한다.

- Cypher에서 가장 범용적으로 사용되는 구문은 `MATCH`이며, `MATCH`는 그래프의 데이터를 대상으로 pattern match를 수행한다. 쿼리 프로세싱 중에, 그래프 엔진은 그래프 패턴에 맞는 모든 노드를 찾기 위해서 그래프를 순회(traverse)한다. 그리고, `MATCH`를 통해 찾아진 데이터는, `RETURN`을 통해서 그 결과를 확인할 수 있다. 
- 즉, `MATCH`를 통해 적합한 데이터를 선택하고, 그 결과를 `RETRUN`으로 확인한다는 말이 되죠. SQL로 비교하자면, MATCH ==> WHERE, RETURN ==> SELECT 가 된다고 보면 되겠네요.
- 아래의 형태가 간단한 형태의 Cypher 구문입니다.

```
MATCH (variable)
RETURN variable
```

```
MATCH (variable:Label)
RETURN variable
```

- `MATCH`, `RETURN` 모두 영어 대문자로 작성해야 한다. 이 coding convention은 Cypher Style Guide에 기술되어 있다. MATCH 구문에 label을 명시함으로써, 해당 label에 속하는 노드만 추출하는 것도 가능하다. 여기서 variable이 명시되는 것이 필수적이고, 그렇지 않으면, 아무것도 리턴하지 않게 된다. 간단한 예는 다음과 같다.
- 물론, SQL과 동일하게, 소문자로 해도 굴러가기는 합니다만, 가독성 측면이나 여러 이유로 대문자 쓰는 것을 추천하고 있는 것이죠. 그리고, 여기에서, n과 p 모두 변수인데, 그냥 제가 만들어주는 변수입니다. 그냥 `xxxxxx`라고 해도 상관없죠.

```
MATCH (n)           // returns all nodes in the graph
RETURN n
```

```
MATCH (p:Person)    // returns all Person nodes in the graph
RETURN p
```


### Exercise 1: Retrieving nodes

#### Properties

- Neo4j에서 Node(relationship도 마찬가지지만)는 해당 노드의 특성이 정의된 property를 가질 수 있습니다. 중요한 것은, 같은 타입의 노드라고 해도, 같은 property들을 가질 필요는 없다는 것이죠. 
- 가령, 노드가 'Moive'를 표현하기 위해서 정의되었다고 해도, 어떤 노드에는 name, year가 정의되어 있을 수 있고, 또 다른 노드에는 name/year/관객수 등 다른 정보가 더 포함되어 있을 수 있다는 것이죠. 다만, 저는 이 부분이 조금 낯설게 느껴지기는 합니다. 아마도 이후에 CONSTRAINT 등을 통해서 이를 가능 혹은 불가능하도록 관리하는 방법이 있겠죠.


Properties can be used to filter queries so that a subset of the graph is retrieved. In addition, with the RETURN clause, you can return property values from the retrieved nodes, rather than the nodes.
- 이러한 property는 그래프에서 해당 property를 가진 노드만을 필터링하기 위해서 사용되는데, RETURN 절에서, 노드 전체를 다 리턴하는 것이 아니라, 필요한 property value만 리턴해서 가져올 수 있다는 것을 의미합니다.


#### Examining property keys

- 쿼리를 작성하기 전에, 현재 property key가 어떤 것들이 있는지 확인하는 것이 필요한데, 이는 명령창에서 `CALL db.propetyKeys`를 통해 쉽게 알 수 있다. 다만, 어떤 노드에 어떤 프로퍼티가 있는지 나오는 것이 아니라, 그냥 모든 프로퍼티가 다 나온다.

#### Retrieving nodes filtered by a property value

- 노드를 검색할 때, 특정 label에 속하는 노드만 뽑아낼 수 있는 것처럼, 특정 property를 가진 노드만 솎아낼 수도 있다. 대략 간단하게는 다음과 같이 수행하면 된다.
- 아래 코드를 보면, 대략 알 수 있는데, `변수명:라벨명:{프로퍼티들}`로 쿼리가 구성된다. property는 파이썬의 딕셔너리처럼 넘겨준다고 생각하면 훨씬 편하다. 

```
MATCH (variable {propertyKey: propertyValue})
RETURN variable
```
```
MATCH (variable:Label {propertyKey: propertyValue})
RETURN variable
```
```
MATCH (variable {propertyKey1: propertyValue1, propertyKey2: propertyValue2})
RETURN variable
```
```
MATCH (variable:Label {propertyKey: propertyValue, propertyKey2: propertyValue2})
RETURN variable
```

- 다음의 형태로 테스트를 해봣는데, 프로퍼티딕셔너리와 라벨의 사이에 스페이스가 없어도 괜찮은 것 같습니다.

```
MATCH (p:Person{born:1970}) RETURN p
```

#### Returning property values

- 또한, 지금까지는 노드를 모두 한번에 리턴했는데(즉, 노드의 모든 property를 가져옴), 노드의 특정 프로퍼티만 가져올 수도 있습니다. 이 부분은 `RETURN` 부분에 명시되죠. 간단한 구조는 다음과 같습니다.

```
MATCH (variable:Label {prop1: value, prop2: value})
RETURN variable.prop3
```

```
MATCH (p:Person {born: 1970})
RETURN p.name
```

#### Specifying aliases

- 그리고 출력되는 결과물에 대해서 다름 이름을 정해줄 수도 있습니다.

```
MATCH (variable:Label {propertyKey1: propertyValue1})
RETURN variable.propertyKey2 AS alias2
```

- 아래와 같이, 이름과 연도를 각각 원하는 칼럼명으로 출력하도록 할 수도 있죠.

```
MATCH (p:Person {born:1970}) RETURN p.name AS name, p.born AS born_year
```

### Exercise 2: Filtering queries using property values

#### Relationships

> Relationships are what make Neo4j graphs such a powerful tool for connecting complex and deep data. A relationship is a directed connection between two nodes that has a relationship type (name). In addition, a relationship can have properties, just like nodes. In a graph where you want to retrieve nodes, you can use relationships between nodes to filter a query.
- Relationship은 Neo4j 그래프 자체가 더 포괄적이고 복잡하고 깊은 층위로 구성되어 있는 데이터를 강력하게 만들어주는 역할을 가지고 있다. A relationship은 두 노드간의 직접적인 연겨를 말하며, 이 연결 또한 relationship type을 가지고 있다. 그리고, relationship 또한, property를 가지고 있으며, 그래프에서 노드를 검색할 때, 관계(relationhip)를 사용해서 필터링할 수도 있다. 
- 여기서는 relationship이라는 이름으로 작성을 했고 맞는 말이기는 하지만, 저는 edge라는 말이 더 익숙합니다. node/edge가 일반적인 네트워크 분야에서 자주 쓰는 네이밍이니까요. 물론 개념적으로는 틀린 것이 아닌데, 일단 단어 자체고 relationship은 너무 길죠. 뭐 의미적으로는 좀 더 리치하다고 할 수 있지만요.

#### ASCII art

> Thus far, you have learned how to specify a node in a MATCH clause. You can specify nodes and their relationships to traverse the graph and quickly find the data of interest. Here is how Cypher uses ASCII art to specify path used for a query:
- 지금까지는 `MATCH`를 사용해서, 어떻게 노드를 구체적으로 표현하는지에 대해서 배워왔다. 그런데 그래프를 순회하고 필요한 데이터를 빠르게 찾는 과정에서는 관계 들에 대해서 구체화하는 것도 필요하다. 아래는 ASCII 아트를 사용해서 쿼리를 하는 방법을 설명하고 있다.

```
()          // a node
()--()      // 2 nodes have some type of relationship
()-->()     // the first node has a relationship to the second node
()<--()     // the second node has a relationship to the first node
```

#### Querying using relationships

> In your MATCH clause, you specify how you want a relationship to be used to perform the query. The relationship can be specified with or without direction. Here are simplified syntax examples for retrieving a set of nodes that satisfy one or more directed and typed relationships:
- `MATCH`에서 필요한 관계들을 다음과 같이 정의할 수 있습니다. 
- 앞서 말한 것과 같이, edge를 아스키 아트처럼 넣어주면 됩니다. 다만, `|`의 경우는 OR를 의미합니다. 즉, 두 릴레이션 중에서 어떤 릴레이션도 모두 허용된다는 것이죠.

```
MATCH (node1)-[:REL_TYPE]->(node2) RETURN node1, node2
MATCH (node1)-[:REL_TYPEA | :REL_TYPEB]->(node2) RETURN node1, node2
```

- 아래와 같이, Person 노드가 ACTED_IN 관계로 title property가 "The MATRIX"인 노드와 연결된 그래프를 추출하고, 이후, 거기서 p, rel, m을 뽑습니다.

```
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie {title: 'The Matrix'})
RETURN p, rel, m
```

- 여러 관계를 동시에 고려하고 싶다면 다음과 같이 해도 되겠죠. 동시에, 저 엣지의 라벨에 대한 부분을 비워두면, 그냥 익명 엣지로 고려되어서, 존재하는 모든 엣지를 찾게 됩니다.

```
MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN|:DIRECTED]->(m:Movie)
RETURN p.name, m.title
```

#### Anonymous Relationship

- 특정하지 않고, 우선 모든 관계를 다 뽑아낸 다음에, 하나씩 필터링하면서 보는 것이 더 효율적일 것 같아요. 물론 그 전에 미리 `CALL db.schema()`를 통해 일단 현재 데이토 모델의 상태를 확인하고 진행하는 것이 맞을 수도 있지만, 저는 이 편이 훨씬 효율적으로 느껴집니다.
- 아래를 보면, edge는 정의되어 있지만 `[]`의 형태로 해당 엣지가 어떤 라벨을 가져야 하는지, 정확히는 어떤 `type`인지에 대해서는 명확하게 작성되어 있지 않죠. 하지만, 각각 실행을 해보면, 문제없이 쿼리가 되집니다. 모든, 관계가 다 도출되는 것이죠. 

```
MATCH (p:Person)--(m:Movie {title: 'The Matrix'})
RETURN p, m
```
```
MATCH (m:Movie)<--(p:Person {name: 'Keanu Reeves'})
RETURN p, m
```

#### Retrieving the relationship types

> There is a built-in function, type() that returns the relationship type of a relationship. Here is an example where we use the rel variable to hold the relationships retrieved. We then use this variable to return the relationship types.
- 그리고 `type()`이라는 관계의 유형을 리턴하는 함수가 있습니다. 이는 `MATCH`부분에서 리턴된 그래프에서, 그 연결이 어떤 유형인지를 명시하고 싶을 때 사용해야 합니다. 

```
MATCH (p:Person)-[rel]->(:Movie {title:'The Matrix'})
RETURN p.name, type(rel)
```

- 이 `type` 함수는 관계에 대해서만 사용될 수 있습니다. 혹시나 해서, 노드에 대해서도 가능한가 싶어서 사용해봤는데, 다음과 같은 에러가 뜨네요. 

```
MATCH (p) RETURN type(p)
```

```
Neo.ClientError.Statement.SyntaxError: Type mismatch: expected Relationship but was Node (line 1, column 23 (offset: 22))
"MATCH (p) RETURN type(p)"
```

#### Retrieving properties for relationships

> Recall that a node can have as set of properties, each identified by its property key. Relationships can also have properties. This enables your graph model to provide more data about the relationships between the nodes.
- 노드가 여러 property를 가질 수 있고, property에 대해서 조건을 걸어서 노드를 필터링할 수 있죠. 마찬가지로 relationship 또한 프로퍼티를 가질 수 있습니다. 

- 우선, 영화 '다빈치 코드'에 참여한 모든 사람을 리턴해봅시다. 

```
MATCH (p:Person)-[]->(:Movie {title: 'The Da Vinci Code'}) 
RETURN p
```

- 그리고, 어떤 관계들이 있는지를 보려면 관계에 유형을 추가하면 되죠. 그리고, 그 관계에 유형을 집어넣어야 합니다.

```
MATCH (p:Person)-[rel]->(:Movie {title: 'The Da Vinci Code'}) 
RETURN p, type(rel)
```

- 결과를 보면 "REVIEWED"라는 관계까 눈에 띄네요. 이 관계만을 리턴해봅시다.

```
MATCH (p:Person)-[rel:REVIEWED]->(:Movie {title: 'The Da Vinci Code'}) 
RETURN p, rel
```

- 여기서 이 관계의 유형에는 'rating'이라는 값이 있고, 특정한 값을 가지는 애들만 데려와보기로 합니다. 다음처럼요. 노드에서도 간단히 `{}`로 관계의 성징을 결정했는데, 여기서도 마찬가지입니다. 즉, 그냥 아래와 같이 특정 property에 대한 값을 넣어주면 됩니다.

```
MATCH (p:Person)-[rel:REVIEWED {rating:65}]->(:Movie {title: 'The Da Vinci Code'}) 
RETURN p, rel
```

- 다만, 여기서 제가 가졌던 의문점은, rating은 숫자로 구성된 값이고, 완전히 똑같은 값보다는 비교를 통해서 크거나 작거나 한 값만 가져오는 것이 더 많지 않나? 였던 것이죠. 그래서 찾아봤는데, 이 부분은 `MATCH` 구문에서 처리할 수는 없고, 뒤에 `WHERE`과 같은 조건을 집어넣어서, 처리해야 하는 것 같습니다.

```
MATCH (p:Person)-[e:REVIEWED]->(:Movie {title: 'The Da Vinci Code'}) 
WHERE e.rating > 66 
RETURN p, e
```

#### Using patterns for queries

> Thus far, you have learned how to specify nodes, properties, and relationships in your Cypher queries. Since relationships are directional, it is important to understand how patterns are used in graph traversal during query execution. How a graph is traversed for a query depends on what directions are defined for relationships and how the pattern is specified in the MATCH clause. Here is an example of where the FOLLOWS relationship is used in the Movie graph. Notice that this relationship is directional.
- 지금까지, 노드, 프로퍼티, 관계 등을 사이퍼 쿼리문에서 정의하는 방법을 배웠다. 이 관계에는 방향성이 있을 수 있고, 이 때는 방향성을 고려해서, 쿼리를 작성하는 것이 필요하다. 아래와 같이, 아스키 아트와 같이 명령문이 작성되며 방향성이 있는 경우 없는 경우를 모두 고려해서 탐색할 수 있다.

```
MATCH  (p:Person)-[:FOLLOWS]->(:Person {name:'Angela Scope'}) RETURN p
MATCH  (p:Person)<-[:FOLLOWS]-(:Person {name:'Angela Scope'}) RETURN p
MATCH  (p1:Person)-[:FOLLOWS]-(p2:Person {name:'Angela Scope'}) RETURN p1, p2
```

- 그리고, 지금까지의 모든 명령문은 node -edge - node의 형태로만 정리되었었는데요 그렇지 않고 여러 복합 관계를 고려해서 표현할 수도 있습니다. 
- 아래를 보시면 node - edge - node - edge - node의 형태로 정리되어 있죠. 즉, 해석을 하자면, 제시카 톰슨의 팔로워의 팔로워를 모두 찾아서 보여준다는 것이죠. 즉, 이러한 방식으로 그래프를 쿼리하고, 결과를 뽑아내는 것도 가능합니다. 

```
MATCH  (p:Person)-[:FOLLOWS]->(:Person)-[:FOLLOWS]->(:Person {name:'Jessica Thompson'})
RETURN p
```

#### Cypher style recommendations

> Here are the Neo4j-recommended Cypher coding standards that we use in this training:
- Cypher를 쓸 때 코딩 규범에 대한 내용을 정리합니다.

> Node labels are CamelCase and begin with an upper-case letter (examples: Person, NetworkAddress). Note that node labels are case-sensitive.
- Node Label은 CamelCase로 쓰여지고, 대문자로 쓰여져야 한다. 실제로, Node Label은 대소문자를 구별한다.

> Property keys, variables, parameters, aliases, and functions are camelCase and begin with a lower-case letter (examples: businessAddress, title). Note that these elements are case-sensitive.
- Property key, variable, parameter, aliases 그리고 함수들도 모두 camelCase지만, 첫 글자는 lower-case로 시작한다). 

> Relationship types are in upper-case and can use the underscore. (examples: ACTED_IN, FOLLOWS). Note that relationship types are case-sensitive and that you cannot use the “-” character in a relationship type.
- 관계의 유형(Relationship type)은 대문자와 언더스코어로 작성된다. 대소문자는 구별되며, - 는 사용하면 안된다.

> Cypher keywords are upper-case (examples: MATCH, RETURN). Note that Cypher keywords are case-insensitive, but a best practice is to use upper-case.
- 사이퍼 키워드(MATCH, RETURN)은 모두 대문자로 작성한다. 하지만, 대소문자를 구별하지 않아도 돌아가기는 하는데, 대문자로 쓰는 것이 좋다.

> String constants are in single quotes, unless the string contains a quote or apostrophe (examples: ‘The Matrix’, “Something’s Gotta Give”). Note that you can also escape single or double quotes within strings that are quoted with the same using a backslash character.
- 문자열 상수는 홑따옴표로 표현된다. 

> Specify variables only when needed for use later in the Cypher statement.
- 변수 명은 cypher statement에서 사용할 때만 표현한다.

> Place named nodes and relationships (that use variables) before anonymous nodes and relationships in your MATCH clauses when possible.
- 이름 있는 node와 relationship은 가능하다면, 익명 노드/엣지보다는 앞에 위치시켜라

> Specify anonymous relationships with -->, --, or <--
- 익명의 관계에 대해서는 다음으로 펴현해라.


## wrap-up

- Cypher의 기본적인 사용법을 정리했습니다. 개념 자체는 그렇게 복잡한 것 같지 않습니다. 아직 손에 익지는 않았습니다만.