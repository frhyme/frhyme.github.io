---
title: What is "Data Separation"? 
category: others
tags: classification 
---

## Intro 

- 일반적으로 "Data Separation"이라고 하면, 클라우드 컴퓨팅 분야에서 말하는 "데이터 분리"를 떠올립니다. 가령 [Link: What is data separation and why is it important in the cloud?](https://searchcloudcomputing.techtarget.com/answer/What-is-data-separation-and-why-is-it-important-in-the-cloud)에서 보는 것처럼 데이터의 보안을 위해서 데이터 자체를 서로 다른 서버에 나누어 관리하도록 하는 것이 좀 더 친숙한 종류의 Data Separation이죠.
- 다만, classification 혹은 logistic regression에서 말하는 data sepearation은 조금 다릅니다. 
- 관련된 포스트가 많지 않은데, [statisticssolutions - data separation](https://www.statisticssolutions.com/data-separation/)의 내용을 초월번역해서 정리해보겠습니다.

## What is "Data Separation"?

- 간단히 말하자면 "Data Separation"은 말 그대로 "데이터 분리"를 말하며, 가령  Binay classification 에서 outcome이 1인 경우의 관측들과, outcome이 0인 경우의 관측들이 완전히 구분되어 존재한다는 것이죠. 
- 이를 다르게 말한다면, logistic regression을 fitting하는 과정에서 발생하는 문제로, "Y가 1인 그룹의 X 값들은 Y가 0인 그룹의 X 값들에서 전혀 나타나지 않음"을 말합니다. 
- 이렇게 된다면, Y가 0인 X데이터와, Y가 1인 X데이터는 완벽히 구분되어 학습되게 되고, 이 경우 학습 자체가 불가능해지죠. 이러한 종류, 두 데이터 간의 접점이 없는 경우를 **Data Separation**이라고 말합니다.
- 당연하지만, "특정한 predictor를 가진 모든 관측(observations)이 동일한 outcome을 가지는 경우"는 보통, 데이터 자체가 매우 작을 때, 발생합니다. 더불어, outcome의 종류도 binary인 경우처럼 적다면 더 명확하죠.
- 참고한 링크에서는, Age, Exercise를 X로 두고, High Blood Pressure를 Y로 두고 모델을 피팅하려고합니다. "High Blood Pressure"는 Yes, No 두 값만을 가지므로 Binary classification 모델을 만드는 것이죠. 
- 다만, 이때, 데이터의 수가 적어서, High Blood Pressure가 No인 observation의 경우는 모두 동일한 X를 가지고 있습니다. Age도 동일하고, Exercise도 동일하죠. 그리고, High Blood Pressure가 No인 Observation의 어떤 값도 High Blood Pressure가 Yes인 집단에서 보이지 않습니다
- 당연히, 이러한 종류의 "데이터 분리"는 데이터 자체가 적을 때 발생하게 되겠죠.
  
## Is the model Perfectly fitting? 

- 어쩌면, **"어, 100% 로 fitting된 모델이다"**라고 생각하실 수도 있습니다만, 세상에 그렇게 똑 떨어지는 모델은 없습니다. 만약 모델의 정확도가 100%로 나온다면 뭔가 이상한 것이죠. 99%가 나온다거나 한다면 차라리 overfitting이라고 할 수 있을지 모르지만, 100%라면 더 큰 문제, 데이터 자체에서 label로 구분되어 데이터가 학습된, data separation이 존재한다고 할 수 있습니다.
- 통계적으로 보면, 이 경우에 MLE(maximum likelihood estimate)는 제대로 동작하지 못합니다. 또한, 전체는 아니더라도, 상당한 분리 partial seperation이 있다고 해도, parameter estimate에 문제가 발생할 수 있구요. 즉, 만약 지나치게 큰 coeffcient가 모델에 포함되어 있다면, 이는 data separation이 당신의 데이터에 내재되어 있음을 말하고 있는 것일 수 있습니다.
- 따라서, 만약 데이터에서 data separation이 있는 것으로 추정된다면, 다른 방법들도 있겠지만, 그냥 데이터를 더 수집하는 것이 필요하다, 는 것이 답이죠.

