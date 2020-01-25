---
title: (한글 번역) Graph Databases for Beginners - ACID vs. BASE Explained
category: others
tags: neo4j graphdb database 
---

## intro 

- 2018년 11월 13일에 작성된, [이 링크](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/)에 있는 영어 원문을 한글로 번역하였습니다. 

## (한글 번역) Graph Databases for Beginners - ACID vs. BASE Explained

> When it comes to NoSQL databases, data consistency models can sometimes be strikingly different than those used by relational databases (as well as quite different from other NoSQL stores).
- NoSQL 데이터베이스에 관해서, 데이터 일관성 모델(data consistency model)은 관계형DB(relational db)와 종종 극도로 다를 수 있다. 

> The two most common consistency models are known by the acronyms ACID and BASE. 
- 보통 가장 일반적인 일관성 모델(consistency model)은 약어로, ACID, BASE로 알려져 있다. 

> While they’re often pitted against each other in a battle for ultimate victory (please someone make a video of that), both consistency models come with advantages – and disadvantages – and neither is always a perfect fit.
- ACID와 BASE가 종종 서로를 이기려고 하기도 하지만, 두 일관성 모델 모두 장점과 단점을 모두 가지고 있씁니다. 어떤 것도 완벽하게 fit하지 않다.

> Let’s take a closer look at the trade-offs of both database consistency models.
- 따라서, 두 데이터베이스 일관성 모델간의 장단점(trade-off)를 좀 더 살펴보겠다. 


### The ACID Consistency Model

> Many developers are familiar with ACID transactions from working with relational databases. As such, the ACID consistency model has been the norm for some time.
- 많은 개발자들이 relational database에서 돌아가는 ACID transaction에 친숙할 것이다. 그래서, ACID consistency model이 오랫동안 표준(norm)으로 인식되어 왔다. 

> The key ACID guarantee is that it provides a safe environment in which to operate on your data. The ACID acronym stands for:
- ACID가 확시하게 보증해주는 것(guarantee)은 그것이 너의 데이터가 동작하는 안정한 환경을 제공해주는 것이다. ACID의 약어는 다음을 상징하는데. 

> Atomic: All operations in a transaction succeed or every operation is rolled back.
- 원자성: transaction의 모든 동작(operation)은 모두 적용되거나, 모두 적용되지 않거나 해야 한다.

> Consistent: On the completion of a transaction, the database is structurally sound.
- 일관성: 트랙잭션이 완료되었을 때, 데이터베이스는 구조적으로 문제가 없어야 한다. 가령, 데이터 타입이 바뀐다거나, 오류가 난다거나 하는 일 없이 일관적인 상태를 유지해야 한다는 거싱죠.

> Isolated: Transactions do not contend with one another. Contentious access to data is moderated by the database so that transactions appear to run sequentially.
- 고립성: 트랜젹선이 다른 트랜잭션과 충돌해서는 안된다. 트랙젹선들이 순차적으로 시행되도록 하기 위해서, 데이터에 대한 충돌적인(contentious) 접근은 DB로부터 조정되어야 한다.

> Durable: The results of applying a transaction are permanent, even in the presence of failures. 
- 영속성: 트랜젹선이 적용된 이후의 결과는 DB에서 영구적으로 유지되어야 한다. 

> ACID properties mean that once a transaction is complete, its data is consistent and stable on disk, which may involve multiple distinct memory locations.
- 즉, ACID 성질은 "만약 트랜잭션이 종료되면, 그의 데이터는 일관적으로 작성되어야 하고, 만약 여러 구별된 메모리가 있다고 하더라고 디스크에서 안정적이어 한다. 

> Write consistency is a wonderful thing for application developers, but it also requires sophisticated locking which is typically a heavyweight pattern for most use cases.
- write consistency는 어플리케이션 개발자에게 매우 효과적인 것이지만, 그것은 동시에, 매우 정교한 locking 기법을 요구한다. 그러한 기법은 대부분의 사용 사례들에서 매우 무겁게 사용되기도 한다.

> When it comes to NoSQL technologies, most graph databases(including Neo4j) use an ACID consistency model to ensure data is safe and consistently stored.
- NoSQL 기술들에서는 Neo4j를 포함한 대부분의 graph DB는 데이터의 안정성과 일관성을 보증하기 위하여, ACID 일관성 모델을 사용한다. 

### BASE Consistency Model

