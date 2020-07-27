---
title: Programming) 왜 아직도 switch 문이 살아 있는가?
category: programming
tags: programming c switch if readability
---

## Intro - 왜 아직 switch가 살아있는가?

- 요즘에는 swift를 재미삼아 공부하고 있습니다. tutorial 책을 읽으면서 프로그래밍을 처음 공부하던 기억을 되살리면서 보고 있는데, `switch`문이 등장하더군요. 뭐, 그건 그럴 수 있는데 꽤나 길고 자세하게 설명이 이어집니다. 이 때 조금 이상한 기분을 느꼈죠.
- 저는 C로 처음 프로그래밍을 시작했습니다. C에도 switch 문이 존재하지만, 사실 `if`구문으로 충분히 변환이 가능하고 굳이 사용해야 할 필요성을 거의 느끼지 못했죠. 그리고 매 case 마다 `break`문이 들어가지 않으면 `default`가 실행된다는 것 또한 꽤나 non-직관적으로 느껴졌습니다. 그래서, 한번도 사용해 볼 필요성을 느끼지 못했고, 이후 python으로 넘어와서는 python에는 아예 `switch`가 존재하지 않기 때문에 사용하지 않았습니다.
- 아무튼, 그래서 문득 궁금하더군요. 왜 아직도 switch는 왜 살아 있는것일까? 라는 질문이 생겼죠.

## Switch vs. Else

- [GeeksForGeeks - switch vs else](https://www.geeksforgeeks.org/switch-vs-else/)에 이에 대한 대답이 꽤 자세하게 나와 있습니다. 그 내용들을 번역하여 요약하면 대략 다음과 같습니다.
- 우선 if-then-else statement의 경우는 값의 범위에 대한 평가를 하는 반면 switch는 하나의 값에 대해서만 비교를 하게 된다.
- switch가 속도 측면에서 우월) 만약 동시에 아주 많은 값들에 대해서 비교를 할 경우, switch 문은 hash-table처럼 변환하여 빠르게 처리해주기 때문에, 그 속도 측면에서 if-then-else statement에 비해 아주 우월한 성능을 가지게 된다(파이썬에서 딕셔너리처럼 처리해준다고 생각하면 됨). 따라서, multi-way branching에 대해서 훨씬 효과적으로 사용될 수 있음. 여기서 만약 5개를 기준으로 그것보다 많다면, switch를 적다면 if-then-else 를 쓰는 것이 효과적이라고 말하고 있음.
- switch가 가독성 측면에서 우월) switch 문은 case와 함께 하나의 변수를 추적하는 형태로 사용됨. 따라서, if 문에 비해 개발자의 의도가 더 정확하게 담기게 됨. 이는 에러 발생 가능성을 낮추며 동시에 유지보수를 쉽게 해줌.

## wrap-up

- 흠, 하지만, 사실 일상에서 switch문을 사용하여 아주 많은 경우의 case를 만드는 일은 매우 적습니다. 그리고, 하나의 값을 중심으로 비교하는 경우는 드물죠. 그래서 늘 if, else 를 사용하는 것이 훨씬 편합니다. 
- 하지만, 혹시 모르니까, "switch는 hash table처럼 처리해서 더 빠르다"는 정도로는 알아두는 게 나쁘지 않을 것 같네요.
