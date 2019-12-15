---
title: aggregate store in Domain_Driven_Development
category: others
tags: graphdb database nosql 
---

## intro: aggregate

- [AggregateOrientedDatabase](https://martinfowler.com/bliki/AggregateOrientedDatabase.html)를 번역하여 정리합니다.
- 해당 글은, 2012년 1월에 [Martin fowler](https://martinfowler.com/aboutMe.html)는 소프트웨어 개발, 특히, 기업용 어플리케이션(처럼 큰 규모의 소프트웨어)를 개발할 때, 필요한 소프트웨어 아키텍쳐를 설계하는 분야의 전문가인 것 같습니다. [위키피디아에도 문서가 있는 것을 보면, 매우 유명한 사람이군요 호호](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer))
- 우선, 아래 글을 이해하려면, 'aggregate'라는 것에 대한 개념이 필요합니다. 이 개념은, 정확히는 'aggregate root'가 맞는데, [위키피디아에서는 다음과 같이 정리](https://en.wikipedia.org/wiki/Domain-driven_design#aggregate_root)되어 있습니다.

> A collection of objects that are bound together by a root entity, otherwise known as an aggregate root. The aggregate root guarantees the consistency of changes being made within the aggregate by forbidding external objects from holding references to its members.
- 하나의 주 단위(root entity)로 묶일 수 있는 오브젝트들의 집합. 즉, 어떤 데이터가 들어오거나 나갈때, 함게 없어지거나, 함께 적용되어야 하는 것을 말하는 하나의 데이터 단위. 관계형 DB로 봤을 때, 하나의 테이블에 종속적이지 않고 다양한 테이블에 걸쳐서 존재할 수 있는 하나의 단위.

> Example: When you drive a car, you do not have to worry about moving the wheels forward, making the engine combust with spark and fuel, etc.; you are simply driving the car. In this context, the car is an aggregate of several other objects and serves as the aggregate root to all of the other systems.

- 즉, 아주 기본적인 하나의 데이터 단위를 말한다고 생각하면 됩니다. 여기서, 기존의 RDB의 경우는 이 일종의 데이터 스키마와 같은 개념이 굉장히 빡빡하게 다루어졌는데, 이후에는 이 부분을 좀 느슨하게 한 편이죠. 보통 정규화니 어쩌고 하면서, 데이터를 쪼개고 각 테이블에 넣는 것을 없애고, 하나의 통짜 테이블, 처럼 관리한다고 생각해도 될것 같아요. 그리고 그 통짜 테이블의 하나의 행이, 여기서 말하는 aggregate가 됩니다.
- 즉, 여기서 설명할, aggregate store는 이처럼, 개체를 표현할 수 있는 하나의 형태를 그대로 저장하는 것이죠. document, key-value, column-family 모두, 그런 형태로 저장하고 있으며, 이를 aggregate store라고 하는 것 같습니다.


## (번역) Aggregate store

> One of the first topics to spring to mind as we worked on Nosql Distilled was that NoSQL databases use different data models than the relational model. 
- NoSQL 데이터베이스는 관계형 모델(relational model)과 다른 형태의 데이터 모델을 사용한다.

> Most sources I've looked at mention at least four groups of data model: key-value, document, column-family, and graph. 
- 지금까지 봐온 대부분의 DB들은 4가지 데이터 모델 중에 하나에 속한다. key-value, document, column-family, graph.

> Looking at this list, there's a big similarity between the first three - all have a fundamental unit of storage which is a rich structure of closely related data: for key-value stores it's the value, for document stores it's the document, and for column-family stores it's the column family. 
- 이 리스트 중에서, 처음 세 가지(key-value, document, column-family)의 경우는 굉장히 큰 유사점을 가지고 있는데, 모두, 기본적인 저장 요소가 데이터에 아주 밀접하게 관련된 데이터의 부유한 구조(rich structure)이기 때문이다. 
    - key-value 저장소의 경우 value, 
    - document store의 경우 document
    - column-family의 경우 column family를 가리킨다. 

> In DDD terms, this group of data is an DDD_Aggregate.
- 그리고, 이것을 DDD(Domain Driven Design) 용어로는 **DDD_Aggregate**라고 부른다.

> The rise of NoSQL databases has been driven primarily by the desire to store data effectively on large clusters - such as the setups used by Google and Amazon. 
- 구글과 아마존과 같은 곳에서 시작한, 많은 클러스터들(Large cluster)에서 데이터들을 효과적으로 저장하려고 하는 열망(desire)때문에, NoSQL 데이터베이스는 기본적으로 운영되어오기 시작했다.

> Relational databases were not designed with clusters in mind, which is why people have cast around for an alternative. 
- Relational database의 경우 클러스터에 적합하게 설계 되지는 않았다. 그것이, 사람들이 다른 대안을 찾아다닌 이유고.

> Storing aggregates as fundamental units makes a lot of sense for running on a cluster. 
- Aggregate를 기본 단위(fundamental unit)으로 구성하는 것은 클러스터를 운영하는 점에서는 이치에 맞는 것으로 보인다. 

> Aggregates make natural units for distribution strategies such as sharding, since you have a large clump of data that you expect to be accessed together.
- aggregate는 특히, 함께 접근할 수 있도록 하는, 대용량의 데이터가 있을 때, sharding과 같은 분산 전략(distribution strategies)을 자연스럽게 구사할 수 있도록 해준다.

> An aggregate also makes a lot of sense to an application programmer. If you're capturing a screenful of information and storing it in a relational database, you have to decompose that information into rows before storing it away.
- aggregates는 또한, 어플리케이션 프로그래머들에게도 많은 이점을 가져오게 된다. 
- 만약, 당신이 화면에 꽉차는 정보를 캡쳐하고, 관계형 DB에 넣어야 한다면, 당신은 그 정보를 저장해버리기 전에, 정보를 row(열)로 분해해야 합니다(이 말은, relational DB schema에 맞는 형태로 데이터를 분해해서, 각 테이블별로 로우를 쪼개어서 넣어야 한다는 말로 보입니다.)

> An aggregate makes for a much simpler mapping - which is why many early adopters of NoSQL databases report that it's an easier programming model.
- 여기서 aggregate의 경우, 훨씬 편한 방식으로 매핑할 수 있으며, 이것이 초기의 NoSQL DB 도입자(adopter)들이, 훨씬 쉬운 프로그래밍 모델이라고 했습니다.

> This synergy between the programming model and the distribution model is very valuable. It allows the database to use its knowledge of how the application programmer clusters the data to help performance across the cluster.
- programming model과 distribution model가 합쳤을 때 발생하는 시너지는 매우 가치가 있습니다. 
- 동시에, 이 시너지는 데이터베이스들이 '어플리케이션 프로그래머들이 데이터를 오는 방식에 대한 지식'을 클러스터 간의 퍼포먼스를 향상시키기 위해서, 사용될 수 있도록 한다.

> There is a significant downside - the whole approach works really well when data access is aligned with the aggregates, but what if you want to look at the data in a different way? 
- 전체적인 접근 방식(whole approach)는 데이터 접근이 aggregate에 맞게 정렬되어 있을 때만, 정말 잘 작동하겠지만, 만약 데이터를 다른 방식으로 보기 시작하면 어떻게 할 것이냐, 라는 중요한 약점이 존재한다.

> Order entry naturally stores orders as aggregates, but analyzing product sales cuts across the aggregate structure. The advantage of not using an aggregate structure in the database is that it allows you to slice and dice your data different ways for different audiences.
- order entry(개별 주문 데이터)는 자연스럽게, 주문(order)들을 합계로 저장하지만, 상품 판매를 분석하는 것은, aggregate structure에도 영향을 미치게 되죠.
- 즉, aggregate structure를 사용하지 않을 때의 이점은 '그것이, 당신에게 다양한 사람들에게 다양한 관점으로 데이터를 slicing, dicing할 수 있도록 해준다는 것이 있습니다'(즉, 기존의 관계형 DB(아주 잘 정리된 테이블들)에서는, 다양한 칼럼별로 데이터를 구분해서, 분석을 수행할 수 있는 반면, aggregate의 형태로 데이터가 정리되어 있을 때는, 이 데이터를 다양한 관점에서 비교해서 보는 것이 좀 어려워진다는 것이죠)

> This is why aggregate-oriented stores talk so much about map-reduce - which is a programming pattern that's well suited to running on clusters. Map-reduce jobs can reorganize the data into different groups for different readers - what many people refer to as materialized views. But it's more work to do this than using the relational model.
- 이것이, 왜 aggregate-oriented store가 여러 cluster에서 돌아가기에 적합한 프로그래밍 패턴인, map-reduce에 대해서 많이 이야기하는 이유죠. 
- Map-reduce 는 데이터를 다양한 그룹으로 재조직(reorganize)하여, 많은 사람들이, materizlized view(일종의 dashboard, 분석 리포트 라고 생각하셔도 됩니다)를 참고할 수 있게 해줍니다. 하지만, relational model에 대해서는 훨씬 많은 작업이 필요하게 되죠.

> This is part of the argument for PolyglotPersistence - use aggregate-oriented databases when you are manipulating clear aggregates (especially if you are running on a cluster) and use relational databases (or a graph database) when you want to manipulate that data in different ways.
- 이것이 PolyglotPersistence()에 대한 논쟁의 일부분입니다. 하나의 클러스터에서 돌아가는 경우에는, aggregate-oriented database를 이용하고, 데이터를 다른 방식으로 조작해야 할 때는 relational database나 graph db를 사용하는 것을 말하죠.

## wrap-up

- 다시 정리하자면, aggregate-store는 graph DB, relation DB를 제외하고, key-value, column-family, document-based의 데이터베이스 종류를 말합니다. 특히, aggregate를 기본으로 사용해서 각 데이터를 클러스터별로 저장해두는 것이죠. 다시 aggregate는 기본적인 데이터 개체의 단위를 말하는 것이라고 생각하면 됩니다. 저는 이를 통짜테이블을 만들었을때의 '행'을 말하는 것이라고 좀 대충 기억하기로 했습니다. 
- 혼자 코딩을 할때야 큰 문제가 없습니다만, 구글이나 아마존처럼 대용량의 데이터를 관리해야할 때는 단일 시스템에서 관리하는 것이 어려워집니다. 즉, 여러 클러스터를 묶어서 관리를 해야 하죠. 그런데, 기존의 RDB에서는 이 클러스터를 한번에 모두 관리하는 것이 과부하가 많이 걸립니다. 가령, 클러스터 별로 테이블을 따로 해두고 필요할 때마다 조인을 하거나 하는 식으로 번거롭게 해야 하나요 아니면 로우별로 쪼개서 해야 하나요? 무엇이든 번거로워지고 과부하가 걸리는 것은 마찬가지죠. 
- 따라서, 어떤 클러스터간의 의존 관계라고 할까요, 이를 해결하기 위해서 aggregate-store처럼 하나의 데이터 개체 단위가 존재하는 식으로 처리하는 것이죠. 그것이 여기에서 말하는 일종의 NoSQL이고, 이를 통해 샤딩과 같이 데이터를 좀 더 분산화해서 효율적으로 처리하는 부분이 좀 더 편해지죠. 
- 물론, 무엇이 가장 좋다! 뭐 이렇게 말하는 것에는 어려움이 있을 것이고, 클러스터별로는 NoSQL을 사용하고, 클러스터간에는 RDB를 사용하는 형태인 일종의 폴리글랏의 형태로 진행하는 것이 필요하다는 것까지가, 여기서 말한 내용들인 것 같습니다.