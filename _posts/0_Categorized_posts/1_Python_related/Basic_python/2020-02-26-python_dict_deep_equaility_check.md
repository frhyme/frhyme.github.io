---
title: python - dictioanry `==` operator recursive check? 
category: python-basic
tags: python python-basic operator dictionary
---

## 1-line summary 

- python dictionary에 대해서 `==` operator는 "내부 요소를 재귀적으로 파고들어가며 완전히 같은지를 확인"한다.

## `==` operator in python dictionary 

- 보통, dictionary를 사용할 때, '복사'를 하거나, `==`를 할때, 얘네가 deep copy하는지, shallow copy를 하는지 헷갈릴 때가 있죠. 
- python의 경우 고맙게도 dictionary, list 모두 deep equaility check를 해줍니다. 
- 아래 코드를 보시면, "nest dictionary", "nest list"의 경우에도 비교하여 equality를 정확하게 체크해주죠.

```python 
print("== equaility check start") 
####################################
# dictionary의 경우
# False
dictA = {'a':{'a':10}}
dictB = {'a':{'a':3}}
assert dictA != dictB

# True
dictA = {'a':{'a':10}}
dictB = {'a':{'a':10}}
assert dictA == dictB

# True
dictA = {'a':1, 'b':2}
dictB = {'b':2, 'a':1}
assert dictA==dictB

####################################
# list의 경우
# False
lstA = [0, 1, {'a':1}]
lstB = [0, 1, {'a':3}]
assert lstA != lstB

lstA = [0, 1, {'a': 1, 'b': 4}]
lstB = [0, 1, {'a': 1, 'b': 4}]
assert lstA == lstB
print("== equaility check complete")
```

## reference 

- [stackoverflow - What does the == operator actually do on a Python dictionary?](https://stackoverflow.com/questions/17217225/what-does-the-operator-actually-do-on-a-python-dictionary)
