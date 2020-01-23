---
title: monte carlo tree search를 알아봅시다. 
category: others
tags: python python-libs simulation monte-carlo-tree-search tree search 
---

## intro 

- 최근에 최적의 tree구조를 찾아내는 연구를 수행하고 있습니다. 그 과정에서 처음에는 genetic algorithm을 활용하여 최적화로 풀어보려고 했는데, 이 방법 외에도 강화학습을 쓸 수 있지 않을까? 라고 막연하게 생각이 되었어요. 
- 그래서 좀 찾아보다보니 우선 **monte-carlo tree search**를 체크해보는 것이 필요할 것 같더라구요. 그래서 그 방법을 좀 알아보고 정리해보려고 합니다. 

## monte-carlo simulation 

### defitnion 

- tree search를 알아보기 전에 우선, monte-carlo simulation부터 먼저 알아야합니다.
- [monte-carlo simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method)의 정의는 다음과 같습니다. 

> Monte Carlo methods (or Monte Carlo experiments) are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results.

- 한국말로 바꾸면 어떤 수치적인 값을 얻기 위해서 랜덤성을 이용하는 모든 알고리즘들, 을 말한다고 하면 되겠죠. 

### example - compute pi 

- 예전에도 한번 한 것같지만, pi를 monte-carlo simulation을 사용해서 해봅시다. 
- 예를 들어서, 한 변의 길이가 2cm인 정사각형의 바구니가 있다고 해봅시다. 그리고 제가 그 정사각형에 공을 던진다고 합시다(공이 정사각형의 균등한 확률로 간다고 가정해봅시다. 
- 그리고 해당 정사각형 안쪽에 정사각형을 꽉 채우는 원통형의 바구니도 있다고 가정을 합시다. 바구니의 두께는 매우 얇아서 제가 던지는 공이 바구니에 맞고 튀어나올 가능성은 없다고 하구요. 
- 이때, 어떤 공은 원형의 통 안에 들어가고, 어떤 공은 원형의 통 밖에 들어가게 되겠죠. 
- 만약 제가 수십만개의 공을 던져서, 그중에서 몇 개의 공이 원형의 통 안에 들어갔는지를 세어 보면, 어떨까요. 
- 우리는 이미 정사각형의 넓이를 알고 있습니다. 여기에 비례해서 원형의 통의 넓이도 대략 알 수 있죠(공의 개수로). 그렇다면 이걸 이용해서 pi값도 계산할 수 있겠죠. 

- code는 대략 다음과 같습니다. 실제로 n이 증가할수록 점점 값이 근사해지는 것을 알수 있습니다. 

```python
import numpy as np 

ns = [10**i for i in range(1, 8)]
for n in ns:
    mat1 = np.random.uniform(-1, 1, (n, 2))
    result = np.apply_along_axis(lambda x: 1 if (x[0]**2+x[1]**2)<1 else 0, axis=1, arr=mat1)
    print(f"n:{n:8d}, estimated pi: {np.sum(result)/n*4:13.12f}")
```

```
n:      10, estimated pi: 2.400000000000
n:     100, estimated pi: 3.200000000000
n:    1000, estimated pi: 3.116000000000
n:   10000, estimated pi: 3.143200000000
n:  100000, estimated pi: 3.137280000000
n: 1000000, estimated pi: 3.142656000000
n:10000000, estimated pi: 3.141124800000
```

## monte-carlo tree search 

- 앞서 보여준 아주 간단한 수준의 monte-carlo simulation이 말해주는 것은, 랜덤성만 가지고 알고리즘을 설계해도 꽤 잘 맞출 수 있따는 것이죠. 물론 컴퓨팅 파워가 존나 좋아야 합니다. 다시, 단순히 말하면, 랜덤한 값을 생성하는 것만 가지고도 알고리즘을 잘 설계하면, 꽤 괜찮은 값을 가져올 수 있다는 것이죠. "랜덤성만 가지고도 특징적인 부분을 캡쳐할 수 있다"라는 것이 중요합니다. 
- 따라서, monte-carlo 를 그대로 이용해서 더 재미있는 짓들을 해봅시다. 
- [monte-carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)라는 것이 있습니다. 위키피디아에 의하면 

> In computer science, Monte Carlo tree search (MCTS) is a heuristic search algorithm for some kinds of decision processes, most notably those employed in game play. 

- 라고 하죠. 연속적으로 결정해야 하는 프로세스(예를 들면, 하스스톤같은 턴 베이스의 게임들처럼)에서 적절한 혹은 최적의 행동을 찾는 휴리스틱한 방법들이 여기에 포함됩니다. 조금 더 자세히 보면 

> The focus of Monte Carlo tree search is on the analysis of the most promising moves, expanding the search tree based on random sampling of the search space.

- 라고 하죠. 가능한 대안 중에서(search space중에서) 랜덤 샘플링을 하고 거기서, 가장 유망한 움직임을 찾아냅니다. 

### algorithm 

- 알고리즘이니까 단계가 있겠죠. 다음과 같은 네 가지 단계가 있습니다. 우선 그림부터 보시죠. 
- 그림의 값들을 잘 보면, child node의 분모끼리 합치고, 분자끼리 합치면 parent node의 값이 되는 것을 알 수 있습니다. 직관적이므로 따로 설명은 하지 않겠지만, root node의 값인 12/21 의 경우 21번 게임을 수행했는데, 12번 이겼다는 것을 말하죠. 즉, root node의 값은 현재 상황에서의 확률믈 말하고, child node의 값들은 현재 상황에서 child node로 움직였을때(게임에서 선택할 수 있는 움직임이 되겠죠), 그 상황에서 얻을 수 있는 승리 확률을 말합니다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/MCTS_%28English%29_-_Updated_2017-11-19.svg/808px-MCTS_%28English%29_-_Updated_2017-11-19.svg.png)

