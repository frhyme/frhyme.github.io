---
title: 야구) 야구에 Markov Chain 적용하기
category: baseball
tags: baseball markov-chain sabermetrics

---

## 야구 equals 마코브 체인 

- [Markov chain의 영문 위키피디아](https://en.wikipedia.org/wiki/Markov_chain#Discrete-time_Markov_chain) 아래 쪽을 보면 다음과 같은 내용이 담겨 있습니다. 

> Markov chain models have been used in advanced baseball analysis since 1960, although their use is still rare. Each half-inning of a baseball game fits the Markov chain state when the number of runners and outs are considered. During any at-bat, there are 24 possible combinations of number of outs and position of the runners. Mark Pankin shows that Markov chain models can be used to evaluate runs created for both individual players as well as a team.[84] He also discusses various kinds of strategies and play conditions: how Markov chain models have been used to analyze statistics for game situations such as bunting and base stealing and differences when playing on grass vs. astroturf.[85]

- 한글로 해석하자면, 대략 다음과 같습니다(발로 번역했습니다)

> 마코브체인은 존나 잘 쓰이지도 않던 1960년대에 야구쪽에서 쓰였다. 개별 이닝은 아웃카운트와 주자 로 구분된 24가지 상황을 state로 한 마코브 체인으로 모델링될 수 있으며, 팀과 선수가 득점에 얼마나 기여하는지를 평가하기 위해 사용될 수 있음을 Mark Pankin이 증명했다. 또한, 마코브체인을 이용하여 다양한 전략과 경기 조건(번트와 도루, 조건: 잔디, 인조잔디)을 분석하였다

- 사실 다시 생각해보면, 턴제로 구분되어 있는 야구는 마코브체인으로 모델링하기에 매우 적합한, 게임입니다. 이미 데이터도 아주 많이 쌓여 있는 것이 사실일 것이고요. 
    - 정확하게는 discrete Time Markov Chain(DTMC)에 적용하기 적합합니다. Time은 매 아웃카운트 로 구분될 수 있겠죠
    - 축구처럼 턴이 명확하지 않은 경우에는 Continous Time Markov Chain을 쓰는 것이 적합할 것 같네요. 

## 야구를 DTMC로 모델링합시다. 

- 기사말고, 좀 잘 정리된 자료를 찾아봤는데 다행히 [여기에](http://www.pankin.com/markov/theory.htm) 있습니다. 일단은 이 내용을 기준으로 진행하겠습니다. 

- `T`: Transition matrix(state to state), 28 by 28 matrix
    - \#01: 0아웃 주자없음 
    - \#02: 1아웃 주자없음
    - \#03: 2아웃 주자없음
    - \#04: 0아웃 1루
    - ...
    - \#07: 0아웃 2루
    - ...
    - \#10: 0아웃 3루
    - ...
    - \#13: 0아웃 1,2루
    - ...
    - \#16: 0아웃 1,3루
    - ...
    - \#19: 0아웃 2,3루
    - ...
    - \#20: 0아웃 1,2,3루
    - ...
    - \#25: 쓰리아웃 무득점 
    - \#26: 쓰리아웃 1득점
    - \#27: 쓰리아웃 2득점
    - \#28: 쓰리아웃 3득점

- `R`: each plate appeareance 별 기대득점 matrix 28 by 1 matrix 
    - R(1)  = p1,1
        - state1(0아웃 주자없음)에서 다시 state1이 될 확률은 결국 홈런밖에 없음. 
    - R(2)  = p2,2
    - R(4)  = 2p4,1 + p4,4 + p4,7 + p4,10 + p4,2
    - R(23) = 4p23,2 + 3(p23,5 + p23,8 + p23,11 + p23,3)
        + 2(p23,14 + p23,17 + p23,20 + p23,6 + p23,9 + p23,12 + p23,27)
        + p23,23 + p23,15 + p23,18 + p23,21 + p23,26
    - R(25) = R(26) = R(27) = R(28) = 0

- `E`: R + TR + TTR + TTTR ..., 해당 state부터 이닝 종료까지의 생산 가능한 득점, 28 by 1 matrix 
    - `R`은 각 state에서 each plate appearance에서 발생가능한 득점을 말하고, 여기에 T를 연속으로 곱해간다는 것은 각 상황에서 타석이 끊어지지 않고 이어질 경우를 고려하는 것임. 따라서 이렇게 계산된 값은 해당 state부터 이닝 종료까지 생산 가능한 득점을 말하고, 이를 `Markov Run`이라고 함. 
    - = (I + T + T2 + T3 + … )R 
    - = (I - T)-1(I - T)(I + T + T2 + T3 + … )R [since (I - T)-1(I - T) = I] 
    - = (I - T)-1(I - T + T - T2 + T2 - T3 + T3 - … )R 
    - = (I - T)-1IR 
    - = (I - T) - 1R 

## with identical batter: 김태균 

- 저기서 `T`를 김태균의 타율로 조정해서 넣어 보겠습니다. 모든 타자가 김태균이라고 가정하고. 




- [Tom tango가 만든 Run Expectancy matrix](http://www.tangotiger.net/RE9902.html)는 개별 상황으로부터 이닝 종료까지 득점을 평균을 내어 계산된 표이다. 

## reference

- <https://www.fangraphs.com/tht/introducing-markov-chains/>
- <https://www.fangraphs.com/blogs/more-fun-with-markov-custom-run-expectancies/>
- <http://www.pankin.com/markov/theory.htm>