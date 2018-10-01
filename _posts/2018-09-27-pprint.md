---
title: json 예쁘게 출력하기. 
category: python-libs
tags: python print pprint python-libs json
---

## intro 

- 요즘 json, xml 등을 사용하는데, 그냥 python의 기본 print로는 예쁘게 출력되지 않는 것 같아요. 
- 그래서 몇 가지를 사용해서 좀 예쁘게, 정확히는 사람이 인지하기 쉽게 출력해보는 것을 목적으로 합니다. 

## pprint 

- [pprint](https://docs.python.org/3.2/library/pprint.html)는 다음을 지원하는 모듈입니다. 

> The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter. 

- 그냥 python을 예쁘게 출력해주는 거라고 생각하시면 됩니다. 

- 간단하게 사용해보면 다음과 같죠. 
    - `pp`: 예쁘게 출력해주는 객체 
    - `pp.pprint(something)`: 으로 출력해줍니다. 직접 출력해주기 때문에, 딱히 문제는 없어요. 

```python
## dictionary print
import pprint
a = {
    1:{j:[i for i in range(0, 10)] for j in range(0, 5)}, 
    2:{j:[i for i in range(0, 10)] for j in range(0, 5)}
}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(a)
```

```
{   1: {   0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           4: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
    2: {   0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           4: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}}
```

- 그러나, 아래처럼 json의 경우에는 제가 원하는 것처럼 예쁘게 만들어주지는 않습니다. 
    - 딕셔너리 내부의 key 순서도 달라지고 들여쓰기도 영 이상하죠. 


```python
test = [
    {
        'name':'process_model01', 
        'model':[
            {'type':'activity', 'model':'act1'}, 
            {'type':'xor', 'model':[]}
        ]
    }, 
    
    {
        'name':'process_model02', 
    }
]
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(test)
```

```
[   {   'model': [   {'model': 'act1', 'type': 'activity'},
                     {'model': [], 'type': 'xor'}],
        'name': 'process_model01'},
    {'name': 'process_model02'}]
```

## using just json

- 이럴때는 그냥 json으로 변환할 때, indent를 넣어서 변환하고, 그 값을 출력해주는 것이 더 좋습니다. 

```python
import json

test = [
    {
        'name':'process_model01', 
        'model':[
            {'type':'activity', 'model':'act1'}, 
            {'type':'xor', 'model':[]}
        ]
    }, 
    
    {
        'name':'process_model02', 
    }
]

print("그냥 출력할 경우")
print(json.dumps(test))
print("=="*30)
print("indent를 넣어서 출력할 경우 ")
print(json.dumps(test, indent=4))
```


```
그냥 출력할 경우
[{"name": "process_model01", "model": [{"type": "activity", "model": "act1"}, {"type": "xor", "model": []}]}, {"name": "process_model02"}]
============================================================
indent를 넣어서 출력할 경우 
[
    {
        "name": "process_model01",
        "model": [
            {
                "type": "activity",
                "model": "act1"
            },
            {
                "type": "xor",
                "model": []
            }
        ]
    },
    {
        "name": "process_model02"
    }
]
```


## wrap-up

- 가능하면, 해당 데이터를 json으로 변환하고, 물론 변환시에 `indent` parameter를 함께 넘겨주고요. 그렇게 진행하는 것이 더 좋습니다. 



## reference 

- <https://stackoverflow.com/questions/9105031/how-to-beautify-json-in-python>