#### node definition

- R(current game state): 
    - Root node를 말합니다. 현재 상황을 말하는 것이 되겠죠. 예를 들어 오목이라면 현재 바둑 판에 놓여진 돌들이 현재의 상황을 말하고, 이 상황이 root node가 됩니다. 
- L(leaf node):
    - 현재의 상황에서 가장 최적(가장 승리로 이끌 가능성이 큰)의 움직임을 연속적으로 선택해서 내려갑니다. 이는 R에서 가장 적절한 childe node를 연속적으로 선택하면서 내려간다는 말이 됩니다. 이 때 더이상 child node가 없는 곳까지 내려갈 경우, 그 노드는 leaf node겠죠. 물론 tree search를 검색해갈수록 L에게도 새로운 child node가 생기기 때문에 영원히 leaf node인 것은 아니죠. 
- C(child node):
    - 말그대로, 현재 node의 child node를 말합니다. 

#### step definition

- **Selection**: 
    - start from root R and select successive child nodes until a leaf node L is reached. The root is the current game state and a leaf is any node from which no simulation (playout) has yet been initiated. The section below says more about a way of biasing choice of child nodes that lets the game tree expand towards the most promising moves, which is the essence of Monte Carlo tree search.
    - R에서 출발하여, leaf node에 닿을 때까지, 연속적으로 child node를 선택해 내려갑니다. 물론, 여기서 가급적이면 승률을 높이는 move(promising move)를 선택하는 편이 제일 좋겠죠. 물론, 반드시 그래야 한다라고 할 수는 없습니다. 승률을 높이는 move로만 움직일 경우, local optimum에 빠질 가능성이 높아지고, 초기의 선택에 따라서 결과가 좌우될 수 있거든요. 

- **Expansion**: 
    - unless L ends the game decisively (e.g. win/loss/draw) for either player, create one (or more) child nodes and choose node C from one of them. Child nodes are any valid moves from the game position defined by L.
    - child node에서 새로운 node를 추가하는 경우를 말합니다. 현재 child node가 가지고 있는 값은 현재 child node에서 playout을 했을때(즉, 랜덤하게 움직여서 게임을 운영했을때)의 값을 말하죠. 그게 아니라, 정확하게 해당 게임내에서 유효한, 특정 움직임이 정의된 새로운 node를 만드는 것을 expansion이라고 합니다. 

