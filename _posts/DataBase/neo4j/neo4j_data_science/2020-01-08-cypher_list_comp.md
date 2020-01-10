---
title: neo4j - cypher - list comprehension
category: others
tags: database graphdb neo4j cypher list
---

## list comprehension in python

- python을 사용할 때, list comprehension을 자주 사용합니다. SQL적으로 표현하면 약간 sub-query느낌이 되기도 하죠. 가령, 다음과 같은 것을 말합니다. 다음 둘은 의미적으로 동일하죠. 다만, 아래의 코드가 훨씬 짧을 뿐만 아니라, 직관적입니다. 또한 필요에 따라서, generator처럼 만들어서, 휘발성으로 써버리고 버릴 수도 있쬬.

```python
result = []
for i in range(0, 10):
    result.append(i)
```

```python
result = [i for i in range(0, 10)]
```


## list comp in Cypher

- 이제 돌아와서, Cypher에서의 list comprehension에 대해서 알아봅시다. 
- 아래의 쿼리와 같이 쓰면 되는데, 사실 굳이 설명을 하지 않아도 좀 직관적으로 어떤 것을 수행하는지 보입니다. 
    - `range(0, 10)`에 속한 `x`를 순차적으로 읽으면서, 
    - `WHERE`의 조건을 만족하는 것들을 리턴한다는 것이죠. 
- 다만, `|` operator가 중간에 있는데, 이는 앞에서 생성된 값들을 어떻게 변형해서 가져올지, 즉 python에서의 map의 역할을 수행한다고 생각하시면 됩니다.

```
RETURN [x IN range(0,10) WHERE x % 2 = 0 | x] AS result
```
- 위의 쿼리를 python으로 처리하면 다음과 같죠. 

```python
result = [x**2 for x in range(0, 11) if x%2==0]
```

- 이렇게 보면 `|`는 일종의 pipeline처럼 보이기도 합니다. 만들어진 세트에 대해서 값을 연쇄적으로 넘길 수 있는 것으로 보이니까요. 따라서, 혹시나 싶어서 다음처럼 처리해봤지만, 오류가 발생합니다. 

```python
query = """
WITH [x IN range(0, 10) WHERE x % 2 = 0 | x^2 | x^2] AS result
RETURN result
"""
```

- 만약 이런 식으로 pipeline을 길게 생성하고 싶다면 오히려 `WITH, AS`를 써야 하죠. 다음처럼요.

```
query = """
WITH [x IN range(0, 10) WHERE x % 2 = 0 | x^2 ] AS result
WITH [x IN result | x^2] AS result
RETURN result
"""
```

- 또한 아래와 같이 graph에 대해서도 특정한 값을 가져와서 list로 처리할 수도 있죠.

```
MATCH (a:Person { name: 'Keanu Reeves' })
RETURN [(a)-->(b) WHERE b:Movie | b.released] AS years
```

## wrap-up

- 뭐, 해보니까 어렵지는 않습니다. 그리고, 다시 느끼지만, 프로그래밍 언어를 하나 잘 할 수 있게 되니까, 다른 것을 배울 때도 그것의 양식에 기반해서 배우게 되는 것 같아요. 이 언어는 기존의 언어와 무엇이 다른가, 어떤 것이 비슷한가, 왜 비슷한가 와 같은 것을 생각하게 되니까 훨씬 재밌는 것 같습니다. 호호. 여러분, 진부한 이야기지만 코딩하세요 호호호.