---
title: generator와 recursion을 쓸 때는 yield from.
category: python-libs
tags: python python-basic recursion generator yield 
---

## 1-line summary 

- generator 내에서 다시 generator를 가져오는 경우, 해당 generator로부터 모든 원소를 가져오고 싶을 때는 `yield from`을 사용하자. 

## python basic - generator 

- generator는 그냥 "데이터를 읽어들이는 흐름"이라고 생각하시면 됩니다. 데이터의 크기가 적을 때는 큰 문제가 안되지만, 데이터의 용량이 커지면서, 모든 데이터를 한 번에 메모리에 처박아두고 쓰기는 힘들어지죠. 이럴 때는, 그냥 "데이터를 읽어들이는 흐름"만을 기억해두고, 필요할 때 각 원소만을 읽어서 처리하고 메모리에서 없앱니다. 즉, 매우 가볍게 사용할 수 있죠. 
- 간단한 예는 다음과 같죠. 그냥 함수 내에 loop를 만들고 그 안에 `yield`를 사용해서 `i`라는 값을 리턴해줍니다. 긜고 다음에는 다시 해당 함수로 돌아가서 그 다음의 값을 리턴해주죠.

```python
def not_generator(n):
    return [i for i in range(0, n)]

def generator(n):
    for i in range(0, n): 
        yield i 

# not generator(n): 
for x in not_generator(n):
    print(x)
# generator(n): 
for x in generator(n):
    print(x)
```

- 또한 간단하게는 `(i for i in range(0, 100))`의 형태로 사용할 수도 있습니다.

## recursion with generator

- 사실, 간단하게 쓸 때는 문제가 없지만, 가끔 recursion과 generator를 합칠 때 약간 다른 점이 생깁니다. 
- 즉, "generator 내에서 다시 generator를 불러서 사용하는 경우"에는 `yield`가 아닌 `yield from`을 사용해야 하죠. 
- 저는 간단하게 "list 혹은 integer로 구성된 복잡한 list에 대해서 integer이면 integer를 리턴하고, list이면 내부의 원소를 하나씩 읽어서 리턴해주는 generator"를 만들어보려고 합니다. 
- 그래서 다음처럼 generator를 만들어줍니다.

```python
def generator1(lst_of_lst): 
    # generator 
    for x in lst_of_lst: 
        if type(x)==list: 
            yield generator1(x)
        else: 
            yield x    
```

- 하지만 아래에 대해서 실행해보면 원하는대로 실행되는 것이 아니고 중간 중간 generator가 return되는 것을 알 수 있죠.

```python
a = [1, 
    [1, 2, [3]], 
    [[[[5]]]], 
    6, [7, [8]]
]
        
for x in generator1(a):
    print(x)
```

```plaintext
1
<generator object generator1 at 0x10ad33258>
<generator object generator1 at 0x10ad332b0>
6
<generator object generator1 at 0x10ad332b0>
```

- 그냥 `yield`만으로는 generator로 리터되는 원소가 container일 때 안에 존재하는 값들을 모두 읽어서 처리해주지 않습니다. 
- 따라서, 이를 해결하려면 `yield from`을 사용하면 내부의 값까지 모두 읽어서 처리하게 되죠.

```python

def generator1(lst_of_lst): 
    # generator 
    for x in lst_of_lst: 
        if type(x)==list: 
            yield from generator1(x)
        else: 
            yield x    

a = [1, 
    [1, 2, [3]], 
    [[[[5]]]], 
    6, [7, [8]]
]
        
for x in generator1(a):
    print(x)

```

## wrap-up

- 사실, 예전에 알았던 건데, recursion으로 뭘 풀다가, 잘 안되길래 다시 처리해보고 알았습니다 호호호. 

## reference

- [stackoverflow: Generator be recursive?](https://stackoverflow.com/questions/38254304/can-generators-be-recursive)