- **Simulation**: 
    - complete one random playout from node C. This step is sometimes also called playout or rollout. A playout may be as simple as choosing uniform random moves until the game is decided (for example in chess, the game is won, lost, or drawn).
    - 특정 노드에서 게임이 결정될 때까지(이기든, 지든, 무승부든) 게임을 random하게 돌립니다. 

- **Backpropagation**: 
    - use the result of the playout to update information in the nodes on the path from C to R.
    - simulation을 통해 획득한 결과를 해당 노드에 반영함은 물론 parent node로 순차적으로 올라가면서 반영합니다. 


### issues

- 즉, 여기서 이슈는 다음 두 가지로 나뉩니다. 
    - tree의 breadth search(너비)를 어떻게 줄일 수 있을까?(바둑의 경우 가능한 모든 action space는 매우 큼)
    - tree의 depth search(깊이)를 어떻게 줄일 수 있을까?(어떻게 더 진행하지 않고, 진다, 이긴다를 파악할 수 있을까? 그 결정적인 상황(혹은 수읽기)를 파악할 수 있을까?)
- [알파고의 경우 이를 뉴럴넷을 통해서 개선했는데, 이 내용은 이 블로그에 잘 나와 있습니다](http://sanghyukchun.github.io/97/)

### in alphago 

- [이 포스트에 있는 내용을](http://sanghyukchun.github.io/97/) 요약해서 보자면 대략 다음과 같습니다. 

- SL of policy network:
    - input(t 시점의 바둑판 기보) ==> output(t+1시점의 바둑판 기보)에 대한 CNN을 만들었습니다.
    - 어찌보면 간단한 classification network일 뿐이고, 현재 상황에서 최적의 '수'를 찾는 네트워크죠. 물론 막대한 컴퓨팅파워로 아주 많은 양의 데이터를 학습했습니다만, 네트워크 구조는 그냥 CNN과 다른 것이 없습니다. 

- RL of policy network: 
    - 간단하게, 이전 시점의 RL network와 현재의 RL network를 계속 대국하게 합니다. 이 과정에서 이기는 RL network에게 reward를 주고 업데이트를 하죠. 
    - 이것을 반복하다보면 현재 RL은 generalization을 획득하고, reward가 높은 놈이 결국 살아남게 됩니다(이렇게 보니까 메타휴리스틱 같기도 한데)

- RL of value network:
    - 이건 regression 문제입니다.
    - 현재 주어진 기보(s)에서 어떤 policy(policy network에서 주어진 값)를 취했을 때 그때 가질 수 있는 reward(승리, 혹은 실패)를 예측하는 것이죠. 
    - 물론 여기서 문제는, 어떤 기보 s 가 결국 궁극에는 승리해서 reward 1을 획득했다고 하면, 이전의 모든 successive position(이전의 모든 기보들)에게 reward가 모두 주어지게 됩니다. 즉 이 결과, 이 연속된 동작에 overfitting되는 문제가 발생한다는 것이죠. 
    - 이를 generalization하기 위해서 알파고의 경우는 역시, 자가대국을 통해 얻은 데이터를 무지하게 집어넣었습니다. 

## wrap-up

- 작게라도 코딩을 직접 해보고 싶다는 생각을 합니다. 오셀로 같은 게임이라면 적용할 수 있을 것도 같은데, 그래도, 제가 직접 하려면 매우 많은 시간이 걸리겠죠. 
- 흠. 그래도 한번 쭉 짜보면 많은 도움이 되지 않을까, 하고 혼자 생각해봅니다. 
- [이 자료에](https://spri.kr/posts/view/14725?code=issue_reports) 더 자세하고 많은 내용이 담겨 있습니다. 

## reference

- <https://en.wikipedia.org/wiki/Monte_Carlo_tree_search>
- <http://sanghyukchun.github.io/97/>
- <https://spri.kr/posts/view/14725?code=issue_reports>