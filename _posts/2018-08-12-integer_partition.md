---
title: integer를 분할해봅시다. 
category: python-basic
tags: integer partition python 
---

## 정수를 여러 그룹으로 쪼개죠. 

- 이미 [스택오버플로우](https://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning)에 잘 정리되어 있습니다. 제가 지금 정수를 다른 수들로 쪼개는 일이 필요해서 이용했는데, 그 참에 정리를 하려고 썼습니다. 
- 참 신기하게, 코딩을 제대로 하려고 하다보면, 수학적인 개념들이 좀 들어가게 되는 것 같아요. 학부때 공부를 좀 더 열심히 했었어야 했는데, 뒤늦게 정말 아쉽네요. 네 지금부터라도 열심히 하면 됩니다 라고 생각해야죠 하하하하 

## integer partition 

- 정수를 쪼갠다는 말입니다. 예를 들어, 3을 쪼갠 다고 하면 대략 다음처럼 세 가지 방법으로 나올 수 있습니다. 
- 슥 봐도 왠지 리커시브한 형태로 코딩을 해야 할 것 같은 느낌이 나지 않나요. 

```
[(3,), (1,2,), (1,1,1,)]
```

- 아무튼, 이런게 은근히 직접 코딩하려면 힘듭니다 하하핫 복잡해지죠. 
- 이미 있는걸 잘 씁시다. 

- 간단하게 binary partition을 해가면서, 왼쪽은 고정하고, 오른쪽의 모든 원소와 왼쪽을 결합시켜가면서 진행한다고 하면 됩니다. 

```python
def partition(number):
    answer = set()
    ## 일단 현재 number도 partition 중 하나 이므로 tuple로 넘겨주고 
    answer.add((number, ))
    ## binary partition: increase x and partition y 
    for x in range(1, number):
        for y in partition(number - x):## new partition of x 
            answer.add(tuple(sorted((x, ) + y)))## like this
    return answer
```

- 만약 여기서 partition되는 결과를 몇 세트(예를 들어, 2가지로 무조건 분할)로 쪼개고 싶다면 그 결과를 list compression이나 filter 를 사용하면 좋습니다. 

```python
[ x for x in partition(10) if len(x)==3]
```