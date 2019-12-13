---
title: What is soft-state
category: others
tags: graphdb database wikipedia
---

## (번역) soft-state Definition in wikipedia.

> In computer science, soft state is state which is useful for efficiency, but not essential, as it can be regenerated or replaced if needed. The term is often used in network protocol engineering.
- 컴퓨터 과학 분야에서, soft-state 는 '효율성(efficiency)를 '위해 유용한 상태'를 말한다. 필수적인 것은 아니다, 보통, 그것은 필요할 때, 재생산(regenerated)되거나, 대체될 수 있다는 것을(replace) 의미한다. 이 단어는 종종 network protocol engineering에서 사용된다.

> It is a term that is used for information that times out (goes away) unless refreshed, which allows protocols to recover from errors in certain services.
- soft-state는 서비스들이 오류로부터 회복되는 것을 허용해주기 위해서(즉, 서비스를 안정적으로 유지하기 위해서), 새로 고쳐지지 않을 경우, 정보가 소실되는 것(times out, goest away)을 말합니다.

> While in general less efficient than well-designed "hard state" protocols when tuned for a particular network regime, soft state protocols behave much better than hard state protocols in an unpredictable network environment such as the Internet.
- 일반적으로, 특정한 네트워크 regime에서는 잘 고안된 hard-state 프로토콜에 비해서 덜 효율적일 수 있지만, 소프트-스테이트 프로콜은 하드 스테이크에 비해서, 인터넷과 같이 예기치 못한 네트워크 환경에서는 훨씬 잘 작동한다.

## wrap-up

- 번역을 하기는 했는데, 솔직히 좀 애매한 부분들이 있습니다. 정리를 좀 해보자면, 기본적으로 soft-state는 확정적이지 않은, 소실될 수 있고 변화될 수 있는 것으로 보는 것 같습니다. non-deterministic이라고 표현하는 것이 훨씬 좋겠네요. 이를 다르게 표현하면, 현재의 상태가, 고정적으로 유지되는 것이 아니라, 외부에서 데이터 변경이 들어왔을 경우, 이 데이터를 최신으로 유지한 다음에야 반응한다는 것으로 볼 수 있죠. 만약 현재의 데이터가 최신이 아니라면, 알아서 커트하는 정도로 생각하면 될 것 같습니다.
- 하드 스테이트의 경우, 인터넷에 문제가 없는 환경에서는 잘 작동한다고 합니다. 즉, 하드 스테이트는, 인터넷에 문제가 없으니까 분산DB를 사용해도 각 노드에 있는 값들이 모두 일관적으로 동일하게 관리된다고 생각해도 되는 것이겠죠. 
- 그런데, soft-state는 앞서 말한 바와 같이, '인터넷이 다양한 문제로 끊기거나 하는 경우'에도 문제없이 디비의 일관성을 유지하기 위한 개념을 설명하기 위해 만들어진 것이라고 할 수 있겠네요. 특정 노드에서는, 경우에 따라서, 최신 데이터를 가지고 있지 않을 수 있습니다. 그리고, 다른 개념인, "Eventual Consistency(최종적인 일관성)"을 위해서도, 현재 노드는, 진짜 최신의 데이터를 가지고 있는 것이 아닐 수 있죠. 바로 적용되는 것이 아니니까요. 즉, 이처럼, '일정 시간 동안 실제로는 아무 변화가 없을지라도, 데이터 자체는 일종의 lazy evaluation처럼 적용될 수 있으므로, 가변적이다'는 것을 표현하는 것이 이 'soft-state'라고 할 수 있겠네요

## reference 

- [A question about soft-state in stackover](https://stackoverflow.com/questions/3342497/explanation-of-base-terminology?noredirect=1&lq=1)