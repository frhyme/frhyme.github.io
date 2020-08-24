---
title: python lib) numpy 기본적인 사용법
category: python-lib
tags: python python-lib numpy 
---

### intro - 아주 간단한 numpy 활용법

- NumPy is the fundamental package for scientific computing with Python. It contains among other things
- numpy없이 간단한 matrix연산하다가 빡쳐서 정리해봤씁니다. 
- 사실 numpy는 전반적으로 과거에 제가 matlab에서 사용했던 문법과 매우 유사하죠.

## 왜 갑자기 numpy를 정리하나요?

- 사실 두 list에 A, B에 대해서, element-wise 연산을 해주고 싶은데, 이 간단한 걸 하려면, 새로운 function을 만들어줘야 하더군요. 따라서, 이걸 그냥 numpy를 사용해서 변경해서 쓰면 될것 같았고 이참에 정리해봤습니다.
- 두 list는 서로 연산하면 concatenation이 되죠.

```python
a = [1,2,3]
b = [4,5,6]
print(a+b)# sad, [1, 2, 3, 4, 5, 6]
```

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

```plaintext
list: [1, 2, 3, 4, 5, 6]
np.array: [5 7 9]
ndim:3, shape:(1, 2, 3)
```

- np.array는 n-dim인데, matrix는 2-dim이 끝입니다. 아래 코드에서 보는 것처럼, 2-dim이 넘는 차원의 배열에 대해서는 `np.matrix`로 변경하려고 할때 에러가 발생하죠.
- 즉, 앞으론느 그냥 `np.matrix`는 없다고 생각하고, `np.array`를 기본으로 생각하고 프로그래밍을 하는 것이 훨씬 효과적이라고 생각되네요.

```python
a = np.matrix([[[1,2,3,4]]])
```

```plaintext
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
```
    
### numpy operation

- 같은 size의 `np.array`에 대해서 기본적인 연산자들인 +, -, \*, /의 경우는 element-wise operation으로 작동합니다.

```python
a1 = np.array([[1, 2, 3], [4, 5, 6]])
print("a1+a1:\n", a1 + a1)  # element-wise add
print("--" * 10)
print("a1-a1:\n", a1 - a1)  # element-wise substraction
print("--" * 10)
print("a1*a1:\n", a1 * a1)  # element-wise multi
print("--" * 10)
print("a1/a1:\n", a1 / a1) # element-wise div
print("--" * 10)
```

- `.multiply`의 경우도 element-wise multiplication으로 작동하죠.
- 그리고, `np.dot`이 우리가 흔히 말하는 matrix간의 연산을 의미합니다.

```python
print("np.multiply(a1, a1)\n", np.multiply(a1, a1))
print("np.dot(a1, a1)\n", np.dot(a1, a1.T))
print("np.dot(a1, a1)\n", np.dot(a1.T, a1))
```

- 정확히 해야 하는 것은 `np.matrix`와 `np.array`가 서로 다르다는 것이죠. `np.matrix`는 * 연산을 했을 때 알아서 `.dot`으로 처리해주지만, np.array는 그렇지 않고 element-wise로 각각 곱셈을 해줄 수 있습니다.
- 따라서, 내가 곱셈을 하려는 것인지, 행렬간의 곱연산을 해주려는 것인지를 명확하게 구분하여 써야 한다는 것을 명심하세요.

## np.array는 list보다 얼마나 더 빠른가? 

- 계산 시간으로 비교해볼 때, `np.array`가 `list`보다 더 빠르다는데, 정말 그런지 실험을 해보겠습니다.
- 10,000,000 크기의 리스트를 소팅할때 걸리는 시간과, np.array를 소팅하는데 걸리는 시간을 비교해봤지만, 고작 8.6%의 시간만이 감소할 뿐이군요. 물론, 이건 단지 시간만의 비교라서 그런 것일테고, 메모리 측면에서 보면 `np.array`가 더 효율적일 겁니다(아마도)

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

```plaintext
[0 1 2 3 4 5 6 7 8 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
np.array:0.21115589141845703, list:0.21898150444030762
3.6 %의 시간 감소
```
    
- 또한, 서로 다른 데이터 타입들도 마구 때려 박을 수 있는 list와 다르게 `np.array`는 모든 원소의 데이터 타입이 동일해야 합니다. type을 미리 지정해서 넣을 수도 있고, 혹은 data를 넣으면 알아서 추론해서 설정해주기도 하죠.

```python
a = np.array([1,2,3,4])
print(a) # [1 2 3 4]
print(a.dtype) # int32

a = np.array([1, 2, 3, 4, "b"])
print(a) # ['1' '2' '3' '4' 'b']
print(a.dtype) # <U11, string이어야 하는데 뭔가 이상한 타입이 출력되었다.
print( type(a[0]) )# <class 'numpy.str_'>, 각 element는 numpy 내의 string으로 출력

l = [1,2,3,4,5]
print( np.array(l, np.int)), # [1 2 3 4 5]
print( np.array(l, np.float)) # [ 1.  2.  3.  4.  5.]
print( np.array(l, np.str)) # ['1' '2' '3' '4' '5']
```

## shallow vs deep copy

- python에서 대부분 그렇지만, 그냥 `=`를 사용하는 경우 shallow copy가 일어납니다. 복제된 것처럼 보여도 하나의 같은 값을 공유하게 되는 것이죠. 
- 따라서, 만약 복사하고싶다면, `.copy()`를 상요해서 deep copy를 해줘야 합니다.

```python
import numpy as np 

a = [[1, 2, 3], [4, 5, 6]]
a = np.array(a)
b = a  # =의 경우 shallow copy
b[0][1] = 10
print(a)
print(b)
print("========")
a = [[1, 2, 3], [4, 5, 6]]
a = np.array(a)
b = a.copy()  # .copy()를 사용해야 deep copy
b[0][1] = 10
print(a)
print(b)
```

```plaintext
[[ 1 10  3]
 [ 4  5  6]]
[[ 1 10  3]
 [ 4  5  6]]
========
[[1 2 3]
 [4 5 6]]
[[ 1 10  3]
 [ 4  5  6]]
```

- 만약 사이즈가 같은 두 벡터를 element-wise multiplcation으로 곱해주려고 한다고 해보겠습니다. 하나는 그냥 list에 대해서 순차적으로 해준다고 하고, 다른 하나는 그냥 `np.array`의 `*` 연산자를 그대로 이요한다고 해보겠습니다.
- 결과를 보면, `np.array`에서 89.21% 만큼의 시간감속이 일어납니다.

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

- pandas 에서의 DataFrame과 유사하게, boolean 으로 index이 가능

```python
a = np.array(list(reversed([[1,2,3], [4,5,6], [7,8,9]])))
b = np.array(([[1,2,3], [4,5,6], [7,8,9]]))
# return boolean array
print( a==b )
print( a[a>3])
print( a[a.nonzero()] )
```

```plaintext
[[False False False]
[ True  True  True]
[False False False]]
[7 8 9 4 5 6]
[7 8 9 4 5 6 1 2 3]
```
    
## Reference

- [python - numpy 선형대수 이해하기](https://www.slideshare.net/dahlmoon/numpy-20160519?qid=8abb061c-101c-47cf-866d-dd32b3f83244&v=&b=&from_search=1)