> For many domains and use cases, ACID transactions are far more pessimistic (i.e., they’re more worried about data safety) than the domain actually requires.
- 많은 분야들과 실제 사용 사례들에서, ACID 트랜잭션은 실제로 그 분야에서 원하는 것(the domain actually requires)보다 더 비관적으로 여겨져 왔다.

> In the NoSQL database world, ACID transactions are less fashionable as some databases have loosened the requirements for immediate consistency, data freshness and accuracy in order to gain other benefits, like scale and resilience.
- NoSQL DB의 세상에서 ACID 트랜잭션은, 데이터의 용량 문제(scale)와 안정성 및 유연성(resilence)을 획득하기 위해서는 다른 DB가 즉각적인 일관성(immediate consistency), 최신 데이터에 대한 정확도 에 대한 요구사항을 약화시킴으로써, 좀 유행이 지난 것처럼 느껴진다. (resilence의 경우 유연성/탄성이라고 해석이 되지만, 다양한 예외상황에 대해서 해당 DB가 얼마나 효과적으로 대처할 수 있는지를 의미하는 개념으로, '안정성'이 확장된 것으로 해석하였다)

> (Notably, the .NET-based RavenDB has bucked the trend among aggregate stores in supporting ACID transactions.)
- 주목할만한 것은, .NET 기반의 RavenDB가 ACID transaction을 지지하면서, aggregate store의 유행(ACID를 사용하지 않는)에 저항하고(buck) 있다. 

> Here’s how the BASE acronym breaks down:
- BASE의 약어는 다음으로 구성된다.

> Basic Availability: The database appears to work most of the time.
- 기본적인 가용성: 데이터베이스는 대부분의 시간동안 동작하는 것처럼 보인다. 즉, 분산 DB에서 몇 개의 다른 DB는 문제가 있다고 하더라도, 살아있는 것이 있으므로 사용자에게는 계속 가용한 것으로 보인다는 것.

> Soft-state: Stores don’t have to be write-consistent, nor do different replicas have to be mutually consistent all the time.
- 저장소(store)는 작성 일관성(write-consistent)일 필요 없으며, 또한, 서로 다른 복제본들(replica) 또한 상호간에 항상 일관적일 필요가 없다. 즉, 각 노드의 값들이 어느 정도 비일관적으로 유지될 수 있다는 것이죠. 현재 노드가 반드시 최신으로 유지되지 않을 수도있고, 썻다고 바로 모든 노드에 적용되는 것은 아니다 라는 것이죠. 이는 다시 eventual consistency와 동일한 개념으로 받아들여질 수 있습니다.

> Eventual consistency: Stores exhibit consistency at some later point (e.g., lazily at read time).
- 최종적인 일관성: 외면적인 일관성을 나중에 저장한다. 즉, 변화가 바로 적용되지 않고, 몇 초 후에 적용되는 식으로 어느 정도의 시간은 비 알관적으로 디비가 유지된다. 사실, 이것은 분산 DB가 기본적으로 가지는, 통신에 따른 지연 시간으로 발생하는 것 때문이기도 하고. 무튼, 중간 중간 일관성을 잃더라도 결과적으로는 일관적이어야 한다는 이야기겠지. 

> BASE properties are much looser than ACID guarantees, but there isn’t a direct one-for-one mapping between the two consistency models (a point that probably can’t be overstated).
- 이처럼, BASE 성질은 ACID를 약하게 하고, 동시에 어떤, 일대일 매핑이 되는 것이 아닙니다.

> A BASE data store values availability (since that’s important for scale), but it doesn’t offer guaranteed consistency of replicated data at write time. 
- BASE 데이터 저장소(혹은 저장 방식)은 가용성(availability)에 가장 큰 가치를 둡니다. 따라서, 다양한 노드들에 분산되어 존재하는 데이터들에 대해서, 완전한 일관성이 데이터 작성시간(write-time)에 보장되는 것은 아닙니다.

> Overall, the BASE consistency model provides a less strict assurance than ACID: data will be consistent in the future, either at read time (e.g., Riak) or it will always be consistent, but only for certain processed past snapshots (e.g., Datomic).
- 전반적으로 BASE 일관성 모델은 보다 ACID에 비해 덜 엄격한 보증(assurance)을 제공합니다. 아마도, 미래에는 데이터가 일관적일 수 있습니다(특히, read time에는). 아니면, 특별히 처리된 과거의 snapshot에 대해서만 항상 일관적일 수도 있습니다.

