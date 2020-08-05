---
title: python-lib) functools cmp_to_keys
category: python-lib
tags: python python-lib functools functional-programming iterator
---

## intro 

- python 에서 유용하게 쓰이는 functools의 주요 함수들을 정리하였습니다. 모든 함수들을 정리한 것은 아니고, 제가 주로 쓰는 함수들을 중심으로 정리해봤습니다.

## functools.cmp_to_key

- `functools.cmp_to_key`는 두 요소간의 '순서상 우위'를 만들어주는 함수입니다.
- 이렇게 말하면 "무슨 소리야?"할 수 있으니, 예제를 통해 정리해보겠습니다.

### Problem - 리스트를 정렬합시다

- python으로 코딩할 때 자주 하는 것 중 하나는, list에 들어 있는 값들을 정렬(sort)하는 것이죠.
- 이 때 어떤 순서에 따라서, 비교우위를 평가할 것인지는 두 가지 방식으로 가능합니다.

### Sort by unary operator

- 가령, 우리에게 `[(1, 2), (3, 4), (5, 4)]`이라는, 각 원소를 tuple로 가지는 리스트가 있다고 하겠습니다. 이 때 각 원소에 대해서 어떤 값을 중심으로 정렬할 것인지는 상황에 따라 달라지죠.
- 이 때 만약 우리가 각 원소의 첫번째 값을 key로 하고 싶다면, `lambda x: x[0]`라는 람다식을 통해 정의하면 됩니다.
- 이처럼, 하나의 원소에 대해서 key값을 바로 뽑아낼 수 있는 경우를 unary operator라고 합니다.
- 이 때는 굳이 `functools.cmp_to_key` 없이도 그냥 하면 됩니다. 대충 다음 코드처럼 하게 되죠.

```python
lst = [(1, 4), (2, 3), (3, 2)]
# lambda x: x[1] 에 따라서, 정렬하게 됨.
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)  # [(3, 2), (2, 3), (1, 4)]
```

### Sort by binary operator

- 그런데, 만약 하나의 원소가 아니라, 원소간의 비교를 새롭게 정의해야 한다면 어떨까요? 
- 가령, A라는 원소와 B라는 원소가 있을 때, "이 둘의 크고 작고 같을 때를 모두 정의해준다"라고 생각하시면 됩니다.
- 조금 더 풀어서 말해보겠습니다. 일반적으로 1이 2보다는 작죠, 2는 3보다 작구요. 이건 왜 그런걸까요? 사실 수라는 것은 어떤 체계인데, 우리는 사실 늘 그렇게 배워온 겁니다. 그게 수학이 세워놓은 단단한 체계니까요.
- 그런데, 만약 어떤 상황에서 우리가 이러한 우열관계를 새롭게 정의해야 할 수가 있겠죠. 그럴때 binary operator를 사용해야 합니다.
- 가령 우리에게 다음과 같은 list가 있다고 해봅시다. 각 원소는 모두 길이가 같은 tuple로 구성되어 있습니다. 이 때 첫번째 원소에 따라 정렬하고, 첫번째 원소가 같다면 두번째 원소에 따라서, ..., 로 정렬한다고 해봅시다. 어떤가요? unary operator만으로 가능할까요? 될것 같기도 한데, 좀 tricky해지고, 해석이 더 어려워질 수 있습니다.

```python
lst = [(1, 2, 3), ... , (4, 5, 6)]
```

- 따라서, 두 원소간의 우열을 정의할 수 있는 새로운 함수를 만들어서 key로 넘겨준다고 하겠습니다. 이 때 `functools.cmp_to_key`가 필요하죠.
- 우선 두 원소간의 우열을 평가하여 `-1, 0, 1`로 리턴해주는 comparator를 만들어 줍니다.

```python
def cmp_func(tup1, tup2):
    """
    - 오른쪽이 클 경우 => -1
    - 오른쪽이 작은 경우 => -1
    - 왼쪽 오른쪽이 같은 경우 => 0 
    """
    if tup1[0] < tup2[0]:
        return -1
    elif tup1[0] > tup2[0]:
        return 1
    else:
        return cmp_func(tup1[1:], tup2[1:])
```

- 이렇게, comparator를 만들었지만, `sorted`와 같은 함수에서는 이 key를 그대로 받아들이지 못합니다. 따라서, 이 아이를 다음처럼 변환해서 넘겨줘야 하죠.
- 이렇게 하고 나면, 그 결과가 제가 원하는 것처럼 정확하게 나오게 됩니다.

```python
import functools

lst = [(1, 4), (1, 3), (1, 2), (2, 3)]
# 앞에서 만든 comprator를 functools.cmp_to_key 를 사용해서 key로 변환하여 넘겨줌
sorted_lst = sorted(
    lst, key=functools.cmp_to_key(cmp_func))
print(sorted_lst) # [(1, 2), (1, 3), (1, 4), (2, 3)]
```

## wrap-up

- 아시는 분은 알겠지만, python2에서는 `sorted`와 같은 built-in 함수에 `key`를 unary operator로도, binary operator로도 넘겨주어도 상관이 없었습니다. 
- 다만, python3로 넘어오면서 binary operator가 빠져버렸죠. 혹시 그 이유를 아시는 분들은 알려주시면 감사하겠습니다.