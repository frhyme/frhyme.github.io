---
title:
category:
tags:

---

## bayesian??? 

- 네 저는 베이지안을 늘 헷갈립니다. 제 기억이 맞다면, 대학원 면접에서도 베이지안을 물어봤던 기억이 있는데, 그때도 헷갈렷던 것 같아요. 저는 공대생이 맞나요...유사공대생입니다...흑흑
- 아무튼 세상을 빈도주의적 관점으로 본다는 '빈도주의적 관점'이 있고, 세상을 베이지안관점으로 보는 '베이지안적 관점'이 있습니다. 고 합니다. 이 둘에 대한 비교라면, 
    - 빈도주의적 세계에서는: 가능한 sample space를 확정한 상태에서, 예를 들어, 동전을 던졌을 때의 sample space는 (앞, 뒤)이고, 각각의 확률은 (0.5, 0.5)입니다. 여기서 확률이라는 것은 '빈도' 즉 100번을 던지면 각각 50번씩의 빈도가 나올 것으로 예측된다는 이야기죠. 
    - 베이지안적 세계에서는: 이것은 확률이 아니라, '신뢰도'를 말합니다. '현재 우리가 가지고 있는 정보'에서 앞면과 뒷면이 나올 확률은 각각 (0.5, 0.5)라는 것이죠. 만약 새로운 사건(예: 동전이 약간 구부러져 있다)이 발생했다면, 이를 활용해서 확률(신뢰도)을 업데이트할 수 있습니다. 이렇게 세계를 모델링하고 지속적으로 업데이트하는 세계를 베이지안적 세계라고 할 수 있겠네요. 
- 무엇보다 중요한 것은, 베이지안이라는 것은 **'새로운 증거, 근거가 생겨날 때마다 확률을 업데이트하면서 신뢰도를 높인다'**라고도 말할 수 있을 것 같아요. 그래서, 베이지안을 공부하면 계속 조건부확률이 나오게 되는 것이구요. 
    - 예를 들어서, 야구에 적용을 해본다면 원래 우리가 가지고 있던 지식이 "현재 타석에 있는 타자가 안타를 칠 확률은 0.3"이다 라면, 베이지안에서는 이 말이 "타자가 안타를 친다"라는 말에 대한 신뢰도가 0.3이 되는 것이죠. 만약 그 상황에서 새로운 이벤트가 발생하여 추가로 정보를 획득했다면(예를 들어서, 투수가 바뀌었거나, 볼카운트가 바뀌었거나), 그 정보에 맞춰서 현재 명제의 신뢰도를 업데이트해야 합니다. 
    - 이런 방식으로 새로운 정보가 업데이트 되면서 현재 정보의 상태를 지속적으로 업데이트해나가는 것. 그것을 베이지안 네트워크(혹은 베이지안 모델)이라고 합니다. 

## bayesian model 

- **Bayesian Models**: A Bayesian Model consists of a directed graph and Conditional Probability Distributions(CPDs) associated with each of the node. Each CPD is of the form P(node|parents(node)) where parents(node) are the parents of the node in the graph structure.
- 한국말로 편하게 정리하자면, 조건부 확률분포와 directed graph를 이용한 확률 예측 모형이다, 라고 말할 수 있겠네요. 아마도. 

## 잘 이해했나 모르겠지만 일단은......

- 아무튼 간에, 과거에는 Bayesian 네트워크를 공부하는 사람들이 많았고, `sklearn`같은데에도 아직 naive bayesian 을 이용해서 classfication할 수 있긴 합니다(저는 그냥 random forest 사용합니다)

## reference

- <https://datascienceschool.net/view-notebook/9605664e26a0411b88f60e4ba9521dd9/>
- <https://datascienceschool.net/view-notebook/f68d16df9ea448689ae66dc2140fe673/>
- <https://datascienceschool.net/view-notebook/165cbb986f2c443ba7bac9ec83659b46/>
- <https://nbviewer.jupyter.org/github/pgmpy/pgmpy_notebook/blob/master/notebooks/1.%20Introduction%20to%20Probabilistic%20Graphical%20Models.ipynb>
- <https://github.com/markdregan/Bayesian-Modelling-in-Python>
- <https://github.com/pymc-devs/pymc3>