---
title: Probability vs. Odds.
category: others
tags: statistics probability odds
---

## Difference with Probability and Odds.

- 사실, 통계학적으로 보는 것이 아니라, 영어 단어로서 보면 이 둘이 가지는 의미는 비슷해 보입니다. 둘다 '가능성'을 의미하니까요. 기본적인 개념은 비슷하지만 이 둘의 개념은 조금 다릅니다. 

### Meaning of Both

- `Probability`, P 는 가능한 모든 event 중에서(N개의 trial) event E가 발생할 수 있는 likelihood를 말한다. 
- `Odds ratio`는 (Event E가 발생할 확률)/(Event E가 발생하지 않을 확률)을 말한다. 즉, `(P(E)) / (1 - P(E))`로 표현되죠. 즉 전체 가능한 모든 event중에서 발생할 수 있는 것을 말하는 것이 아니죠. 이는 '해당 이벤트의 성공확률이 실패 확률에 비해서 얼마나 더 높은지'를 의미합니다.

### Difference in detail.

- 차이를 좀 더 자세히 보겠습니다. 
- `probability`의 경우, 동일한 값이라면, `P(E)`는0.5가 됩니다. 그리고, 항상 0과 1사이의 값만을 가지게 되죠.
- `Odds Ratio`의 경우, 동일한 값이라면, 1이 됩니다. 즉, "1번 실패하면 1번 성공한다는 이야기죠". 그리고 이 Odds는 0부터 무한대까지의 값을 가질 수 있습니다. 사실, 이것이, `Odds Ratio`의 강점인데요. 
    - `Odds ratio`의 경우 range(0, inf)의 구간을 가집니다(앞서 말한 바와 같이 probability의 경우는 range(0, 1)이구요. 

### Probability : Linear Regression

- binary logistic regression에서 봤을 때, 좌변인 P(E)는 0과 1사이의 값을 가져아 합니다. 그리고, regression model은 아래와 같은 형태로 만들어져야겠죠.
- `P(E) = b0 + b1x1 + ... + bnxn` 의 모델로 만들어지죠(레이텍 쓰기 귀찮아서 대충 했습니다). 
- 이때 좌변항의 경우는 range(0, 1)을 가지는 반면 오른쪽의 경우는 range(-inf, inf)가 되죠. 서로 다른 space가 mapping됩니다. 

### Odds : Linear Regression

- Odds의 경우를 봅시다. 똑같이, `Odds(E) = b0 + b1x1 + ... + bnxn`의 형태를 가지게 되죠. 
- 여기서 `Odds(E)`는 range(0, inf)를 가집니다. 그리고 여전히 우변항은 range(-inf, inf)가 되구요. Probability보다는 낫지만, 여전히 좌변항과 우변항의 space는 다르게 mapping됩니다. 

### log-odds : Linear Regression

- 여기서 Log-Odd가 나옵니다. 이것이 우리가 종종 부르는 `logit function`이기도 하구요. 어렵지 않고, 그냥 Odd에서 log를 씌운 형태가 됩니다. 
    - `log(Odds(E))`
    - `=log( P(E|x) / (1 - P(E | x)) )`
- 자, 이제 Log-Odds를 사용해서 linear regression을 만든다고 생각해봅시다. 
- `log( P(E | x) / (1 - P(E | X)) ) = b0 + b1x1 + ... + bnxn`의 형태가 되죠. 
- 이렇게 변경하게 되면, 좌변항과, 우변항이 모두 range(-inf, inf)라는 동일한 범위를 가지게 됩니다.

## wrap-up

- 정리를 하자면, binary regression에서는 0과 1을 바로 나타낼 수 없기 때문에 우선 확률적인 값인 `P(E)`등을 이용하여 `P(E) = b0 + b1x1 + ... + bnxn` 형태로 표현합니다. 하지만, 이렇게 표현하게 될 경우, 좌변과 우변의 range가 다릅니다. 좌변은 proability이므로 range(0, 1)인 반면, 오늘쪽의 경우는 range(-inf, inf)를 가지죠. 따라서 이를 똑같이 mapping할 수 있도록 해주기 위해, Odds로 변경하고, 다시 Log-Odds로 변경해줍니다. 
- 조금 혼동되는 부분이 있었는데, [incredible.ai - logistic regression](http://incredible.ai/machine-learning/2016/04/26/Logistic-Regression/)의 글을 통해 명확하게 알 수 있었습니다. 이 글이 혹시라도 도움이 되셨다면, 그것으 제가 참고한 이 글 덕분입니다. 

## reference

- [Why use Odds Ratios in Logistic Regression](https://www.theanalysisfactor.com/why-use-odds-ratios/)

- [incredible.ai - logistic regression](http://incredible.ai/machine-learning/2016/04/26/Logistic-Regression/)

- [Why use odds and not probability in logistic regression?](https://stats.stackexchange.com/questions/215349/why-use-odds-and-not-probability-in-logistic-regression/215357#215357?newreg=4e74d383e6464030ac94dbc6e0aa5652)

- <http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Confidence_Intervals/BS704_Confidence_Intervals10.html>
- <https://en.wikipedia.org/wiki/Odds>