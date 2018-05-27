---
title: 야구) 야구에 Markov Chain 적용하기
category: baseball
tags: baseball markov-chain sabermetrics

---


- [Markov chain의 영문 위키피디아](https://en.wikipedia.org/wiki/Markov_chain#Discrete-time_Markov_chain) 아래 쪽을 보면 다음과 같은 내용이 담겨 있습니다. 

> Markov chain models have been used in advanced baseball analysis since 1960, although their use is still rare. Each half-inning of a baseball game fits the Markov chain state when the number of runners and outs are considered. During any at-bat, there are 24 possible combinations of number of outs and position of the runners. Mark Pankin shows that Markov chain models can be used to evaluate runs created for both individual players as well as a team.[84] He also discusses various kinds of strategies and play conditions: how Markov chain models have been used to analyze statistics for game situations such as bunting and base stealing and differences when playing on grass vs. astroturf.[85]

- 한글로 해석하자면, 대략 다음과 같습니다(발로 번역했습니다)

> 마코브체인은 존나 잘 쓰이지도 않던 1960년대에 야구쪽에서 쓰였다. 개별 이닝은 아웃카운트와 주자 로 구분된 24가지 상황을 state로 한 마코브 체인으로 모델링될 수 있으며, 팀과 선수가 득점에 얼마나 기여하는지를 평가하기 위해 사용될 수 있음을 Mark Pankin이 증명했다. 또한, 마코브체인을 이용하여 다양한 전략과 경기 조건(번트와 도루, 조건: 잔디, 인조잔디)을 분석하였다

- 사실 다시 생각해보면, 턴제로 구분되어 있는 야구는 마코브체인으로 모델링하기에 매우 적합한, 게임입니다. 이미 데이터도 아주 많이 쌓여 있는 것이 사실일 것이고요. 