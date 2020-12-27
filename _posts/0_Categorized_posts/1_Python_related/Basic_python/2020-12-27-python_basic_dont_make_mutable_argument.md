---
title: python Basic - Don't make Mutable Argument
category: python-basic
tags: python python-basic argument
---

## python Basic - Don't make Mutable Argument

- 다음과 같이, list에 새로운 원소를 넣어주는 함수가 있습니다.
- 뭐, 아무 문제가 없죠.

```python
def add_list(elem, returned_list):
"""
- returned_list에 elem을 append하고 리턴합니다.
- returned_list가 없을 경우 새로운 list를 만들어서 리턴합니다.
"""
    if returned_list is None:
        returned_list = list()
    returned_list.append(elem)
    return returned_list


if __name__ == '__main__':
    new_lst1 = add_list(1, [])
    new_lst2 = add_list(2, [])
    new_lst1 = add_list(2, new_lst1)


    print(new_lst1)  # [1, 2]
    print(new_lst2)  # [2]
```

- 그런데, 우리가 조금 깔끔하게 하려고 함수 `add_list`를 다음과 같이 변경했다고 해봅시다.
- default argument를 정해주는 것이죠. `returned_list`에 아무 값도 전달받지 않으면, 알아서 새로운 list를 만들어주도록 처리한 것입니다.

```python
def add_list(elem, returned_list=[]):
    returned_list.append(elem)
    return returned_list
```

- 이렇게 해놓고, 실행을 해보면, 다음처럼 이상하게 실행되는 것을 알 수 있습니다 

```python
def add_list(elem, returned_list=[]):
    returned_list.append(elem)
    return returned_list


if __name__ == '__main__':
    new_lst1 = add_list(1)
    new_lst2 = add_list(2)


    print(new_lst1)  # [1, 2]
    print(new_lst2)  # [1, 2]
```

## python function default parameter is evaluated only once

- Python function에서 Argument에 대해서 다음과 같이 동작합니다.
  - value(primitive type)일 경우, 값 자체가 복사되어 넘어가지만
  - reference(object)일 경우, 값을 복사해서 넘어가는 것이 아니라, 그대로 넘어갑니다.
- 아래는 value type과 reference type을 비교하기 위해 넣은 간단한 코드입니다.

```python
def pass_to_func(x, lst):
    x += 1
    lst.append(10)


if __name__ == '__main__':
    x = 10  # <class 'int'>
    lst1 = [1]  # <class 'list'>
    # x는 int 로 value type이지만
    # lst1은 list 로 reference type입니다.
    # 따라서 함수에 값을 넘기면 x는 복사되어 넘어가고
    # lst는 그대로 넘어가게 되죠.
    pass_to_func(x, lst1)
    # x: 10, lst: [1, 10]
    print(f"x: {x}, lst: {lst1}")
```

- 이제 본론으로 넘어옵시다. 
  - Default parameter는 함수가 실행될 때 생겨납니다(evaluation). 그리고 이 아이는 reference type이죠. 일단은 편하게 그냥 `list`라고 하겠습니다. 
  - 그리고 `add_list(1)`를 실행했다고 합시다. 그럼 새로운 `list`를 생성하고 1을 집어넣어서 `[1]`을 리턴하게 되죠.
  - 그럼 이 상태에서 function의 parameter는 이미 만들어진 `list`를 가리키게 되는 상황이죠. 그리고, function에서 parameter가 reference type인 경우 복사하지 않고 그대로 reference를 가져오게 됩니다. 
  - 이 상태에서 다시 `add_list(2)`를 실행할 경우 지금도 default parameter를 사용하게 되므로 이전에 가리켰던 `[1]`을 그대로 가리키게 됩니다. reference type을 가져올 때는 복사하지 않고 그대로 가져오기 때문이죠(shallow copy). 따라서 기존에 만든 `list`에 2를 추가하여 `[1, 2]`가 리턴되는 것이죠.

## Wrap-up

- 결과적으로, reference type의 `default Argument`는 무조건 `None`로 해라, 가 이 글의 교훈이군요.

## Reference

- [Stackoverflow - python function default parameter is evaluated only once](https://stackoverflow.com/questions/13087344/python-function-default-parameter-is-evaluated-only-once)
