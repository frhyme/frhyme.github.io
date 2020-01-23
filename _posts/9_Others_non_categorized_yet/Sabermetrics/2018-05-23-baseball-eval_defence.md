---
title: 야구) 타격을 못해도 수비 잘하는 선수가 더 좋아요. 
category: baseball
tags: baseball sabermetrics FPct RF ZR UZR

---

- [이 포스트](http://birdsnest.tistory.com/75)를 참고하여, 작성되었습니다. 단순히 참고라기보다는 상당 부분 참고하였습니다. 

## 이제는 수비 지표들을 좀 정리해보겠습니다. 

- 최근 한용덕 감독은 팀의 엔트리를 구성할 때, "타격 잘하는 선수보다는 수비 잘하는 선수로 엔트리를 짠다"라고 말했습니다. 팬 입장에서는 기가 막힌 수비보다는 수비시프트를 뚫고 날아가는 타격이 더 보는 재미가 있지만서도, 결국 경기를 이기게 하는 건 수비입니다. 타격으로 점수 내는 것이 수비로 점수 막는 것보다 훨씬 어렵습니다.
- 그러나, 타격의 경우 '타율/출루율/장타율'처럼 타격에 대한 지표들이 어느 정도 완성되어 있는 반면, 수비에 대한 지표는 부족한 것이 사실입니다. 

## 좋은 수비란 무엇인가요? 

- 제 생각에는 대략 다음으로 정리할 수 있을 것 같습니다. 
    - 실책이 적어야 하고
    - 가능하면 그라운드의 많은 범위를 커버해야 하고 
    - 다른 야수들과의 연계 플레이가 좋아야 하고 

## FPct(Fielding Percentage)

- 아주 전통적인 계산법이기는 하지만, 수치 자체로는 문제가 많습니다. 
- 실책이 많아질수록 값이 안 좋아지는데, 포지션별로 '실책'이 많은 포지션이 있다는 것을 감안하면, 이 값은 전체 수비수의 효과를 측정하는 것에는 한계가 있습니다. 특히 강습타구가 많이 오는 유격수의 경우에는 실책의 개수가 올라가게 되서 불이익이 발생하게 됩니다. 

$$
FPct = (A+PO)/(A+PO+E)
A: Assist, 보살 
PO: Putout, 자살
E: Error, 실책
$$

## RF(Range Factor)

- 처음에는 'Range'가 들어가 있어서, 전체 그라운드에서 커버하는 범위를 모델링한 지표라고 생각했는데, 그것이 아니고, 수비수가 관려한 PO+A를 소화이닝으로 나눈 값을 의미한다. 

$$
RF = (PO+A)*9 \over Inn
Inn: Innings Played
$$

### 한계 

- 단 이 경우에도, 당겨치는 우타자가 많은 경우에, 유격수에게 공이 많이 오게 되면, 유격수는 운이 좋게 이 값이 올라가게 된다. 물론 단순하게 이 값을 시즌 내 전체 경기 등으로 계산하게 되면 충분히 유의미한 지표가 되긴 하겠지만. 

## ZR(Zone Rating)

- 야구장 전체를 구역별로 구분하고, 포지션이 담당해야 하는 구역을 설정한다(이미 설정되어 있다). 단순하게, 자신의 담당 구역에서 이루어진 타구 중에서 몇 개나 아웃을 잡아냈는가의 비율을 계산한다. 

![](http://www.baseballthinkfactory.org/szymborski/zrgrid.jpg)

### 한계 

- 단, **3루수가 이대호고, 유격수가 박기혁인 상황** 따라서 박기혁이 훨씬 많은 range을 커버하고 있다고 해도, ZR 만으로는 이를 파악할 수는 없다. 
- 그림에서 보는 것처럼 전체 그림에서 구역을 구분하였는데, 이는 '수비 시프트'를 반영하지 못한다.
- 슈퍼세이브! 를 반영하지 못한다. ZR의 경우 "수비수간의 경계에 위치한 영역은 수비수도 어쩔 수 없는 지역"으로 설정하였다. 하지만, 그 지역을 막아내는 것이 바로 슈퍼세이브! 과거의 정근우가 자주 하던 수비!. 이런 수비는 마치 슬램덩크처럼 타자들에게 심리적인 벽을 느끼게 해준다는 2차적인 의미도 있다. 아무튼, 어려운 공을 잡아내는 슈퍼 세이브에 대한 반영이 없다는 것. 

## UZR(Ultimate Zone Rating)

- 단순히 말하면, ZR의 업그레이드 버전. ZR은 개별 낙구를 모두 동일한 점수로 두고 평가하는 반면, UZR에서는 특정 구역에 떨어진 공의 가치(Average Run Value)를 통해 해당 낙구의 실점과의 연계성을 고려한다. 
    - 정확한 계산방법은 나와 있지 않은데, 내 생각을 아주 간단하게 설명하자면, 
    - 아웃카운트와 주루 상황을 고려하여, 그때 실점 기대값을 고려하고, 
    - 64개의 구역별 평균 실점을 고려하여, 
    - 아웃을 잡아냈을 경우, 상황을 고려하고 구역에 대한 평균 실점을 더하고
    - 아웃을 잡지 못했을 경우, 상황을 고려하고 구역에 대한 평균 실점을 빼서 계산하면 되지 않을까 싶다. 

![](http://www.retrosheet.org/hitloc.jpg)

- 현재는 UZR이 파크팩터, 타구 속도, 좌타/우타 등도 고려하여 더 정확하게 변화되었다고 하긴 하는데, 실제 계산방법을 확인해봐야 할것 같다. 


## wrap-up

- 이 외에도, TZ(Total Zone)도 있는데, 일단 UZR만 알아도 어느 정도 될 것 같아서 더 정리하지 않았다. 
- 세이버메트릭의 궁극적인 지향점은 **선수를 말하는 단 하나의 숫자**를 찾는 것이 아닐까 싶다. 표준화하고, weight를 매기고, 등등의 방법으로. 
- 그러나, 사실 수비의 경우에는 그 상황을 하나하나 파악하는 것이 필요하다. 예를 들어 우타자만으로 좁혀서 보고, 좌타자 만으로 좁혀서 보고, 상황을 보고, 종합해서 보고, 이런 반복을 통해서 '약점'을 찾는 것이 더 적합하다고 생각되는데, 세이버메트릭에서 찾는 '지표'들은 이 총체적인 값을 하나에 우겨넣음으로써 오히려 더 근시안적인 시각을 보여주는 것이 아닐까? 하는 생각도 든다. 
- 


## reference

- <http://birdsnest.tistory.com/75>