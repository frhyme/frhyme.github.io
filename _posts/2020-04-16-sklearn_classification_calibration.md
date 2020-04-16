---
title: Python - sklearn - Probability Calibration
category: python-libs
tags: python python-libs sklearn 
---

## Intro

- [이 글](https://machinelearningmastery.com/calibrated-classification-model-in-scikit-learn/)의 내용을 정리하고 번역하였습니다.

## Calibration of Predictions

- 흔히들 Calibration은 "실제 현상에서의 빈도"와 "예측 모델을 통해 예측된 확률값"이 같은 정도를 말한다고 보시면 됩니다.
- (기본적으로는 binary classification 상황에서 보면) 우리는 늘 그냥 "accuracy"만 가지고 해당 모델의 성능을 평가하죠. 가령, "예측한 것 중에서 얼마나 잘 맞았는가?"와 "진짜 인 것들을 얼마나 잘 검증해내는가?"정도로 보통 분류기의 성능을 측정하죠. 뭐, 이게 보통 accuracy, precision, recall, 등이 있고 보통 이 measure만으로도 꽤나 충분하기는 합니다.
- 하지만, 언젠가부터, calibration도 많이 보고 있죠. 이는 "이 모형을 통해 예측하는 probability가 0.8이라면, 실제로 그 값을 가진 대략적인 Y는 80의 확률로 True여야 한다는 것을 말하죠.
- 조금 더 설명해보자면, 가령 우리가 만든 분류 모델 A에서는 확률이 0.1과 0.2사이로 나온 구간을 보면 실제로도 Y가 True인 애들이 10%는 있어야 한다는 이야기죠. 만약, 그렇지 않고, 확률을 매우 낮게 계산했는데, 그 구간에는 훨씬 많은 수가 있다면, 결과적으로 accuracy등이 맞다고 해도, 이 아이는 실제 현상에서의 빈도를 반영하지 못한다는 한계를 가지고 있게 됩니다.

### Reliability Diagrams(Calibration Curves)

- 이를 평가하기 위해서 Reliability Diagram이 있습니다. X축에는 예측된 평균 확률 값을 놓고, Y축에는 실제로 그 확률 구간에 존재하는 True인 아이들의 비율을 놓죠.
- 아래 그림을 보면 더 명확해집니다. 보시면, logistic regression의 경우는 확률 구간에 따라서, 비교적 일정하게 Y가 True인 비율이 증가하죠. 다만, 반대로, Support Vector Classifier의 경우에는 확률이 0.5에 가까운 경우에 True인 애들이 확 증가하게 됩니다.

![sklearn - reliability diagram plot](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_0011.png)

- 즉, chart가 S-Curve를 그리는 경우에는 "그럴법한 경우에는 확 확률이 높아지고, 그렇지 않을 경우에는 확 확률이 떨어진다"라는 것이죠. 만약, 우리가 만든 모델이 이러한 S-Curve를 그린다면, 이 모델의 확률값은 큰 의미가 있다고 보기 어렵습니다. 즉, 여기서 말하는 "의미"라는 것은 "현실에서의 상황을 반영해주지 못한다"라는 이야기죠.

- 이 Reliability Diagram 혹은 Calibration Curve는 `sklearn.calibration.calibration_curve`를 사용해서 가져올 수 있습니다. 예측한 Prediction을 X축에 두고, Y축에는 실제 그 확률 내에 존재하는 실제 Y의 비율을 히스토그램으로 그리는 것을 말하죠. 다시 말하지만, "예측확률과 그 결과가 선형적으로 증가해야, calibrated Model"이라고 할 수 있습니다.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.calibration import calibration_curve

import matplotlib.pyplot as plt


np.random.seed(0)
N_SAMPLES = 10000
X, y = make_classification(
    n_samples=N_SAMPLES, n_features=20, n_informative=2,
    n_classes=2, n_redundant=2, random_state=0)
n_train_samples = N_SAMPLES//10

X_train, y_train = X[:n_train_samples], y[:n_train_samples]
X_test, y_test = X[n_train_samples:], y[n_train_samples:]


clf_dict = {
    'logistic_reg': LogisticRegression(),
    'gaussianNB': GaussianNB(),
    'svc': SVC(probability=True),
    'mlpclassifier': MLPClassifier(hidden_layer_sizes=(100))
}

plt.figure(figsize=(9, 9))
plt.plot([0, 1], [0, 1], '--', color='gray')

for clf_key, clf in clf_dict.items():
    clf.fit(X_train, y_train)
    y_test_positive_predict_proba = clf.predict_proba(X_test)[:, 1]
    # fraction_of_positives: 실제로 양성일 비율
    # - 즉, probability가 낮음에도 실제로 이 값이 positive일 비율
    # mean_predicted_value: 관측된 probability의 평균
    fraction_of_positives, mean_predicted_value = calibration_curve(
        y_test, y_test_positive_predict_proba, n_bins=20)
    plt.plot(
        fraction_of_positives,
        mean_predicted_value,
        'o-',
        label=clf_key)

plt.legend()
plt.savefig("calibration.png", dpi=60)
```

### Probability Calibration

- logistic regression의 경우는 이미 calibrated이다. 몇몇 알고리즘의 경우는, 이미 calibration되어 있지만, neural network, SVM, decision tree와 같은 알고리즘들은 대부분 직접 probability에 대한 예측을 수행하지 않기 때문에, approximation을 통해 probability를 계산한다. 따라서, 이 모델드은 이미 uncalibrate이며, calibration을 사용해서 해당 모델의 확률 값들을 rescaling해주어야 한다.
- Platt Scaling과 Isotonic Regression이라는 두 가지 방법이 있는데, 우선, Platt Scaling은 S-shape의 reliability diagram에 대해서 적합하다.
- Isotonic Regression은 훨씬 복잡하며, 더 많은 데이터를 필요로 하고, 다른 모양의 reliabililty diagram들 특히, monotonic distortion에 대해서 유용하게 사용될 수 있다. 하지만, 동시에, isotonic regression은 overfitting되는 결과를 가져올 수 있으므로, 데이터가 충분하지 못할 경우에는 Platt Scaling보다 더 나쁜 결과를 생성할 수도 있습니다.
- 역시나, 이 방법도 `sklearn.calibration.CalibratedClassifierCV`에서 사용할 수 있습니다만, 모든 경우에 대해서 다 calibration을 잘해주는 것 같지는 않네요.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import calibration_curve
from sklearn.calibration import CalibratedClassifierCV

import matplotlib.pyplot as plt


np.random.seed(0)
N_SAMPLES = 10000
X, y = make_classification(
    n_samples=N_SAMPLES, n_features=20, n_informative=2,
    n_classes=2, n_redundant=2, random_state=0)
n_train_samples = N_SAMPLES//10

X_train, y_train = X[:n_train_samples], y[:n_train_samples]
X_test, y_test = X[n_train_samples:], y[n_train_samples:]

gaussianNB_clf = GaussianNB()

plt.figure(figsize=(12, 9))
plt.plot([0, 1], [0, 1], '--', color='gray')

# uncalibrated
gaussianNB_clf.fit(X_train, y_train)
y_test_positive_predict_proba = gaussianNB_clf.predict_proba(X_test)[:, 1]
fraction_of_positives, mean_predicted_value = calibration_curve(
    y_test, y_test_positive_predict_proba, n_bins=10)
plt.plot(
    fraction_of_positives,
    mean_predicted_value,
    'o-', label='Uncalibrated_clf')

# calibrated
gaussianNB_clf_sigmoid = CalibratedClassifierCV(gaussianNB_clf, cv=2, method='sigmoid')
gaussianNB_clf_sigmoid.fit(X_train, y_train)
prob_pos_sigmoid = gaussianNB_clf_sigmoid.predict_proba(X_test)[:, 1]

fraction_of_positives, mean_predicted_value = calibration_curve(
    y_test, prob_pos_sigmoid, n_bins=10)
plt.plot(
    fraction_of_positives,
    mean_predicted_value,
    'o-', label='Calibrated_clf')


plt.legend()
plt.savefig("calibration_scaling.png", dpi=60)
```

## wrap-up

- 음, 사실 저는 언젠가부터 그냥 classification 문제가 생기면, 본능적으로 `sklearn.neural_network.MLP_classifier`를 사용합니다. 그리고 그냥 accuracy만을 사용해서 처리해버렸죠. 그리고, `.pred_proba`를 통해 계산하는 확률 값이 실제 확률이 아니라, 추정 값이라는 것도 이번에 알았네요.
- 앞으로는 모델을 만든 다음에, 이 모델의 calibration curve를 가능한 그려보고 그다음에 검증해보는 습관이 필요할 것 같습니다.

## reference

- [machinelearningmastery - calibrated-classification-model-in-scikit-learn](https://machinelearningmastery.com/calibrated-classification-model-in-scikit-learn/)
- [kaggle - notes on classification probability calibration](https://www.kaggle.com/residentmario/notes-on-classification-probability-calibration)
- [논문리뷰 - 현대 딥러닝의 Calibration 에 대하여](https://3months.tistory.com/490)
