---
title: sklearn - semi supervised learning
category: python-libs
tags: python python-libs sklearn semi-supervised-learning machine-learning
---

## Intro: What is semi-supervised learning 

- [semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning)은 "비교적 적은 양의 label data로부터, labeling되어 있지 않은 unlabeld data에 대해서 label을 붙이는 작업"을 말합니다. 이 아이의 이름이 'semi-supervised learning'인 것은, labeled data에게는 supervised learning을 하고, unlabeled data에게는 unsupervised learning을 하기 때문이죠.

## semi-supervised learning in sklearn

- python의 머신러닝 라이브러리인 `sklearn`에는 `LabelPropagation`, `LabelSpreading`라는 두 가지 기법이 있습니다. 
- 이 둘의 차이는, `LabelSpreading`의 경우 regularization 성질을 가진 loss function을 사용함으로써, 좀더 generalization적인 성직을 가지고 있다는 것(정확히는, noise-robust)이 차이이고, 나머지는 큰 차이가 없다, 라고 일단은 생각해도 됩니다. 
- 또한, 보통 clamping factor(alpha)에 따라서 각 모델별로 조금씩 조정을 하는데, 이 값, 즉 `alpha`가 0이라면, 기존의 label distribution을 매우 철저하게 적용한다, 라는 것을 의미하며, 0.2라면 약 20%만 적용한다, 라고 생각하시면 됩니다.
- 원래는 둘다 간단하게 사용해보려고 했지만, 귀찮으므로 `LabelSpreading`만 사용해 봅니다.

### Use Case of LabelSpreading

- 해당 내용은 기본적으로, [sklearn - label propagation digits](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#sphx-glr-auto-examples-semi-supervised-plot-label-propagation-digits-py)에서 가져왔습니다. 흥미롭게도, URL에는 label propagation이라고 적혀 있지만, 실제로는 LabelSpreading을 사용합니다. 
- 아무튼 대부분의 sklearn function들이 그렇듯이, `fit`, `predict`인 건 동일합니다. 다만, semi-supervised learning의 경우 training data가 충분하지 않으므로, 없는 경우는 그냥 `-1`을 넣어서 학습시킵니다. 그럼 끝나요. 

```python
from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading

"""
X: 1797 by 64의 np.array 
- 즉, img의 각 matrix를 reshape한 것이라고 보면 도니다.
Y: X의 True Label
img: 1797 by 8 by 8 의 np.array 
- 8 by 8 크기의 image가 1797개 있음. 
"""
digits = datasets.load_digits()
X = digits.data
Y_True = digits.target
img = digits.images


# digit는 0, 1, 2, 의 순서로 데이터가 존재함. 
# 따라서 random으로 데이터를 가져오는 것이 좋지만, 귀찮으므로 그냥 10개씩 끊어서 가져옴
# 그럼 나름 균등하겠지. 
print(f"Sample Size: {len(X)}")
# True_Label_N까지만 True label이고 나머지는 모두 -1로 세팅함. 
True_Label_N = 10
Y_Train = Y_True.copy()
Y_Train[True_Label_N:] = -1


# Trains Start
LabelSpreadingModel = LabelSpreading(gamma=0.25, max_iter=200)
LabelSpreadingModel.fit(X, Y_Train)
Y_Pred = LabelSpreadingModel.predict(X)
print("== Y_True")
print(Y_True[:30])
print("== Y_Pred")
print(Y_Pred[:30])
```

```
Sample Size: 1797
== Y_True
[0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9]
== Y_Pred
[0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 6 6 7 8 5 0 1 2 3 4 6 6 7 8 5]
```

## wrap-up

- 원래는 좀 더 자세하게, parameter에 따른 차이 등도 민감하게 보려고 했지만, 안타깝게도, [sklearn documentation page](http://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html)가 유지 보수 문제로 접근이 안되는 상황입니다. 그래서 그냥 이렇게만 정리하고 넘어가기로 합니다 호호.


## reference

- [sklearn - label propagation](https://scikit-learn.org/stable/modules/label_propagation.html)
- [semi-supervised learning in wikipedia](https://en.wikipedia.org/wiki/Semi-supervised_learning)