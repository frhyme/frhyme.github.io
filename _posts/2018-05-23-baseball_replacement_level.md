---
title: 야구) Replacement level이 뭔가요?
category: baseball
tags: baseball replacement-level 

---

## 우선. 

- 철저하게 [이 포스트](http://birdsnest.tistory.com/74)의 내용을 기본 줄기로 삼습니다. 제가 변경하는 부분은 있을 것이고 관점을 달라질 수 있겠지만, 해당 포스트가 없었으면 이 포스트는 작성될 수 없었음을 명확하게 밝힙니다. 


## 비교의 척도. 

- 우리가 무엇을 평가할 때, '평균보다 높은가' 를 많이 이야기합니다. 시험 보고 나서도(특히 대학교 때는 늘) 평균보다 높은지만 따졌던 것 같습니다. 생각보다 평균을 넘었던 적이 그리 많지는 않다는 사실을 떠올리니 슬퍼지는군요. 
- 아무튼, 사실 '평균'이라는 것은 이미 아주 잘하는 수준입니다. 

## so, what is Replacement level 

- 책 <Baseball between the Numbers> 에 나오는 "Replacement Level"에 대한 정의를 그대로 옮긴 포스트에서 다시 복사하여 옮겼다. 

> Replacement Level is the expected level of performance a major league team will receive from one or more of the best available players who can be obtained with minimal expenditure of team resources to substitute for a suddenly unavailable starting player at the same position.

- suddenly unavailable starting player at the same position: 특정 포지션의 주전선수가 부상, 이적 등으로 인해 공백이 발생했을 경우 
- one or more of the best available players who can be obtained with minimal expenditure of team resources: 즉시 데려올 수 있는(2군에 있거나 놀고 있거나) 선수 들로 해당 공백을 메꿈. 

- 즉, 빵꾸를 떼울 때, 즉시 메울 수 있는 수준의 선수, 리그에 무수히 많은 레벨의 선수들을 말한다(보통 한 명만으로 이 사람을 대체할 수는 없다). 예를 들어 한화 이글스의 2루수 정근우가 초반에 부진으로 인해 2군으로 내려갔을 때 그 자리는 오선진과 정은원 등으로 돌아가면서 채우게 된다. 

## Replacement Level 구하기 - 타자편 

### 가정들

- 100년 간의 MLB 데이터를 활용하고, 타격 지표는 RC/27을 활용한 결과 다음을 발견하였다. 
    1. "주전 선수와 대체 선수 간의 타석 비율은 8:2"이고
    2. 평균적인 대체선수들은 평균적인 주전 선수들에 비해 80%의 성적을 냈다. 단 포수의 경우는 85%, 1루수의 경우는 75%.
    - 포수는 공격력이 약하고, 1루수는 공격력이 강하기 때문에 이런 결과가 발생한 것으로 생각됨. 

- Replacement Level 선수의 타격 스탯은 아래의 공식을 활용해 계산한 값 P를 기존 선수의 스탯에서 각각 빼서 계산됩니다.
    - R: 0.8(단 포수의 경우 0.85, 1루수의 경우 0.75)

$$
P = (0.1073 - 0.11 * R) * \sqrt[3] {\frac{ (25 * OBP * SLG) }{(1.0 - AVG)}}
$$

### by example

- 예를 들어서 김태균(1루수)가 부상으로 인해 결장하게 되고, 이 때 김태균의 기존 stat이 0.4/0.6/0.9 라고 합시다(애정을 담아 스탯을 뻥튀기하였습니다). 
    - 김태균은 1루수이므로 R 값이 0.75가 됩니다. 
    - 계산한 P 값은 0.07이 됩니다. 
- 따라서 대체가능한 선수의 slash stat은 0.33/0.53/0.83 이 되는데....너무 높은데요??? 대체선수가 이정도만 해줘도 정말 좋겠습니다. 해당 선수의 stat이 좋을수록 이 값 또한 높아지게 되는데, 이게 맞는건가? 
    - 음, 이를 굳이 설명하자면, "해당 선수가 extraordinary 뛰어날 수록, 해당 팀에는 해당 선수때문에 빛을 보지 못하는 좋은 피지컬의 선수가 있을 수 있다", 예를 들면 양의지로 인해 꽃피지 못했다고 평가받기도 하는 '최재훈', '박세혁' 등이 그렇고. 
    - **즉 뛰어난 선수일수록, replacement level의 선수 또한 뛰어날 수밖에 없다** 라는 논리인 것이죠. 이게 맞는건지 모르겠네요. 

- 또한, 일반적으로는 replacment level의 선수와 주전 선수간에는 득점에서 20점 정도의 차이가 발생한다고 합니다. 보통 10점을 1승으로 간주하게 됩니다(나름 상관관계가 높은 설득력 있는 지표). 따라서 어떤 시즌에 주전 선수가 풀시즌을 뛰어 80승을 거두었는데, 다음 시즌에 부상으로 인해 시즌 아웃이 되었다면 이번 시즌에는 78승을 거둘 것이다. 라는 말로 설명할 수 있는 것이죠. 
    - 물론 경우에 따라서, 10득점을 2승으로 보는 경우도 있지만, 만약 지나친 타고투저 리그라면 10득점은 2승보다 적다고 볼 수 있겠죠. MLB에서도 AL은 2.5승, NL은 2승으로 봅니다. 

## Replacement Level 구하기 - 투수편 

- 앞서 타자의 경우도 Replacement Level은 slash stat(AVG/OBP/SLG)를 가지고 평가하지만, 투수의 경우는 RA(Runs Average), 리그 평균 실점(자책+비자책)을 활용하여 계산합니다. 
- 우선 현대 야구는 '선발 투수(Starter)'와 '구원 투수(Reliver)'가 분리되어 있으며 따라서 이 둘을 분리하여 평가합니다. 각각 아래 의 계산 방식에 따라 계산됩니다. 

$$
Replacement Level Starter RA = 1.37 x League Average RA - 0.66
Replacement Level Reliever RA = 1.70 x League Average RA - 2.27
$$

## wrap-up

- 처음에는 Replacement level을 계산하는 방법이 "실제 전체 선수들의 타격 지표를 활용하여 분포를 도출한 다음, 특정 지점에 있는 값(예를 들어서, 1quantile)에 있는 수준을 대체 가능한 수준으로 본다"는 것일줄 알았는데, 이런 것이 아니라, slash stat(AVG/OBP/SLG)를 그대로 활용하여 계산한다는 것이 약간 의아했습니다. 
    - 더 좋은 방법이 있지 않을까 싶습니다만 흠. 
- 아무튼, 결과적으로 말하자면, 기존 데이터들을 활용해 '대체선수레벨을 구하는 공식'을 고안하고, 이 공식에 기존 선수들의 스탯을 집어넣으면, 해당선수가 부재할 경우, 획득할 수 있는 선수의 스탯을 계산할 수 있습니다. 
- 또한 일반적으로 주전 선수는 대체 선수 대비 20점 정도의 득점을 더 올릴 수 있다, 라고 합니다. 
- 그러나, 여기서 말하는 Replacement level에는 '타격'만 고려되어 있다는 한계가 있습니다. wOBA와 마찬가지인데, 해당 선수의 수비 지표, 도루 지표는 Replacement Level에 어떻게 반영될 수 있을까요


## reference

- http://birdsnest.tistory.com/74