---
title: What is eigen vector, value? 
category: python-libs
tags: python python-libs networkx centrality eigenvector linear-algebra
---

## Eigen Value and Vector: 분명히 학부 때 배웠던 것입니다만. 

- 제 기억이 맞다면, 2008년(아 너무 먼 옛날이다)에 학교 "선형 대수학(Linear algebra)"에 분명히 배웠던 기억이 있습니다. 물론 아주 엄청나게 예전이고, 이후에 복습을 하지 않았으니 까먹는건 사실 자명한 일이죠. 그저, "해당 매트릭스의 unique성을 말해주는 것"정도로만 기억하고 있습니다. 나름 공대 박사까지 하고 있는 것인데 이게 다 무슨 짓인지 호호호.
- 요즘에도 딱히 쓸 일이 없기는 해서, 잊어버리고 살다가, 최근에 python library 중 하나인 `networkx`의 centrality 중에서 **eigen vector centrality**를 복습하다가, 생각난 김에 다시 공부해봤습니다. "공대를 나오면 뭐하냐, 이것도 제대로 기억못하면서"라는 말이 머릿 속을 잠시 스치는데, 뻔뻔하게 "공대 나와도 모를 수도 있지!"라는 식으로 응수합니다. 스스로를 아껴줘야 해요 호호호. 

## Back to : Eigen value and vectors

- 위키피디아에 정리된 [EigenValue and EigenVector](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)에 따르면,
    - 어떤 square matrix(N by N)인 `T`가 있다고 합시다. 
    - 그리고 `np.dot(T, X) == np.multiply(L, X)`을 만족하는, `X`, `L`이 각각 있다고 합시다. 
    - 이를 만족하는 `X`를 eigen vector, `L`을 eigen value라고 합니다. 
- 이를 해석하자면, `T`가 일종의 rotation matrix라고 할 때, 이걸, `X`라는 매트릭스에 적용해도, unit vector는 바뀌지 않는다는 것을 말하죠. 즉, `T`라는 매트릭스를 아무리 곱해도, unit vector는 그대로 라는 것을 말하죠.
- 그리고, 보통 여기서 `T`가 아닌 `A`를 많이 쓰지만, 굳이 `T`를 쓴 것은, "Linear Transformation"을 표현하기 위함이었습니다. 선형 변환을 적용해도, 달라지지 않는, vector, 그것을 eigen vector라고 합니다.

### its Application, especially in Graphtheory. 

- [wikipedia에 설명된 내용](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)application을 중에서, 재미있는 부분이 좀 있습니다. 하지만, 다 이해하기는 어렵고 그저 "Eigen vector/value"가 각 분야별로 어떤 의미로 쓰이고 있구나, 정도로만 넘어가시면 되요. 제가 관심있어 하는 부분은 Graph에서 eigen value가 중요한 이유를 서술한 부분이고, 대략 다음과 같습니다. 
- spectral graph theory에서 graph의 eigenvalue는 보통 graph의 adjacency matrix의 eigen value로 정의된다. 
    - first eigenvector는 보통 각 node(vertex)의 centrality를 측정하기 위해 사용되는데, 그 중 하나의 예가 바로 Google의 PageRank Algorithm이다. 이 벡터는 row-normalized adjacency matrix의 Markov chain의 stationary distribution과 동일하다(물론, 당연히, 해당 adjacency matrix가 stationary distribution이 존재함을 증명해야 하고)
    - second smallest eigenvector는 graph를 cluster로 나눌 때, 특히, spectral clustering을 통해서 나눌 때 사용된다.
