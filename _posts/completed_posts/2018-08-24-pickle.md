---
title: pickle로 모든 객체를 그대로 쓰고 읽읍시다. 
category: python-lib
tags: python python-lib pickle 
---

## serialization

- 간단하게 말하자면, 보통 데이터 구조, 함수, 객체 등을 다른 곳으로 전송해야 할 때(네트워크 통신으로 보내거나 혹은 다른 컴퓨터에 저장하는 것이든 무엇이든), 이를 일관적으로 유지하기 위해서 데이터를 특정한 포맷으로 변경하는 것을 말합니다. 
- xml, json csv 등이 이 serialization 과정에서 많이 쓰이죠. 

## pickle

- python에서는 pickle이 많이 사용됩니다. 

> The pickle module implements binary protocols for serializing and de-serializing a Python object structure.

- 이라고 하네요. 

### comparison with json 

- json과 비교를 간단하게 해보면, 다음과 같다고 합니다. 
    - JSON is a text serialization format (it outputs unicode text, although most of the time it is then encoded to utf-8), while pickle is a binary serialization format;
    - JSON is human-readable, while pickle is not;
    - JSON is interoperable and widely used outside of the Python ecosystem, while pickle is Python-specific;
    - JSON, by default, can only represent a subset of the Python built-in types, and no custom classes; **pickle can represent an extremely large number of Python types** (many of them automatically, by clever usage of Python’s introspection facilities; complex cases can be tackled by implementing specific object APIs).
- 즉, json이 훨씬 범용적이지만, pickle이 파이썬에서는 압도적으로 좋다, 정도로 해석할 수 있네요. 

## do it

- 아래처럼 잘 읽을 수 있구요. 

```python
## pickle test
import numpy as np 
import pickle
## read, write binary file 

orig_data = np.random.normal(0, 1, 1000)
## pickling: serialization 
with open('test.aa', 'wb') as f:
    pickle.dump(orig_data, f)
## unpickling: de-serialization 
with open('test.aa', 'rb') as f:
    new_data = pickle.load(f)
print(type(new_data))
print(all(orig_data == new_data))
```

```
<class 'numpy.ndarray'>
True
```

- 아래처럼 함수도 저장할 수 있습니다. 

```python
def test_function(inputA):
    print(inputA)
    
with open('test_func.aa', 'wb') as f:
    pickle.dump(test_function, f)
with open('test_func.aa', 'rb') as f:
    new_function = pickle.load(f)
new_function(10)
```

## wrap-up

- 그동안 은근히 파일을 외부에 저장하지 않고(왜냐면 저장하면 다시 읽고 변환하는 과정이 매우 성가시니까요) 그냥 썼는데 앞으로는 가능하면 피클링해서 써보면 좋을 것 같아요. 
- 흠. 좋은 것 같네요. 마음에 듭니다. 
- 단, 좀 더 찾아보니가 보안 과 일관성유지 측면에서는 pickle이 가지고 있는 한계점들이 있는 것 같아요. 안전하지 않은 곳과 통신할 때는 가능하면, json을 쓰는 것이 더 좋다는 이야기는 있습니다. 

## reference

- <https://docs.python.org/3/library/pickle.html>