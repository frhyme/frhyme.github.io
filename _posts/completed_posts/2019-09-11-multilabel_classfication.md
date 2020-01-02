---
title: multi-label classification 
category: python-libs
tags: python python-libs multi-label-casslfication classification 
---

## text가 어떤 분류에 속하는지를 분류합시다.

- 저는 요즘 간단히, 자연어 데이터가 어떤 분류에 속하는지를 예측하는 알고리즘을 구현하고 있습니다. 
- 비슷한 예를 든다면, 인스타그램과 같은 서비스에 올라오는 글이 있고 각 글에 달리는 tag가 있다고 하면 글이 input이 되고, tag가 output이 되죠. 즉, 글을 넣어주면 자동으로 적합한 태그를 매칭해주는 알고리즘을 구현하고 있습니다. 


## multi-label classification 

- [sklearn_multi_class](https://scikit-learn.org/stable/modules/multiclass.html)을 확인해보면, multi-class 분류법을 다음과 같은 4가지로 분류하고 있습니다. 물론, 이런 분류를 외우는 것도 의미가 없지만, 각각이 구현하고 있는 것이 조금씩 다르므로 이렇게 분류되는구나, 정도로만 알고가면 될것 같아요.
- **multi class classification**
    - 그냥 classification이라고 하면 보통 binary classification에 속함. 그러나, True or False가 아니라 여러 output class중에서 어떤 output class에 속하는지, 그리고, 반드시 하나의 class에만 속하는 경우를 말한다(예를 들어, 과일이 하나만 찍혀 있는 사진이 있는데 이 과일이 사과이면서, 배일 수는 없다, 물론 교배종이 나타난다면! 과 같은 경우들이 있지만 제외하도록 한다)
- **multi label classification**
    - class가 아니라 label임. label은 multi-class와 다르게, output class가 배반적이지 않음. 보통 문서를 분류한다고 할때, 각 문서는 여러 종류의 특성을 동시에 가지고 있을 수 있음.
- **multi output regressionn**
    - 이건 이번에 처음 알게 된 건데, 아, 그냥 y에 속하는 값이 1개가 아닐때를 의미하는 것 같음. 예를 들어서, "태풍이 어느 정도의 강수량과 풍속으로 온다"를 예측하려고 할때, 강수량이 y1, 풍속이 y2가 될 것이다. 즉, 이러한 방식으로 y 자체가 여러 값으로 섞여 있을때, 이를 multi-output regression문제라고 함. 
- **multioutput-multiclass classification**
    - 이 문제는 앞서 말한 분류기들의 일반화버전이라고 볼 수 있으며, input, ouput이 모두 그 크기의 array로 들어옴으로써 그 값을 처리하고 출려해주는 형식이라고 생각하면 된다.

## how to use it 

- sklearn 문서 상에서 multi-label, mult-class가 각각 구분되어 있지는 않다. 예를 들어서, `sklearn.multi_label.~~`와 같은 식으로 구분되어 있지 않다는 이야기인데, 이걸 좀 더 꼼꼼히 보면, 그냥 output만 다르게 넘겨주면 된다는 것으로 해석된다. 
- 뭔가 이상한데, [이 문서](https://scikit-learn.org/stable/modules/multiclass.html)를 꼼꼼히 읽어보면 결국 다음으로 요약된다. 

- 기본적으로 sklearn의 분류기는 모두 binary classifier를 기본으로 고려함. 
- 그러나, 필요에 따라서, multi-label을 지원하는 경우들이 있으며, 다음의 분류기들이 multi-label을 지원함. 
- Support multilabel:
    - sklearn.tree.DecisionTreeClassifier
    - sklearn.tree.ExtraTreeClassifier
    - sklearn.ensemble.ExtraTreesClassifier
    - sklearn.neighbors.KNeighborsClassifier
    - sklearn.neural_network.MLPClassifier
    - sklearn.neighbors.RadiusNeighborsClassifier
    - sklearn.ensemble.RandomForestClassifier
    - sklearn.linear_model.RidgeClassifierCV
- multilabel을 지원한다는 이야기는, 그냥 X, Y를 각각 알아서 넣어줘도 돌아간다는 이야기인데, 대략 다음과 같다고 말할 수 있음, 그냥 X, Y만 각자 각 feature가 다른 칼럼에 존재하도록 만들어놓고 집어넣으면 됨. 

```python
X = [
    [0, 1, 1], 
    [1, 1, 0]
]
Y = [
    [0, 1], 
    [1, 1]
]
MLPClassifier.fit(X, Y)
```

- 사실은, 그냥 이렇게만 알아도 큰 문제는 없지만, 필요에 따라서, 이렇게 multi-label을 지원하지 않는 classifier를 써야 할 때가 있음. 그럴때는 아래처럼, `OneVsRestClassifer`와 같은 multiclass classifer에 `SVC`같은 binary classifier를 먹여서, 사용해야 합니다. 
    - 물론, 언제나 그렇듯이, MLPClassifier를 사용하는 것이 더 좋습니다. 얘네가 훨씬 웨만하면 잘 돌아가요. 

```python
from sklearn.multiclass import OneVsRestClassifier
clf = OneVsRestClassifier(SVC())
```

## MultiLabelBinarizer

- 자, 우리한테는 태그 리스트만 있다고 해봅시다. 이 때, 각 태그를 칼럼으로 넣고, 1, 0으로 변환해야지 나중에 학습을 시킬 수가 있겠죠. 
- 아래를 사용해서 하면 됩니다.

```python
Y_mlb = MultiLabelBinarizer()
Y_true = Y_mlb.fit_transform(Y_true_kwds)
kwd_classes = Y_mlb.classes_ # binarizer를 저장해두고, 이후에 classes_ 를 읽어서, 각 칼럼이 무슨 값인지를 확인해야 함.

```


## evaluation: metric 

- multi-label algorithm의 경우 잘 되는 것인지 무엇으로 평가할 수 있을까? 
- 그냥 hamming_loss와, jaccard_similarity_score로 계산하면 될것 같습니다.



## wrap-up

- 어차피, 뭐 분류하다보면 `MLPclassifier`를 많이 쓰게 됩니다. 이게 오버피팅의 문제가 좀 있기는 해도, 웬만하면 잘 맞춰주니까요. 
- 아무튼 multi-label classification을 사용하는 방법을 요약하면 다음과 같습니다. 
    - set X, Y: 늘 그렇듯, 우선 무엇으로 무엇을 예측할지를 정리해야 합니다. 
        - set X: 텍스트라면, TfIDF로 feature를 뽑아낼지, Doc2vec으로 뽑아낼지 정해서 각 문서별로 feature를 정리합니다. 
        - set Y: multi-class라면 one-hot vector로 정리하고, multi-label이라면 각 label이 속하는지 속하지 않는지가 각 칼럼에 담기도록 변환합니다. 이는 `MultiLabelBinarizer`로 처리할 수 있습니다. 
    - classifier: 자 이제, 무엇으로 학습시킬 것인지를 정리해야 합니다. 
        - 기본적으로 multi-label을 지원하는 분류기의 경우는 저 X, Y를 그대로 넣으면 되고, 그렇지 않을 경우에는 One vs. Rest or One vs. One 중에 무엇으로 할지를 정래서 진행해야 합니다. 
        - 하지만, 일반적으로는 그냥 randomforest, mlpclassifier 를 쓰는 것이 좋습니다. 
        - 물론 오버피팅이 되지는 않는지 확인해보고 진행하도록 하죠.
    - evaluation: classifier를 평가합니다. 
        - 보통 sparse한 multi-classification에서는 jaccard-similarity score를 쓰는 것처럼 여기서도 jaccard score를 쓰기도 합니다. 
        - 또, hamming loss를 쓰기도 하는데, 귀찮아서 그냥 저는 jaccard를 쓸게요 하하하하하하
- 뭐, 대충 이렇습니다. 사실 정확하게 하려면 좀 꼼꼼하게 해야 하는데 저는 좀 귀찮아서 적-당, 적-당히 합니다하하하
- 요즘은 사실 좀 사는게 급해서 대충대충 쓰게되는 경향성이 있네요 호호호 나중에 다시 더 정확하게 해야하면 그때 다시 좀 더 정리해보겠습니다.