---
title: digitsProduct(product)
category: algorithm 
tags: python algorithm codefight dictionary list

---

## Problem

- 특정한 수 `product`가 들어왔을 때, `product`의 인수 들을 조합해 만들 수 있는 가장 작은 수를 찾는 함수입니다. 
- 이 문제는 약간 이해가 어려울 수 있어서, 예를 중심으로 설명합니다. 

### examples

1. digitsProduct(2) ==> 2
	- 2의 경우, 한자리수로 표현할 수 있기 때문에 그대로 2로 표현
2. digitsProduct(16) ==> 28
	- 16의 경우, 2`*`8, 4`*`4, 등이 존재하는데, 이를 활용해 28, 44, 82 등을 만들 수 있다. 
	- 이중에서 가장 작은 수가 바로 28
3. digitsProduct(36) ==> 49
	- 마찬가지로, 4`*`9 가 존재하며, 49가 가장 작은 값
4. digitsProduct(13) ==> -1
	- 13의 경우 인수에 두 자리수 이상의 값인 13이 존재한다. 
	- 이 경우에는 -1을 리턴한다. 

## solution

- 우선 `n`에 존재하는 모든 인수와 그 갯수를 딕셔너리로 만들어주는 함수(`DestructNum`)를 정의한다. 
	- 이 결과로 나오는 딕셔너리의 키 값은 2,3,5,7 뿐이며, 그 이상일 경우에는 -1을 리턴해주면 된다. 
- `ExistPlus_Non1` 함수의 경우는 딕셔너리에 대해서 defaultdict의 역할을 비슷하게 한다. 
		- 키 값이 이미 존재하면 +1, 없으면 1을 세팅해야 하는 경우가 아주 많은데, 파이썬에서는 이 부분이 종종 불편함.
		- 또한, 파이썬으로 코딩할 때는 함수에서 리턴하는 경우가 많은데, dictionary, list는 다른 함수에서 argument로 읽어들일 때, `call by reference`로 진행된다. 따라서 해당 함수에서 굳이 리턴할 필요 없음. 

```python
def ExistPlus_Non1(input_d, k):
    if k in input_d.keys():
        input_d[k]+=1
    else:
        input_d[k]=1

def DestructNum(n):
    if n>=2:
        i=2
        r = {}
        while n>=2:
            if n%i==0:
                ExistPlus_Non1(r, i)
                n=n//i
            else:
                i+=1
        return r
    else:
        return {1:1}
```


- DictToList의 경우 만들어진 딕셔너리를 리스트로 변환해주는 함수다. 
	- {1:2, 3:2} 를 [1,1,3,3]으로 변환해준다. 
- 또한 `IsPrimeAndOver10`의 경우 두자리가 넘는 소수가 있는지를 체크해주는 함수 

```python
def DictToList(input_d):
    r = []
    for k in input_d.keys():
        r+=[k for i in range(0, input_d[k])]
    return r
def IsPrimeAndOver10(n):
    c = 0 
    if n<10:
        return False
    for i in range(2, n):
        if n%i==0:
            c+=1
    return False if c>=1 else True
```

- 이제 나머지는 간단하다. 
- 해당 수에 두자리 이상의 소수가 없고, 존재하는 인수를 리스트로 만든 이후에, 어떻게든 자리수를 줄여야 값이 작아진다. 
	- 따라서, 현재 인수들을 활용해서 9,8,7,6,5,4,3을 순서대로 만들 수 있는지를 확인하고, 자리수를 최대한 줄인다음
	- 해당 값을 역으로 연결하여 합쳐준다. 참 쉽죠?

```python
def digitsProduct(product):
    if product==0:
        return 10
    n_dict = DestructNum(product)
    if any([IsPrimeAndOver10(k) for k in n_dict.keys()]):
        return -1
    else:
        while True:
            if 3 in n_dict.keys() and n_dict[3]>=2:
                n_dict[3]-=2
                ExistPlus_Non1(n_dict, 9)
            else:
                if 2 in n_dict.keys() and n_dict[2]>=3:
                    n_dict[2]-=3
                    ExistPlus_Non1(n_dict, 8)
                else:
                    if 2 in n_dict.keys() and n_dict[2]>=1 and 3 in n_dict.keys() and n_dict[3]>=1:
                        n_dict[2]-=1
                        n_dict[3]-=1
                        ExistPlus_Non1(n_dict, 6)
                    else:
                        if 2 in n_dict.keys() and n_dict[2]>=2:
                            n_dict[2]-=2
                            ExistPlus_Non1(n_dict, 4)
                        else:
                            break
    return int("".join([str(d) for d in sorted(DictToList(n_dict))]))
```

## lesson learned

- 그동안은 왜 때문인지 다른 함수에서 dictionary, list를 argument로 가져올 때 항상 def func(lst): return lst 와 같은 형태로 사용했다. 
	- 물론 pandas 를 쓰다보면 습관이 되기도 하지만.
- 굳이 리턴하지 않아도 된다는 것을 알게 된 것이 나름의 조촐한 수확. 
