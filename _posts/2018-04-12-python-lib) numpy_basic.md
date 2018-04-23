---
title: python - numpy
category: python-lib
tags: python python-lib numpy 

---


- 아주 간단한 numpy 활용법을 정리했습니다. 

### intro

- NumPy is the fundamental package for scientific computing with Python. It contains among other things
- numpy없이 간단한 matrix연산하다가 빡쳐서 정리해봄.
- numpy는 전반적으로 우리가 matlab에서 썼던 문법과 유사하게 사용됨

### why 갑자기 numpy start요?

- 사실 다음의 문제 때문에, 시작함.
- 두 list에 대해서 a+b를 하고 싶은데(matrix, vector처럼) 저걸 하려면 좀 번거롭게 function을 새로 만들어야 한다는 사실이 화가 났음
- list에 대해서 더하면, concatenation


```python
a = [1,2,3]
b = [4,5,6]
print(a+b)# sad
```

    [1, 2, 3, 4, 5, 6]


- 그래서 matrix 연산을 지원하는 것이 없나 보니까 numpy가 있음. 넘나 좋은 것
    - list 를 np.array로 변환하는 것이 너무 쉬움 핱핱
    - 내부 변수로는 ndim, shape등이 있으나, 뭐 별로 중요하지 않음.
        - ndim: 쉽게 말해, 괄호의 갯수
        - shape: 모양, 디멘션별 크기


```python
import numpy as np

a = [1,2,3]
b = [4,5,6]
print("list:", a+b)
a = np.array(a)
b = np.array(b)
print("np.array:", a+b)#good
c = [[[1,2,3], [4,5,6]]]
c = np.array(c)
print("ndim:{}, shape:{}".format(c.ndim, c.shape))
```

    list: [1, 2, 3, 4, 5, 6]
    np.array: [5 7 9]
    ndim:3, shape:(1, 2, 3)


- np.array는 n-dim인데, matrix는 2-dim이 끝.
- np.array가 np.matrix보다 제네릭하므로, 앞으로는, matrix는 따돌림을 시키도록 한다!!
    - matrix야 너도 어떤 평행우주에서는 쓸모가 있을거야 힘내, 내가 공부를 더 해서 니가 필요한 날이 생기면 다시 올게 앙냥


```python
a = np.matrix([[[1,2,3,4]]])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-352-a3049ecc4fe2> in <module>()
    ----> 1 a = np.matrix([[[1,2,3,4]]])


    C:\Users\frhyme\Anaconda3\lib\site-packages\numpy\matrixlib\defmatrix.py in __new__(subtype, data, dtype, copy)
        272         shape = arr.shape
        273         if (ndim > 2):
    --> 274             raise ValueError("matrix must be 2-dimensional")
        275         elif ndim == 0:
        276             shape = (1, 1)


    ValueError: matrix must be 2-dimensional


### operation:
- +, -, \*, / 는 같은 사이즈의 `np.array`에 대해서만 가능
- `np.dot`이 우리가 흔히 말하는 matrix 곱셈.
- `.T` method는 transpose, `np.transpose` 도 가능


```python
l1 = [[1,2,3], [4,5,6]]
a1 = np.array(l1)
print("a1+a1:\n", a1+a1)
print("a1-a1:\n", a1-a1)
print("a1*a1:\n", a1*a1)
print("a1/a1:\n", a1/a1)
print("np.multiply(a1, a1)\n", np.multiply(a1, a1))
print("np.dot(a1, a1)\n", np.dot(a1, a1.T))
print("np.dot(a1, a1)\n", np.dot(a1.T, a1))
```

    a1+a1:
     [[ 2  4  6]
     [ 8 10 12]]
    a1-a1:
     [[0 0 0]
     [0 0 0]]
    a1*a1:
     [[ 1  4  9]
     [16 25 36]]
    a1/a1:
     [[ 1.  1.  1.]
     [ 1.  1.  1.]]
    np.multiply(a1, a1)
     [[ 1  4  9]
     [16 25 36]]
    np.dot(a1, a1)
     [[14 32]
     [32 77]]
    np.dot(a1, a1)
     [[17 22 27]
     [22 29 36]
     [27 36 45]]


- 행렬 연산을 좀 더 유심히 보자(서로 다른 사이즈일 경우)
    - 내가 원하는 대로 매트릭스 연산이 되지 않는 것을 알 수 있음.
- dot method로 계산해보면 값이 나오기는 함.
    - 다만, a의 각 row가 b(3 by 1)와 곱해져서 3 by 1의 매트릭스가 나와야 하는데 그렇게 안됨.
    - ndim=1인 np.array는 transpose해도 안해도 똑같음.


```python
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([1,2,3]).T
print(b)
print("a*b\n", a*b)
print( np.dot(a, b).T )
print(np.dot(a, b)==np.dot(a, b).T)
```

    [1 2 3]
    a*b
     [[ 1  4  9]
     [ 4 10 18]
     [ 7 16 27]]
    [14 32 50]
    [ True  True  True]


- 그리고 생각보다 matrix를 써야 하는 시간이 빨리왔다...
- 매트릭스를 이용하면, 쉽게 아래처럼 계산할 수 있음.. 정확히 내가 원하던 대로.


```python
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([1,2,3])
c = np.matrix(a)*np.matrix(b).T
print(c.shape)
print(c)
```

    (3, 1)
    [[14]
     [32]
     [50]]


- 사실 ndim이 1이 아니면, transpose가 잘 되기 때문에, np.matrix, np.array 모두 문제없이 흘러감


```python
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[1,1,1], [2,2,2]]).T