> The BASE consistency model is primarily used by aggregate stores, including column family, key-value and document stores.
- BASE 일관성 모델은 기본적으로는  칼럼-패밀리, 키-밸류, 도큐먼트 스토어와 같은 aggregate stores에서 사용됩니다(Graph DB는 제외됨).

### Navigating ACID vs. BASE Trade-offs

> There’s no right answer to whether your application needs an ACID versus BASE consistency model. 
- 사실, 어플리케이션이, ACID를 따라야 하는지, BASE를 따라야 하는지에 대해서 명확한 답은 없다.

> Developers and data architects should select their data consistency trade-offs on a case-by-case basis – not based just on what’s trending or what model was used previously.
- 개발자들과 데이터 설계자들은 그들의 데이터 일관성에서 오는 기회비용을 다양한 측면에서 고려해서, 결정해야 한다. 무엇이 유행이고, 전에 무엇을 썼는지에 대해서 논의하는 것이 아니라. 

> Given BASE’s loose consistency, developers need to be more knowledgeable and rigorous about consistent data if they choose a BASE store for their application. It’s essential to be familiar with the BASE behavior of your chosen aggregate store and work within those constraints.
- 주어진 BASE의 약화된 일관성에서, 만약 그들의 어플리케이션에서 BASE 저장소를 사용한다면, 개발자들은 좀더 많은 지식을 갖추고 있어야 하고(knowledgable), 그들의 일관적인 데이터에 대해서 엄격할 필요가 있다. 또한, 당신이 선택한 aggregate store에서 그 제한사항(constrain)들에게 친숙해지는 것은 필수적이다.

> On the other hand, planning around BASE limitations can sometimes be a major disadvantage when compared to the simplicity of ACID transactions. A fully ACID database is the perfect fit for use cases where data reliability and consistency are essential (banking, anyone?).
- 반면에, BASE의 제한사항들에 대해서 행동하는 것은 ACID의 단순성과 비교했을 때, 큰 단점이 될 수 있다. 완벽한 ACID DB는 은행과 같은 데이터의 신뢰성과 일관성이 매우 중요한 곳에서는 아주 정확하게 맞아 떨어기 때문이다.

> In the coming weeks we’ll dive into more ACID/BASE specifics when it comes to aggregate stores and other graph technologies.
- 다음에는 aggregate store와, 나머지 graph technology에 관한 ACID/BASE에 대해서 좀 더 상세하게 알아보겠다.

## wrap-up

- 정리를 좀 해보겠습니다. 본 기사는 결국, 데이터베이스 갖춰야 하는 성질을 이야기한 것인데, 우선은, 기존의 데이터베이스들은 대부분 ACID를 따랐죠 혹은 따라야 했습니다. 일종의 표준, 이라고 생각하셔도 됩니다. 특히, 관계형 DB에서 유효해야 하는 성질이 바로 ACID인 것이죠. 
- 그런데, 시간이 지나고, 정확도가 물론 중요하지만, 정확도보다는 사용자가 필요할 때 데이터를 빠르게 전달하는 것, 빠르게 다양한 인터넷 환경 등의 상황에서도 문제없게 DB가 반응할 수 있도록 하는 것, 특히 대용량의 데이터가 전달될 때, 이 데이터를 어떻게 빠르게 저장할 수 있을지 등에 대한 고민이 늘어나게 됩니다. 너무 쉽지만, 사실 모든 것은 기회비용이라서, 빠르게 대응하기 위해서는 어느 정도는 무언가를 포기해야 하는 것이 필요하니까요. 그래서 나온 개념이 BASE라고 보입니다. 
- 그리고, 사실 저는 BASE와 같이 약어로 구성된 개념들을 별로 좋아하지 않습니다. 이렇게 구성된 개념은 각각이 모드 exclusive하게 되어 있어야, 이해가 되는데, 여기서의 개념은 그게 서로 배반적으로 구성되어 있는 것처럼 보이지 않아요. 그냥, '최종적으로는 정확하고, 일관적이지만, 분산된 노드별로 좀 일관적이지 않은 애들도 있고 서로 다른 애들도 있다. 어쨌거나, 결론적으로는, 약간의 부정확성을 통해서 빠르게 대응할 수 있도록 하는 것을 위한 DB'라고 생각하시면 되지 않을까 해요. 