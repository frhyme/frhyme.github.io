---
title: Python - Dictionary - 깊숙하게 합치자.
category: python-libs
tags: python dictionary python-basic
---

## Intro. 

- python으로 코딩하면서, 가장 많이 사용하는 아이가 바로 dictionary입니다. 필요에 따라서 그냥 set operation처럼 쓸 수도 있고, json으로 serialization하기도 편하고 다양한 편리함을 갖추고 있죠. 

## UPDATE dictionary simple

- 우리에게 여러 가지의 dictionary가 있다고 하겠습니다. 그리고 필요에 따라서, 이 dictionary들을 합치는 것이 필요할 수 있죠. 
- 가장 단순하게 합치는 방법은 그냥 `dict1.update(dict2)`를 사용해서, dict2의 정보를 dict1에 합쳐주는 것이 있죠. 

```python
dict1 = {
    0: 1
}
dict2 = {
    1: 2
}
print(
    dict1.update(dict2)
)
```

## UPDATE dictionary bettter.

- 저는 조금 특수한 방식으로 dictionary를 합칠 겁니다. 개별 dictionary를 network처럼 이해하면, `dict1`은 "0 => 1"이고, `dict2`는 "1 => 2"죠.

```python
dict1 = {
    0: 1
}
dict2 = {
    1: 2
}
```

- 이를 합치면, 대략 다음처럼 되어야 하는 것이 아닐까요? 0은 1로 갔다가 2로 가는 것이므로 최종 목적지를 바로 표현해주는 것도 새로운 방법이 되는 것이죠. 

```python
new_dict = {
    0:2, 
    1:2
}
```

- 매우 특수한 상황에 쓰일 것 같기는 하지만, 다음과 같이 간단하게 코딩하였습니다. 


```python
def MERGE_by_DEEP(dict_lst):
    """
    dict_lst에 들어 있는 dictionary들을 합쳐줌 
    단, 이 때, 해당 dictionary가 중첩될 경우 이를 반영함 
    예) MERGE_by_DEEP([{0:1}, {1:2}]) ==> {0:2, 1:2}
    ---------------------------
    dict_lst: merge할 dictionary들이 들어 있는 lst 
    - [dict1, dict2]
    """
    def cycle_included(input_dict):
        """
        input_dict에 0:1, 1:0 과 같은 cycle이 있는지 확인하고 
        True, False를 리턴함.
        """
        for k, v in input_dict.items(): 
            if v in input_dict.keys(): 
                if input_dict[v]==k: 
                    print("=="*40)
                    print(f"== Cycle {k} - {v} included")
                    print("=="*40)
                    return True
        return False

    return_dict = {}
    for each_dict in dict_lst:
        return_dict.update(each_dict)
    while True: 
        if cycle_included(return_dict) is True:
            # cycle이 있으면 진행해봤자 무의미하므로 그만둠.
            return None
        key_set = set(return_dict.keys())
        value_set = set(return_dict.values())
        if len(key_set.intersection(value_set))!=0: 
            # key와 value에 겹치는 것이 있으므로, 아직 끝까지 다 합쳐준 것이 아님. 
            for k in return_dict.keys():
                v = return_dict[k]
                if v in return_dict.keys():
                    return_dict[k] = return_dict[v]
        else: 
            break 
    return return_dict

```