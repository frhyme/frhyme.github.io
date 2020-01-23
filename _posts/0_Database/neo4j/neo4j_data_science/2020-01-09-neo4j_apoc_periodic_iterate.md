---
title: neo4j - cypher - apoc.periodic.iterate
category: others
tags: database graphdb neo4j cypher list jobmanagement
---

## neo4j - job management 

- DB를 전반적으로 관리할 권한을 가지고 있지 않고, 그저 데이터를 읽는 정도로만 사용할 때는 문제가 없지만, DB의 데이터 일관성과 같은 것들을 면밀하게 관리해야 할 때는 중요한 것은 일종의 load-balancing 이죠. 늘 말하지만, 데이터베이스에는 무한에 가까운(사실은 무한이 아니지만, 이렇게 생각해야 할정도로 아득히 큰 값들이 들어있으니까요), 데이터들이 들어있고, 이 데이터를 한번에 변경할 경우, 데이터베이스 자체가 터질 수도 있습니다. 뿐만 아니라, 만약 쓸 때 lock이 걸린다면, 데이터를 종료될때까지 날아가는 transaction들의 수는 또 상상을 초월하게 되죠.
- 따라서, 필요에 따라, 명령어가 주기적으로 분할하여 작업이 실행되는 것이 필요하며, 이를 위해 neo4j에서는 `apoc.periodic.iterate`라는 커맨드를 지원합니다.

## Periodic Execution

- [Periodic Execution](https://neo4j.com/docs/labs/apoc/current/graph-updates/periodic-execution/)
에 보다 자세한 설명이 작성되어 있으며, 저는 그중에서도 [apoc.periodic.iterate](http://neo4j-contrib.github.io/neo4j-apoc-procedures/3.5/cypher-execution/commit-batching/#commit-batching)를 설명합니다. 

```
CALL apoc.periodic.iterate(
    // first command 
    // 2번째 커맨드가 적용되어야 하는 대상.
    "MATCH (p:Person) WHERE (p)-[:ACTED_IN]->() RETURN p",
    // second command
    // 첫번째 커맨드에 무엇을 적용할 것인가?
    "SET p:Actor",
    // config: 
    // 
    {batchSize:10000, parallel:true}
)
```

- config에 대한 설명은 다음과 같습니다. 다른 것들도 많은데, 뭐, 이 둘 말고는 필요하지 않은 것 같아서 제외하였습니다.
    - `batchSize`: 한번에 second statement를 몇 개나 적용할 것인가?
    - `parallel`: second statement가 병렬로 돌아가게 할 것인가? 

## wrap-up

- `apoc`가 무슨 약자인지 봤더니, [Awesome Procedure On Cypher](https://neo4j.com/labs/apoc/)이더군요...
- 이런 식의 이름을 가진 라이브러리에 그냥 넣어두는 것은 사실, 좋은 설계가 아닌데, 그냥 일단은 여기에 둔 것 같아요. 
***Powered by Neo4j Labs.*** 라는 글도 적혀 있는 걸로 봐서는, 일종의 테스트 버전을 삭 넣어둔 것으로 보입니다.