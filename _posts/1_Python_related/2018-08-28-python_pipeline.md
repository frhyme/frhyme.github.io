---
title: python에서 pipeline 만들기 
category: python-lib
tags: python python-lib pipeline reduce itertools functools accumulate julia lambda 
---

## pipeline??

- R이나 julia를 써보신 적이 있으신 분들은 아시겠지만, 이 두 언어에는 pipeline이라는 개념이 있습니다. 
- julia의 경우 대략 다음처럼 사용됩니다. 
    - 값 |> 함수1에 적용 |> 함수2에 적용 |> 함수3에 적용
    - 이를 수학적으로 표현하면 함수3(함수2(함수1(값))) 의 방식이 되죠. 사실 코딩할 때, 이렇게 작성하는게 매우 성가십니다. 

```julia
k_lst = [1,2,3]
for (i, k) in enumerate(k_lst)
    ## 아래와 같이 함수를 연속으로 나열합니다. 
    new_x = k |> (x-> x+1) |> (x-> 2*x) |> (x->x^2) |> log
    println("$i: $new_x")
end
```

```
1: 16
2: 36
3: 64
```

- 아무튼 간에 python에서는 이렇게 pipeline을 사용해서 처리하는 방법이 없습니다. 
- pipeline을 사용하면 함수를 모듈화하여 정리하여 오류를 줄일 수 있고 디버깅이 쉬워지고, 기정의된 여러 함수를 섞어서 새로운 복합함수를 정의하는 것도 매우 쉬워지거든요. 

- 예를 들어서, 현재 파이썬에서는 복합함수를 만드는 방식이 다음과 같아집니다. 
- 적용되는 함수가 안에서부터 밖으로 나가는것도 가독성이 떨어지고, 그걸 또 익명함수로 만들어야 하는 것도 좀 이상하구요. 

```python
a = lambda x: x+1
b = lambda x: x+2
c = lambda x: x+3
d = lambda x: x+4

z = lambda x: d(c(b(a(x))))## 순서가 반대임, 제일 안쪽에 있는 놈부터 적용됨, 사소한데 귀찮음. 
print(z(10))
```

- julia에서는 대략 다음처럼 진행됩니다. 가독성이 더 좋아지지 않나요?, 물론 제 생각일 수 는 있습니다만. 

```julia
## a, b, c, d 함수가 모두 정의되어 있다는 가정하에 
new_func = x -> x |> a |> b |> c |> d
```

## make pipeline in python

- 물론 sklearn에 pipeline과 비슷한 것들이 있기는 한데, 이는 머신러닝을 위한 pipeline을 만드는 형태에 가까워요. 
- 따라서 python에서 composite function을 어떻게 쉽게 만들 수 있는지 한번 만들어 봤습니다. 

```python 
## 우선 function 2개를 입력받아서 composite function을 만들어주는 함수를 정의하고 
def compose2(func1, func2):## func1 first applied
    return lambda x: func2(func1(x))
## 순서대로 적용될 함수리스트 
pipes = [lambda x: x+1, lambda x: x*2, lambda x: x*10]
## reduce를 통해 함수2을 섞어서 새로운 함수를 만드는 일을 반복함
comp_func = functools.reduce(compose2, pipes)
for i, x in enumerate(range(5, 10)):
    print(f"{i}: {comp_func(x)}")
```

```
0: 120
1: 140
2: 160
3: 180
4: 200
```

- `functools.reduce`말고 `itertools.accumulate`를 사용할 수도 있습니다. 
- 최종 값만 알려주는 `functools.reduce`에 비해 `itertools.accumulate`는 중간 값들도 다 알려준다는 차이점이 있죠.  

```python
for i, f in enumerate(itertools.accumulate(pipes, compose2)):
    print(f"{i}: {f(10)}")
```

```
0: 11
1: 22
2: 220
```

## wrap-up

- 별로 어렵지는 않습니다만, 그러니까 그냥 정의를 해주면 좋을 것 같네요. 
- 저는 이미 reduce 가 python2에서 python3로 넘어오면서 제외된 것도 마음에 들지 않아요 흠. 생각난 김에 왜 빠지게 되었는지 그 원인도 좀 정리를 해보면 좋을 것 같은데, 그 부분은 제가 나중에 한 번 찾아보겠습니다. 