print(np.dot(a, b))
print(np.matrix(a) * np.matrix(b))
```

    [[ 6 12]
     [15 30]
     [24 48]]
    [[ 6 12]
     [15 30]
     [24 48]]


- computation time에서 np.array가 list보다 훨씬 빠르다는데 정말 그럴까요?
- 실험을 해봅니다.
- 10,000,000 크기의 리스트를 소팅할때 걸리는 시간과, np.array를 소팅하는데 걸리는 시간을 비교합니다.
- 8.6%의 미미한 시간이 감소했습니다. 하하하하


```python
import time
a = list(reversed(range(0, 10000000)))
arr = np.array(a)
ar_t = time.time()
arr.sort()
print(arr[:10])
ar_t = time.time() - ar_t

lst_t = time.time()
a.sort()
print(a[:10])
lst_t = time.time() - lst_t
print("np.array:{}, list:{}".format(ar_t, lst_t))
print( round((lst_t - ar_t)/lst_t*100, 1),"%의 시간 감소" )
```

    [0 1 2 3 4 5 6 7 8 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    np.array:0.21115589141845703, list:0.21898150444030762
    3.6 %의 시간 감소


- np.array에서는 뭐든 때려박을 수 있는 list와 다르게, 모든 원소의 데이터 타입이 동일해야 합니다.
    - 서로 다른 data를 넣으면 하나의 타입으로 통일됨
    - type을 지정해서 넣어줄 수도 있음.


```python
a = np.array([1,2,3,4])
print(a)
print(a.dtype)

a = np.array([1, 2, 3, 4, "b"])
print(a)
print(a.dtype)# string이어야 하는데 뭔가 이상한 타입이 출력되었다.
print( type(a[0]) )# 각 element는 numpy 내의 string으로 출력

l = [1,2,3,4,5]
print( np.array(l, np.int))
print( np.array(l, np.float))
print( np.array(l, np.str))
```

    [1 2 3 4]
    int32
    ['1' '2' '3' '4' 'b']
    <U11
    <class 'numpy.str_'>
    [1 2 3 4 5]
    [ 1.  2.  3.  4.  5.]
    ['1' '2' '3' '4' '5']


- shallow copy를 조심합시다.


```python
a = [[1,2,3], [4,5,6]]
a = np.array(a)
b = a
b[0][1] = 10
print(a)

a = [[1,2,3], [4,5,6]]
a = np.array(a)
b = a.copy()
b[0][1] = 10
print(a)
print(b)
```

    [[ 1 10  3]
     [ 4  5  6]]
    [[1 2 3]
     [4 5 6]]
    [[ 1 10  3]
     [ 4  5  6]]


- 사이즈가 같은 두 벡터를 곱해주는 것이 필요하다!!!
- np.array는 아까의 수모를 갚을 수 있을 것인가!!!
- 1000 사이즈의 두 벡터를 곱해주는 것이 필요함.


```python
k = 1000
l1 = list([1]*size)
l2 = list(range(1, size+1))
a1 = np.array(l1)
a2 = np.array(l2)
# by list
lst_t = time.time()
k = [ x*y for x in l1 for y in l2]
lst_t = time.time() - lst_t

ar_t = time.time()
k = a1*a2
ar_t = time.time() - ar_t

print("np.array에서 {}% 만큼의 시간감속".format(round((lst_t-ar_t)/lst_t*100, 2)))
```

    np.array에서 89.21% 만큼의 시간감속


- pandas 에서의 DataFrame과 유사하게, boolean 으로 index이 가능


```python
a = np.array(list(reversed([[1,2,3], [4,5,6], [7,8,9]])))
b = np.array(([[1,2,3], [4,5,6], [7,8,9]]))
# return boolean array
print( a==b )
print( a[a>3])
print( a[a.nonzero()] )
```

    [[False False False]
     [ True  True  True]
     [False False False]]
    [7 8 9 4 5 6]
    [7 8 9 4 5 6 1 2 3]


Reference

- [python - numpy 선형대수 이해하기 ](https://www.slideshare.net/dahlmoon/numpy-20160519?qid=8abb061c-101c-47cf-866d-dd32b3f83244&v=&b=&from_search=1)
