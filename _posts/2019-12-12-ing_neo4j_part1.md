---
title: neo4j - graphDB
category: others
tags: neo4j graphdb database 
---

## intro 

- 요즘의 저는 시간이 좀 남아서, 대부분의 시간을 영어 공부를 하면서 보내고 있습니다. 어떻게 공부를 하는 게 좋을까 고민을 하다가 관심있는 분야의 글들을 번역하고 제 의견을 넣어서 정리하는 것이 재밌어 보이더라고요. 그래서 평소에 관심을 가지고 있던 [neo4j](https://neo4j.com/graphacademy/online-training/introduction-to-neo4j/part-1/)라는 graphDB의 자료를 한글로 정리해서 정리해두려고 합니다. 
- 특히, 이 포스트의 내용은 [이 링크](https://neo4j.com/graphacademy/online-training/introduction-to-neo4j/part-1/)에서 참고하였습니다. 

## neo4j: part 1 : Introduction to Graph Databases

### The evolution of graph databases

> Today’s business and user requirements demand applications that connect more and more of the world’s data, yet still expect high levels of performance and data reliability. Many applications of the future will be built using graph databases like Neo4j. In this video, you will learn how the need for graph databases has evolved.
- 오늘날의 사업과 사용자들의 요구사항들은, 더 높은 수준의 성능(performance)과 데이터에 대한 신뢰도(data reliability)를 기대하면서(아직 갖추어지지 못했음에도), 세계의 더 많은 데이터와 연결되려고 하고 있습니다. 
- 미래의 많은 어플리케이션들은 Neo4j와 같은 그래프 DB 위에서 구축될 것이며, 당신도 graph DB에 대한 수요가 어떻게 성장해 가는지를 아는 것이 좋을 것이다.

### What Is a graph database?

> A graph database is an online database management system with Create, Read, Update and Delete (CRUD) operations working on a graph data model. Graph databases are generally built for use with online transaction processing (OLTP) systems. Accordingly, they are normally optimized for transactional performance, and engineered with transactional integrity and operational availability in mind.
- graph DB는 CRUD(쓰고, 읽고, 변경하고, 삭제하는 것) 동작을 graph data model에서 수행하는 온라인 데이터베이스 관리 시스템을 말한다. 
- graph DB는 일반적으로 OLTP을 위해 만들어진다. 따라서, 그들은 보통 transactional performace에 최적화되어 있고, transactional 무결성(transactional integrity), operational availability에 맞춰서 설계뙤어 있다.

> Unlike other databases, relationships take first priority in graph databases. This means your application doesn’t have to infer data connections using foreign keys or out-of-band processing, such as MapReduce.
- 다른 DB와는 다르게, 관계(relationship)이 graphDB에서는 가장 중요하다. 이것은 우리의 어플리케이션이 foreign-key를 이용하거나 MapReduce와 같은 out-of band processing를 사용하여 데이터간의 관계를 추론해야 한다고 말하는 것은 아니다.

> By assembling the simple abstractions of nodes and relationships into connected structures, graph databases enable us to build sophisticated models that map closely to our problem domain.
- 개체(node)와 관계들을 연결된 구조(connected structures)로 조립하는 것을 통해, graphDB는 우리가, 우리의 문제 영역(problem domain)에 좀 더 밀접하고 정교하게 일치되는 모델을 만들 수 있도록 해준다. 

### The case for graph databases

> The biggest value that graphs bring to the development stack is their ability to store relationships and connections as first-class entities. For instance, the early adopters of graph technology reimagined their businesses around the value of data relationships. These companies have now become industry leaders: LinkedIn, Google, Facebook and PayPal.
- 그래프를 개발 도구(development stack)으로 가져왔을 때, 가장 큰 이득은 관계(relationship)와 연결(connections)을 가장 중요한 개체(first-class entities)로 보는 능력이다.
- 예를 들어서, graph 기술의 초기 도입자들은 데이터 관계의 가치들에서, 그들의 사업을 재구상했다. 이런 회사들은, 실제로 지금 산업의 리더가 되었다(링크드인, 구글, 페이스북, 페이팔)

> As pioneers in graph technology, each of these enterprises had to build their own graph database from scratch. Fortunately for today’s developers, that’s no longer the case, as graph database technology is now available off the shelf.
- 그래프 기술의 개혁자로서(pioneer), 이런 회사들은 바닥부터 그들의 고유한 그래프 DB를 구축해야 했다. 다행히도, 오늘날의 개발자들은, 더이상 그러한 경우에 속하지 않는다. 이제 그래프DB는 (마치 선반에서 꺼내는 것처럼), 손쉽게 구할 수 있다.

> In this video, you will learn how graph databases help you to model real-world data that needs to be connected as well as how Neo4j is used to solve real problems facing enterprises today.
- [이 비디오에서는](https://youtu.be/-dCeFEqDkUI?list=PL9Hl4pk2FsvWM9GWaguRhlCQ-pa-ERd4U), 그래프 DB가 당신이 연결되어야 하는, 당신의 실제 데이터를 어떻게 모델링할 수 있는지를 도와줄뿐 아니라, Neo4j가 기업이 오늘날 마주치는 다양한 실제 문제들을 어떻게 해결할 수 있을지에 대해서 알려준다. 


### What is a graph?

> A graph is composed of two elements: nodes and relationships.
- 그래프는 두 가지 구성요소로 구성된다. 점(node)과 관계(relationship) 혹은 선들.

> Each node represents an entity (a person, place, thing, category or other piece of data). With Neo4j, nodes can have labels that are used to define types for nodes. For example, a Location node is a node with the label Location. That same node can also have a label, Residence. Another Location node can also have a label, Business. A label can be used to group nodes of the same type. For example, you may want to retrieve all of the Business nodes.
- 각 노드는 개체(entity)를 의미한다. 이 개체는 사람, 장소, 어떤 것, 분류, 데이터 등 무엇이든 될 수 있다. Neo4j에서는 Node는 label, 그 노드의 유형을 알 수 있는 label을 가질 수 있다.
- 예를 들어, 위치 노드라면, 'Location'이라는 라벨을 가진 노드가 될 것이다. 각 노드가 반드시 하나의 라벨을 가져야 하는 것은 아니며, location, label, business 등 다양한 라벨을 가질 수 있고, 필요할 때, 해당 라벨을 가진 노드만 추출해서 볼 수도 있다.

> Each relationship represents how two nodes are connected. For example, the two nodes Person and Location, might have the relationship LIVES_AT pointing from a Person node to Location node. 
- 관계 혹은 선이라는 개념은 노드들이 어떻게 연결되어 있는지를 의미한다. 예를 들어, 두 노드가 각각 사람과 장소라면, "LIVES_AT(살고_있는)"와 같은 관계를 Person(사람)과 Location(장소) 사이에 만들 수 있다.

> A relationship represents the verb or action between two entities. The MARRIED relationship is defined from one Person node to another Person node. Although the relationship is defined as directional, it can be queried in a non-directional manner. That is, you can query if two Person nodes have a MARRIED relationship, regardless of the direction of the relationship. For some data models, the direction of the relationship is significant. For example, in Facebook, using the KNOWS relationship is used to indicate which Person invited the other Person to be a friend.
- 관계는, 두 개체간의 동사(verb)나 행동(action)을 의미한다. "MARRIED"는 Person 노드로부터 다른 Person 노드 간에 정의된다. 관계가 단방향적이더라도, 방향과 관계없이 쿼리할 수 있다. 즉, 두 사람 노드 사이에 MARRIED 관계가 있다면, 그 방향과 상관없이 검색할 수 있다. 
- 물론 몇몇 데이터 모델의 경우, 관계의 방향이 중요할 수 있다. 예를 들어, 페이스북에서 알고 있다(Knows) 관계의 경우 어떤 사람이 어떤 사람을 친구로 초대했는지를 의미하며, 이는 방향성이 있는 관계다.

> This general-purpose structure allows you to model all kinds of scenarios: from a system of roads, to a network of devices, to a population’s medical history, or anything else defined by relationships. The Neo4j database is a property graph. You can add properties to nodes and relationships to further enrich the graph model.
- 이런 일반적인 목적의 구조는 다양한 시나리오에 맞춰서 사용할 수 있다. 도로교통망, 기기들의 네트워크, 인구의 의료 기록 등 관계를 정의할 수 있는 어떤 것에도 적용할 수 있다.
- Neo4j 데이터베이스는 property graph이며, 그래프 모델의 정보를 rich하게, 즉, 풍부한 정보를 제공하기 위해서, node와 relationship에 성질을 넣을 수 있다. 

> This enables you to closely align data and connections in the graph to your real-world application. For example, a Person node might have a property, name and a Location node might have a property, address. In addition, a relationship, MARRIED , might have a property, since. In this video, you will learn how to model property graphs containing nodes and relationships and how Cypher is used to access a graph database.
- 따라서, 실제 데이터에서, 그래프의 연결성(Connection)과 데이터를 가깝게 정렬하는 것을 가능하게 한다. 예를 들어, 사람노드(person node)가 성질(property)과 이름(name)을 가지고 있다면, 위치 노드(Location node) 또한 성질을 가지고 있다. 또한, 관계(relationship) 들도 성질을 가지고 있다. 따라서, 비디오에서는, 우리가 property graph(노드와 관계를 포함한)를 설계하고, Cypher를 사용해서 그래프 데이터베이스에 접근하는 방법을 배우게 될 것이다.


### Modeling relational to graph

> Many applications’ data is modeled as relational data. There are some similarities between a relational model and a graph model:
- 대부분의 많은 어플리케이션들에서는 데이터가 relational data로 되어 있다. 그리고, relational model과 graph model에는 각각 유사한 점들이 많이 있다.
    - row ==> nodes
        - 관계형 DB에서 각 row는 하나의 개체를 의미합니다. 따라서, 각 row는 node와 유사하죠. 
    - join ==> relationship
        - 관계형 DB에서 join은 서로 다른 개체를 연결하는 것을 의미합니다. 관계형 DB에서 서로 다른 개체를 연결해서, 그들간의 관계를 보는 것이 join이고, 이는 그래프 DB에서는 relationship으로 각 개체간에 이미 저장되어 있기 때문에, 원하는 관계를 가진 개체들을 읽어 오면 되는 것이죠. 
    - table names ==> label. 
        - 테이블의 이름은 각 개체의 클래스를 의미합니다. 즉 label이 다시 각 개체가 어떤 클래스인지를 말해주는 것이고요.
    - columns ==> properties. 
        - 그리고, 각 칼럼은 각 개체의 attribute로 해석할 수 있으며, 이는 곧 '성질'이라고 할 수 있습니다.

> But, there are some ways in which the relational model differs from the graph model:
- 그리고, 당연히 차이점도 있습니다. 

> Each column must have a field value. ==> Nodes with the same label aren’t required to have the same set of properties.
- 관계형 DB에서는 각 rowd에 값들이 모두 존재해야 하는데, 그래프 DB에서는 같은 Label을 가지고 있다고 해도, 같은 property가 충족되지 않아도 됩니다. 

> Joins are calculated at query time. ==> Relationships are stored on disk when they are created.
- 관계형 DB에서는 join이 query될 때 실행되어, 상대적으로 쿼리시에 과부하가 많이 걸리는데, 그래프 DB에서는 관계가 이미 디스크에 저장되어 있습니다.

> A row can belong to one table. ==> A node can have many labels.
- 관게형 DB에서는 하나의 로우가 반드시 하나의 표에 포함되어 있어야 하지만, 그래프DB에서는 노드가 여러 라벨을 동시에 가지고 있을 수 있습니다.


### How we model: RDBMS vs graph

> How you model data from relational vs graph differs:
> Relational: Try and get the schema defined and then make minimal changes to it after that.
> Graph: It’s common for the schema to evolve with the application.
> Relational: More abstract focus when modeling i.e. focus on classes rather than objects.
> Graph: Common to use actual data items when modeling.
- 관계형 DB와 그래프 DB는 서로 다른 방식으로 데이터를 모델링하는데, relaional 의 경우 만든 이후, 스키마를 최소한의 수정만 가능한 스키마를 작성하는 반면, 그래프의 경우 어플리케이션이 발달함녀서, 스키마를 변경하는 것이 가능하고, 
- 관계형 DB의 경우 모델링하는 것보다는 추상화에 관심이 많은데, 그래프의 경우, 모델링 때에 실제 데이터 아이템을 그대로 쓰는 것이 가능하다, 는 차이가 있습니다.
- 이는, 결국 그래프 디비가 훨씬 직관적으로 대상을 표현한다고도 말할 수 있습니다.

### How does Neo4j support the property graph model?

> Neo4j is a Database – use it to reliably store information and find it later.
> Neo4j’s data model is a Graph, in particular a Property Graph.
> Cypher is Neo4j’s graph query language (SQL for graphs!).
> Cypher is a declarative query language: it describes what you are interested in, not how it is acquired.
> Cypher is meant to be very readable and expressive.
- Neo4j는 데이터베이스이며, 정보를 신뢰성있게 저장할 수 있고 또한 이후에 검색할 수도 있다. 
- Neo4j의 데이터 모델은 그래프, 특히 property graph이다. 
- cypher는 neo4j의 그래프 질의어이며, graph를 위한 SQL이라고 생각해도 된다.
- cypher는 선언적인 query language이며, 가독성있고 표현력이 좋다.


## reference

- [neo4j](https://neo4j.com/graphacademy/online-training/introduction-to-neo4j/part-1/)