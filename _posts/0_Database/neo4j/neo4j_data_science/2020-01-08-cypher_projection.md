---
title: neo4j - cypher - cypher projection
category: others
tags: database graphdb neo4j cypher list
---

## cypher projection in neo4j algorithm. 

- 요즘 neo4j에서 사용하는 pagerank algorithm을 조금 정리하고 있습니다. 
- 기본적인 사용법은 다음과 같죠. 즉, 첫번째에는 node label을, 두번째에는 relationship type을 세번째에는 config을 넘겨주면 되죠.

```
CALL algo.pageRank.stream('Article', 'CITED', {sourceNodes: sourceNodes})
YIELD nodeId, score
```

- 그런데, 몇몇 알고리즘에서는 위와 같은 형태로 사용하지 않고, 다음의 형태로 사용하곤 합니다.
    - 첫번째로는 node들의 ID가 들어가는 것처럼 보이고, 
    - 두번째로는 source, target이 들어가는 걸 보니, directional edge가 들어가고, 
    - 세번째 config 자리에는 `graph: "cypher"`라는 뜬금없는 값들이 들어가죠.

```
CALL algo.pageRank(
'MATCH (n) RETURN id(n) AS id',
"MATCH (n)-->(m) RETURN id(n) AS source, id(m) AS target",
{graph: "cypher"})
```

- 이게 무엇인가 찾아보니, [cypher-projection](https://neo4j.com/docs/graph-algorithms/current/projected-graph-model/cypher-projection/)이라고 하는, 즉 그래프를 필요에 따라서 가져오는 형태로 보입니다. 따라서 이 내용을 다음에 정리하기로 하였습니다.
- 굳이 algorithm에만 이러한 cypher-projection이 있는 이유는 알고리즘에 적용할 때, 다양한 sub-graph를 적용해야 할 필요가 있기 때문이겠죠. 단순히 node label, rel label 만으로 전달하는 것은 불충분하고, 다양한 쿼리에 맞춰서 노드와 edge를 전달할 수 있다면, 특정한 graph에 대해서 알고리즘을 적용할 수 있으니까요. 
- 따라서, 이러한 cypher-projection을 사용할 때는 다음의 용법에 따라서 사용하게 됩니다.
    - `node-statement` instead of the label parameter
    - `relationship-statement` instead of the relationship type
    - `graph:'cypher'` in the config.

- 따라서 다음의 형태가 되죠. 유의해야 하는 것은, node, source to target이 모두 id로 정리되어야 한다는 것이죠.

```
CALL algo.<name>(
  'MATCH (n) RETURN id(n) AS id',
  'MATCH (n)-->(m) RETURN id(n) AS source, id(m) AS target',
  {graph: "cypher"})
```

## wrap-up

- 필요에 따라서, 이런식으로 query를 만드는 것도 필요하겠지만, 쿼리가 전반적으로 가독성이 매우 떨어진다고 생각해요. 이렇게 쿼리를 직접 집어넣는 것보다는, `WITH`를 사용해서 node의 id만을 리스트로 넘기는 것은 불가능한지, 의문이 좀 남습니다.