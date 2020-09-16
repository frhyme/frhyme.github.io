---
title: list of list에서 unique한 것만 뽑기. 
category: python-basic
tags: python list set python-basic tuple data-structure
---

## intro

- 저는 파이썬으로 코딩할 때, class를 잘 만들지 않습니다. 여러 가지 이유가 있을 수 있겠지만, 기존에 잘 구성된(남이 만든) class를 가능하면 쓰려고 하고, 또 제가 쓰는 라이브러리들은 대부분 데이터 분석에 가까운 것들이라서, `pd.DataFrame`을 잘 이용하면 대부분 할 수 있기는 하니까요. 
- 아무튼, 그 외에도 가능하면 dictionary, list 등을 사용해서 코딩하려고 하는데, 그 와중에 '간단하다고 생각했던' 몇 가지가 안되는 일들이 있어요. 

## set of list

- list에서 unique set을 뽑으려고 할 때, 보통 다음을 사용합니다. 

```python
lst1 = [1,2,3,6,3,2,4]
print(lst1)
print(set(lst1))
```

```plaintext
[1, 2, 3, 6, 3, 2, 4]
{1, 2, 3, 4, 6}
```

- 그런데, list 안에 list가 또 있다면 어떻게 될까요? 
- 아래에서 보는 것처럼 list는 unhashable type이기 때문에 여기서 unique set을 뽑아내지는 못합니다. 

```python
lst1 = [[1,2,3], [1,2,3], [3,4,5]]
print(lst1)
print(set(lst1))
```

```plaintext
[[1, 2, 3], [1, 2, 3], [3, 4, 5]]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-08ba8f47a02d> in <module>()
      1 lst1 = [[1,2,3], [1,2,3], [3,4,5]]
      2 print(lst1)
----> 3 print(set(lst1))

TypeError: unhashable type: 'list'
```

## unhashable type: list

- 우선 list가 unhashable type이라는 것을 한번 알아봅시다. 
- 자세한 내용은 [여기에 나와있기는 합니다만](https://stackoverflow.com/questions/2671376/hashable-immutable). 

### hashable 

- hashable 이라는 것은 어떤 데이터를 hash 함수를 이용해서 hash 값으로 변환할 수 있다는 것을 의미합니다. 

### immutability

- 이는 해당 데이터(혹은 구조)가 변하지 않는 다는 것이 보장된다는 것을 의미합니다. 

### hashable and immutable 

- 자, 이런 가정을 해봅시다. mutable 한 데이터 구조가 있고, 이 구조를 hash할 수 있다고 하면, 음, 좀 이상해지지 않나요? 
- hash는 어떤 특정한 데이터에 대해서, 매우 유니크한 하나의 값을 가지게 됩니다. 
- 그런데, 원래 데이터가 변한다면, 이 데이터가 변함에 따라서 해당 hash 값도 항상 변하게 되겠죠. 
- 따라서, hashable하려면 우선 immutable해야 합니다.

### case of list

- list는 mutable합니다. 따라서 hash로 처리할 수 없고, 따라서 set 함수를 이용해서 처리할 수 없는 것이죠. 

## how to solve it

- 그냥 아래처럼 list를 immutable하게 변경해주면 됩니다. 

```python
lst1 = [[1,2,3], [1,2,3], [3,4,5]]
print(lst1)
tuple_lst1 = [tuple(l) for l in lst1]
print(set(tuple_lst1))
```

```plaintext
[[1, 2, 3], [1, 2, 3], [3, 4, 5]]
{(3, 4, 5), (1, 2, 3)}
```

## wrap-up

- 물론, 지금은 아주 간단한 경우에 대해서만 처리했습니다. 
- 또 그냥 list를 쓰지 않고, class 등을 사용해서 했다면 더 편해졌을 수도 있을 것 같기는 한데. 뭐 저는 이정도로도 만족합니다.
