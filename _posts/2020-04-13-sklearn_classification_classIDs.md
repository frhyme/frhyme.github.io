---
title: Python - sklearn - class ID는 그냥 서로 다르기만 하면 되나? 
category: python-libs
tags: python python-libs sklearn 
---

## Intro

- 사실 사소한 질문입니다. classification 문제를 풀 때, Data Y에 대해서 class Label을 지정해주죠. 
- 즉, 만약 우리의 `Y`의 데이터가 다음과 같다면, 우리는 10개의 sample을 가지고 있으며, 0 아니면 1로 서로 다르다는 것을 정의해준 것이죠.

```bash
[0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
```

- 그리고, 위처럼 0부터 순서대로 증강하는 식으로 class를 지정해준 것이 아니라, 아래처럼 음수, 혹은 정수 상에서는 큰 값의 차이가 나는 등 다름이 있어도, 문제없이 학습이 될까요?
- 네 사실 문제없이 학습됩니다. 사실 생각해보면 이를 결국 one-hot enconding으로 처리하기 때문에, 그냥 아무 문제없는 것이죠.

```bash
[1, 2, 1, 1, 2, 2, 1, 2, 2, 1]
[-10, -9, -10, -10, -9, -9, -10, -9, -9, -10]
[-30, 1, -30, -30, 1, 1, -30, 1, 1, -30]
```

## 실제로 해봅니다

- 사실 당연하지만, 저는 똥인지 된장인지 직접 찍어서 먹어 보는 종류의 사람이므로 직접 해봅니다. 아래와 같이, 간단하게 직접 해봤고 그 결과는 다음과 같습니다.

```python
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

X, Y = make_classification(
    n_samples=100,
    n_features=10,
    n_classes=3,
    n_informative=4,
    random_state=1)

# Y ==> 0, 1, 2
Classifier_A = MLPClassifier(random_state=0)
Classifier_A.fit(X, Y)
print("== Y ==> 0, 1, 2")
print(Classifier_A.predict(X)[:10])

# Y_diff ==> -8, -9, -10
Y_diff = np.array([y-10 for y in Y])
Classifier_A = MLPClassifier(random_state=0)
Classifier_A.fit(X, Y_diff)
print("== Y_diff ==> -8, -9, -10")
print(Classifier_A.predict(X)[:10])

# Y_diff2 ==> 1, 2, 9
Y_diff2 = np.array([y if y!=0 else 9 for y in Y])
Classifier_A = MLPClassifier(random_state=0)
Classifier_A.fit(X, Y_diff2)
print("== Y_diff2 ==> 1, 2, 9")
print(Classifier_A.predict(X)[:10])
```

```bash
== Y ==> 0, 1, 2
[2 1 0 2 0 0 1 2 0 0]

== Y_diff ==> -8, -9, -10
[ -8  -9 -10  -8 -10 -10  -9  -8 -10 -10]

== Y_diff2 ==> 1, 2, 9
[2 1 9 2 9 9 1 2 9 9]
```
