---
title: networkx - unary operator - complement and reverse
category: python-libs
tags: python python-libs networkx graph-operator complement reverse
---

## 2-line summary 

- graph `G`의 complement `GC`는 "`GC`+`G` = complemet graph"라고 생각하면 됨. 
- Directed graph `G`의 `reverse`는 방향성을 반대로 하는 것을 말함(`(u, v)` ==> `(v, u)`)

## complement of `G`

- `complement`: graph `G`의 edge를 모두 없애고, 없는 edge만을 추가함. 

## reverse of `G`

- `reverse`: directed graph의 경우, 방향성을 모두 반대로 변경함
    - `(u, v)` ==> `(v, u)`



## reference

- [networkx - operators](https://networkx.github.io/documentation/stable/reference/algorithms/operators.html)