- 왜 graph의 adjacency matrix가 "markov chain의 stationary distribution, 즉 단순하게 말하면 마코브체인을 무한히 반복했을 때 도착하는 분포"를 의미하게 되는가? 는 매우 자연스럽게 나올 수 있는 질문이지만, 이걸 답하기는 매우 어려울 것으로 보입니다. 네, 아마도 이 논문 저논문을 다 뒤져보면 결국 나오게 되겠지만요. 
- 저는, 그냥 외우기로 했습니다. **Graph에서 Adjancecy matrix의 eigen vector는 centrality를 평가하기 위해서 사용된다. 거의 마코브체인과 동일하다**라고요. 물론, 수렴하지 않는 경우들이 있을 수 있습니다만(이것이, 전제조건으로 깔아둔, stationary distribution이 존재해야 한다, 라는 이야기겠죠)


## How to solve it. 

- 실제 코드로 구현해야 한다면 매우 어렵겠지만, 이 아름다운 python은 오늘도 저를 구원해줍니다. [scipy.linalg.eig](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html)를 사용해서 빠르게 구할 수 있죠. 
- 아래처럼 실행하면 끝납니다 호호호호호호.

```python
import scipy.linalg as la

A = np.array([[1, -2], [2, -3]])
eigenVal, eigenVec = la.eig(A)
```

- 조금 더 길게 코멘트와 함께 실행해본 결과는 다음과 같습니다.

```python
import numpy as np

np.random.seed(0)
N = 3
##############################
# A 라는 rectangular(N by N) matrix가 있다고 합시다
A = np.random.normal(0, 3, N**2).reshape(N, N)
A = np.abs(A)
print(f"== A - shape: {A.shape}")
##############################
# 아래의 조건을 만족하는 것을 각각 eigen_value, eigen_vector라고 합니다.
# np.dot(A, eigen_vector) == np.multiply(eigen_value, eigen_vector)
# ----------------------------
# 앞은 전형적인 matrix product, 뒤는 그냥 scalar 곱이죠.
##############################
# scipy.linalg.eig 를 사용하면 구하는 것 자체는 어렵지 않습니다.
import scipy.linalg as la
#A = np.array([[1, -2], [2, -3]])
eigenVal, eigenVec = la.eig(A)
print(f"eigenVal.shape: {eigenVal.shape}")
print(f"eigenVec.shape: {eigenVec.shape}")
print("==")
# LEFT는 dot product, 일반적인 matrix product
LEFT  = np.dot(A, eigenVec)
LEFT = np.round(LEFT, 8)
# RIGHT는 element-wise operation
RIGHT = np.multiply(eigenVal, eigenVec)
RIGHT = np.real(RIGHT) # imaginary 부분이 있을 수 있으므로 변경
RIGHT = np.round(RIGHT, 8)
# 당연하지만, 이렇게 같게 나와야 함.
print(f"LEFT==RIGHT: {np.all(LEFT==RIGHT)}")
```

- 결과는 다음과 같습니다.

```
== A - shape: (3, 3)
eigenVal.shape: (3,)
eigenVec.shape: (3, 3)
==
LEFT==RIGHT: True
```


## wrap-up

- 아주 오랜만에 eigen vector, value를 다시 공부해봤습니다. 초기에 궁금했었던, "이 아이가 왜 마코브체인처럼 수렴하는 역할을 하는 것인가?"에 대한 질문은 답을 가지지 못했지만, 그래도, 어느 정도 개념들을 다시 잡은 것 같기는 합니다. 
- 추가로, 사실 저 간단한 수식도 실제로 풀어내려면 아주 어렵죠. 따라서, exact method보다는 approximation algorithm이 많이 존재합니다. 이후 제가 정리할 [power iteration](https://en.wikipedia.org/wiki/Power_iteration) eigenvalue algorithm에 속합니다. 나중에 정리해볼게요.

## reference

- [Eigenvalues and eigenvectors in Wikipeia](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [데이터사이언스 스쿨 - 고유값 분해](https://datascienceschool.net/view-notebook/7fd58178d9e64be682058db7e024d8b5/)
- [What is the importance of eigenvalues/eigenvectors?](https://math.stackexchange.com/questions/23312/what-is-the-importance-of-eigenvalues-eigenvectors)