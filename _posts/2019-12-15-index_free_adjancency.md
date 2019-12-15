---
title: index-free-adjacency
category: others
tags: database nosql sql graphdb 
---

## (번역) index-free-adjancency in wikipedia.

- 위키피디아에 있는 [index-free-adjacency](https://en.wikipedia.org/wiki/Graph_database#Index-free_adjacency)를 번역했습니다. 

> Data lookup performance is dependent on the access speed from one particular node to another. Because index-free adjacency enforces the nodes to have direct physical RAM addresses and physically point to other adjacent nodes, it results in a fast retrieval. 
- 데이터 검색 성능(Data lookup performanc)은 하나의 노드에서 다른 노드로 가는 속도에 의존저으로 처리됩니다. 
- index-free adjacency는 노드가 물리적인 RAM 주소를 가지도록 강제하고(포인터 같은 개념으로 생각하시면 됩니다), 따라서, 다른 노드를 물리적으로 탐색할 수 있기 때문에, 빠른 검색이 가능해진다. 

> A native graph system with index-free adjacency does not have to move through any other type of data structures to find links between the nodes. Directly related nodes in a graph are stored in the cache once one of the nodes are retrieved, making the data lookup even faster than the first time a user fetches a node. 
- index-free adjacency를 갖춘 native graph system은 노드들 사이의 관계(link)를 찾기 위해서, 다른 데이터 구조들을 따라갈 필요가 없습니다. 
- 노드가 검색되면, 그래프 내에서 그 노드와 직접 연결된 노드들은 캐시에 저장되며, 이를 통해, 데이터 검색이 훨씬 빠르게 진행됩니다.

> However, such advantage comes at a cost. index-free adjacency sacrifices the efficiency of queries that do not use graph traversals. Native graph databases use index-free adjacency to process CRUD operations on the stored data.
- 하지만, 이러한 장점은 비용을 가져오게 됩니다. index-free adjacency는 graph traversal이 아닌 질의(query)의 효율성을 희생합니다(즉, insert, delete 등과 같은 부분에 대해서는 더 많은 오퍼레이션이 필요하다고 할 수 있겠죠). native graph database는 index-free adjacency를 저장된 데이터에 대해서 CRUD 오퍼레이션을 처리하기 위해 사용합니다.

## index-free adjancency(more)

- 위키피디아에 설명된 것만으로도 대략은 이해가 되지만, 좀 명확하지 않은 부분들이 있어서, 다른 블로그에 있는 글들을 가져와서 좀 더 정리해봤습니다. 
    - [링크1](https://thomasvilhena.com/2019/08/index-free-adjacency)

> Graph databases are much more efficient than traditional relational databases for traversing interconnected data. The way they store data and execute queries is heavily optimized for this use case, and one property in particular is key for achieving such higher performance: index-free adjacency.
- Graph DB는 상호 연결된 데이터를 순회(traversing)하는 측면에서는 전통적인 traditional relational database보다는 훨씬 효율적이다. 특별히 이 use case에 대해서는 데이터를 저장하고, 질의를 실행하는 것이 굉장히 optimized되어(heavily optimized) 있는데, 이렇게 고성능을 달성하기 위한 핵심 요소가 바로 index-free-adajcency입니다. 


### Relational DB

> Since SQL by itself doesn’t support control structures and recursion, we need help of a procedural programming language for implementing this traversal algorithm, and fortunately most database systems do support structured programming out of the box for writing functions and stored procedures.
- (사실, 상호연결된 데이터를 가져오기 위해서는 relational DB에서는 join등을 사용해야 하는데)SQL은 그자체로, constrol structure나 recursion을 제공하지는 않는다. 오히려, traversal algorithm을 구현하기 위해서는 procedural programming language를 사용해야 하며, 다행히도, 대부분의 DB가 함수가, 프로시져를 구현할 수 있는 structured programming을 제공한다.

- 그리고, 본문에서는 이미 만들어둔 색인(해당 칼럼의 검색 조건에 대해서 빠르게 탐색하기 위해 따로 뽑아둔 주소값 처럼 이해해도 됨)을 통해서, recursion을 진행하는데, 그렇다고 해도, 오래 걸리는 것은 똑같음.

> Without the index things would be much worse, since a full table scan would be necessary to fetch followers, yielding O(V * n + E) time complexity in the worst case.
- 특히, DB의 index 없이는, 더 나빠지는데, follower를 전체 보기 위해서 full table 스캐닝이 필수적이며, 최악에는 O(V*n+E)의 계산 시간이 소요된다.

### Graph DB

- 앞서 말한 바와 같이, Graph DB가 Relational DB에 비해서, 이런 종류의 '연결된 데이터들에 대한 순회측면에서는 훨씬 효과적'인데, 이는 index-free-adjacency라는 것을 활용하고 있기 때문임.

> Instead of relying on a global index for accessing connected nodes, each node directly references its adjacent nodes. Even though the lack of a global index for nodes relationships is what gives the index-free adjacency property its name, you can think that each node actually holds a mini-index to all nearby nodes, making traversal operations extremely cheap.
- 연결된 노드들에 접근하기 위해서, global index를 사용하는 것 대신, 각 node(each node)가 직접 근접 node에 대해서 참조할 수 있도록 한다.
- 만약, 노드 관계에 대한 글로벌 인덱스(global index for nodes relationships)가 없기 때문에, index-free adjancency property에 각 이름이 부여되지만, 각 노드가 근처의 노드들(nearby nodes)에 대한 mini-index를 가지고 있음으로써, 순회 동작(traversal operation)을 훨씬 쉽게 할 수 있다.
- 설명이 어려운데, 기존에서는 global-index를 사용해서, 모든 노드에 대해서 그나마 쉽게 접근이 가능했다면, 이제는 각 노드에 인덱스를 통해서 쉽게 접근하는 것은 아니고, 한 노드에서 인접한/연결된 노드에 접근할때 mini-index처럼 쉽게 접근할 수 있도록 해서, 더 빠르게 접근할 수 있다는 것을 말합니다.

> As to leverage this structure, graph databases perform traversal queries natively, being able to execute the BFS algorithm from the previous section entirely whithin the database query engine. The BFS part will still execute O(V + E) operations, however the cost to fetch a user node followers will go down to O(1), running in constant time, since all followers are directly referenced at the node level.
- 이러한 구조를 강화(leverage)하기 위해서, Graph DB는 순회 쿼리를 기본적으로 수행하며, 전체 데이터베이스 쿼리 엔진에서 전체적으로 앞서 설명한 BFS 알고즘을 사용합니다. 그래서, 각 BFS 부분은 여전히 O(V+E)의 컴퓨팅 시간이 필요하지만, 유저 노드로부터 follower노드로 가는것(즉, 이웃노드를 탐색하는 것)은 훨씬 적은 비용이 들고, 고정된 시간이 필요합니다. 이는 물론, 모든 follower드이 직접 노드 레벨에서 서로를 참조하고 있을 때 가능한 것입니다.

> A lot of factors that affect database performance were left out of the analysis for simplicity, such as file system caching, data storage sparsity, memory requirements, schema and query optimizations.
- 그 외에도, 본문에서는, 단순화하기 위해서 데이터베이스의 성능에 영향을 미치는 다른 요소들을 제외하였습니다. 여기서는 file system caching, data storage sparsity, memore requirmeent, schema and query optimization등에 대해서는 제외되어 있습니다.

> There’s no single universal database that performs greatly in all scenarios. Different kinds of problems may be better solved using different kinds of databases, if you can afford the additional operational burden. As with most decisions in software development, a reasonable approach is to lay down your requirements and analyze whether or not tools available to you meet them before jumping to a new ship.
- 모든 시나리오, 모든 사용 상황에서 완벽하게 동작하는 범용적인 DB는 없습니다. 서로 다른 문제가 서로 다른 DB에서는 쉽게 해결될 수 있죠. 많은 소프트웨어 개발에서의 결정이 그러하듯이, 합리적인 접근은 당신의 요구사항을 규정하고(lay down) 그 도구가 당신의 요구사항을 만족시킬 수 있는지 분석하는 것부터 시작됩니다.

## wrap-up

- 어릴 때, 프로그래밍 언어인 C를 처음 배울 때, pointer라는 개념에서 허우적 거렸던 기억이 있습니다. 그저, 물리적으로 해당 변수가 존재하는 주소를 기억해놓고, 한번에 그주소로 가게 하는 것을 의미하는데, 그때는 그게 왜 그렇게도 헷갈렸는지 모르겠네요. 아무튼, 그때도, linked-list와 같은 것들을 보면서, 왜 이렇게 해야 하냐, 포인터를 통해 접근하는 것이 도대체 뭐가 빠르고, 왜 빠르고 뭐 그런 생각을 한참 했던 기억이 있습니다만, 오늘 index-free adjancency에 보면서 그때의 기억들이 떠오르네요. 
- 기존의 DB index는 칼럼에 대해서 값들을 색인처럼 만들어두고, 상대적으로 빠르게 탐색할 수 있도록 합니다. 이를 통해, 한번 찾을 때, 조금 더 빠르게 찾을 수 있게 되죠. 
- 하지만, 우리가 원하는 데이터 모델이 그래프 형태일때, 그래서, 해당 데이터 모델로부터 원하는 모델을 정확하게 가져오기 위해서는, 여러번의 Recursion이 필요하게 된다면, index만으로는 충분히 효과적으로 검색되지 않죠. 따라서, 그렇다면, 각 노드에 대해서 mini-index라는 개념으로 해당 노드의 근접 노드를 빠르게 접근할 수 있는 '포인터 같은 것'을 만들어둔다고 생각하면 됩니다. 그렇게 쓰고 보니, 결국 그냥 '링크드 리스트'의 개념으로 디비를 관리하는 것과 유사하게 느껴지네요. 그런 방식으로 값을 캐시에 저장하거나, 그렇게 해서 빨리 한다는 거시죠. 
- 다시, 그런데, 앞서 말한 것처럼 DB 에서 index는 read에서는 효과적이지만, update/write 등에서는 효과적이지 않습니다. 당연한 것이, 원래는 테이블에만 한 번 쓰면 되는 것이었는데, 이제는 테이블에도 쓰고, 인덱스에도 값을 고쳐줘야 하니까요. 이는 graphDB에도 동일하게 적용되는 조건입니다. 값이 테이블에 업데이트 되면, 미니 인덱스 들에 대해서 모두 업데이트되는 것이 필요하니까, 아마도, 더 많은 부하가 디비에 걸리게 되겠죠. 
- 매번 반복하는 것이지만, 똑같습니다. 모든 것에 완벽한 종류의 DB는 보통 없어요. 그래서, 우리한테 그래프디비가 얼마나 적합한지, 그것을 정하는 것이 가장 중요한 일이죠.

## reference

- [index-free-adjacency in wikipedia](https://en.wikipedia.org/wiki/Graph_database#Index-free_adjacency)
- 