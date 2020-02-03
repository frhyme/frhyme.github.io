---
title: 야구) 타구 비율 지표
category: baseball
tags: baseball hit sabermetrics

---

## intro: 윤성환 vs 이대형

- 이미 보신 분들이 많으시겠지만, [상대적으로 그렇게 좋은 타자라고 평가하기는 어려운 이대형 선수는 윤성환 킬러로 유명합니다(http://mlbpark.donga.com/mlbpark/b.php?&b=kbotown2&id=1404201). 
- 이대형 선수는 땅볼을 많이 만드는 유형의 타자입니다(투수가 공을 던졌을 때, 위쪽을 맞춘다는 이야기죠), 반면 윤성환 투수의 경우는 타자에게서 뜬공을 많이 유발하는 유형의 타자입니다(타자가 공 아래쪽을 맞춘다는 이야기죠). 그래서 이대형 선수가 윤성환 선수를 만나면, 정타를 맞게 된다는 아주 흥미로운 이야기입니다. **역시 야구는 과학이다**, 라고 말씀드릴 수 있을 것 같아요. 
- 이렇게 세부 지표를 보기 시작하면 그동안 이해 되지 않던 야구의 모습들이 새롭게 다가오기 시작합니다. 그러니까, 머니볼에서 빌리빈의 대사처럼 **야구는 사랑하지 않을 수 없습니다**. 특히 저와 같은 한화 팬들에게는 이렇게라도 야구를 즐겨야 덜 괴롭습니다 하핫. 

## GO/AO or GB/FB

> 땅볼아웃/뜬공아웃 비율, Ground Out Per Air Out

- 흔히들 '땅뜬비'라고 말한다고 합니다(하지만 볼삼비는 자주 듣지만, '땅뜬비'라는 말은 굉장히 낯설군요). 간단하게, **뜬공 대비 땅볼이 얼마나 많은가?** 에 대한 이야기인데, 물론 투수의 유형에 따라서 달라지지 않는지 파악해야 하겠지만, 타자의 유형을 직접적으로 파악할 수 있기 때문에, 유용하다고 생각됩니다. 
- 특히, 대타를 내보낼 때는 현재 투수에게 가장 강한 선수를 내보내어야 합니다. 만약, **희생플라이가**가 중요한 순간이라면(뭐 물론 대타를 내는 순간들이 대부분 득점권이고, 희생플라이가 중요한 상황이긴 합니다), 현재 투수의 유형에서 가장 뜬공 생산 비율이 높은 선수를 내보내는 것이 적절하겠죠. 
- 따라서, 이 지표만으로도 현재 타자의 타격 자세에서의 문제점을 어느 정도 짚어낼 수 있지 않을까? 생각하게 됩니다. 흠, 이걸 좀 더 파악하려면 **투수의 구종**과 **타격 자세**등도 파악해야 할 것 같은데, 어려우므로 이건 다음에 해보겠습니다.
- 마찬가지로 투수에게도 적용할 수 있겠죠. 이 지표를 통해서 투수가 땅볼을 많이 만드는 유형의 투수라는 것이 도출된다면, '투수는 스트라이크 존의 아래 쪽을 공략하는 경향성이 있다'라는 해석을 할 수 있을 것 같기는 한데, 이건, 굳이 지표 필요없이도, 존에서 어느 쪽을 공략하는 지 그림으로 보면 될 것 같네요. 


## GB%, LD%, FB%, IFFB% 

> 땅볼 비율, 라인드라이브 비율, 뜬공 비율, 내야팝업(내야 뜬공) 비율

- 이 지표는 제 판단에서는 약간 '오버'하고 있다고 판단되어서, 알아보지 않겠습니다.

## HR/FB

> 뜬공 중 홈런 피율(HR / Fly Ball)

- 흠, 뜬공 중에서 담장을 넘어갈 비율을 의미한다고 합니다. "공을 띄운다"는 것은 공의 약간 아래쪽에 배트를 맞춘다는 것이죠. 너무 아래쪽을 맞추면 발사각이 높아지므로 내야 뜬공이 될 수 있고, 적절하게 맞추어서 대충 각도는 맞는데, 배트를 제대로 회전하지 못하였다거나, 힘을 전달하지 못하였다면 외야 뜬공이 될 가능성이 있겠죠(물론, 수비수가 빈 곳에 보낼 수도 있지만 공이 느리면 외야수들이 잡을 가능성이 높아지니까요). 
- 이 지표는 아주 단순하게 보면 뜬공의 생산성 정도로 평가할 수 있겠지만, 대부분의 거포형 홈런타자들은 '뜬공'수와 '홈런'수가 모두 많을 것 같습니다. 좀 미묘하군요. 

## IFH%, BUH% 

> 내야안타(Infield Hit), 번트안타 비율

- 전체 땅볼 중 내야안타의 비율, 번트 시도 중 내야안타가 된 비율이라고 하는데, 이것도 일단 무시할게요. 

## Pull%, Cent%, Oppo%

> 타구 방향의 비율(당겨친 비율, 가운데 비율, 밀어친 비율)

- 오른손 타자를 기준으로 당겨치면 야구장 왼쪽으로 공이 향하게 됩니다. 밀어치면, 오른쪽으로 가게 되고, 음..가운데는 어떻게 보내죠? 적절하게....치면 중간으로 갑니다. 아무튼 이 비율은 투수를 평가하는 지표라기 보다는 타자를 평가하는 지표가 됩니다. 
- 굳이 투수와의 관련성을 따지자면, 해당 투수가 '바깥쪽'과 '안쪽' 어느 쪽을 주로 공략하느냐의 문제와 연계될 수 있는데, **타자입장에서는 공이 바깥쪽으로 오면 밀어치고, 안쪽으로 오면 당겨치는 것이 적절합니다**. 그러나, 
- 어쨌든, 특정한 타자가 `Pull%`, `Cent%`, `Oppo%`의 비율이 고르다면(샘플 사이즈가 충분한 경우에), 해당 타자는 소위 '스프레이히터'라고 부를 수 있습니다. 공을 어느 쪽이든 잘 보낼 수 있다는 것이죠. 
    - 국내에서는 이 지표를 데이터화하여 관리하지 않는 것 같고, [MLB의 추신수 기록](https://www.fangraphs.com/statss.aspx?playerid=3174&position=OF)을 보면 전체 타구의 방향 비율이 39.8%, 34.5%, 25.7%인데, 이정도면 스프레이히터라고 봐야 할 것 같습니다. 
    - 또 [류현진의 기록](https://www.fangraphs.com/statss.aspx?playerid=14444&position=P)도 봤는데, `17.0%, 50.2, 32.8 %` 인데, 중간으로 가는 비율이 높기는 하지만, 밀어치는 유형의 타자라고 해야겠네요(류현진은 좌투우타)
- 그러나 타자가 특정 값이 너무 높다, 예를 들어 `Pull%`가 대부분이라면, 수비시프트를 극단적으로 한쪽으로 밀어붙이는 것이 필요할 수도 있겠죠. 또 이 수비시프트를 뚤어내는 타자가 뚫어내는가, 도 매우 흥미로운 부분이 되구요. 

## Soft%, Med%, Hard% 

> 타구 강도의 비율(약한 타구 비율, 중간 타구 비율, 강한 타구 비율)

- 흠, 그런데, 이 강도를 어떻게 측정할 수 있는지 애매한 것 같습니다. 요즘은 타자가 공을 쳤을 때, 타구의 속도를 측정하기는 하니까, 타구 강도를 측정할 수는 있을 것 같습니다. 단, '타구 속도'는 continuous한 값인데 이를 굳이 저 세 가지 비율 지표로 나누어 카운트해야 하는지는 잘 모르겠네요. 그냥 타구 속도의 평균 정도로 하면 되지 않을까 싶은데. 

## BABIP 

> 인플레이로 이어진 타구에 대한 비율, Batting Average on Balls In Play

- 계산식으로 보면 명확합니다. **(총 안타수-홈런)/(타수-삼진-홈런+희생플라이+희생번트)**인데, 일단 "분모"의 경우 안타에서 홈런을 뺍니다. ?? 라는 생각이 들죠. 그리고 또 밑에도 타수에서 삼진과 홈런을 빼고, 희생플라이와 희생번트를 더합니다(다시 말하지만, 원래 '타수'에는 희생플라이와 희생번트가 포함되어 있지 않습니다. 작전에 의해 희생되었다고 보기 때문이죠). 아무튼 가만히 보면 뭔가 패턴이 보이지 않나요? 
- 네, **'인플레이로 이어진 타구'는 타자가 공을 쳐서 그라운드 내로 떨어진 타구**를 말합니다. 그래서 홈런같은 경우는 제외하는 것이죠. 
- BABIP는 1999년 보로스 맥크라켄(Voros McCracken)이라는 대학원생이 DIPS(FIP)라는 스탯과 함게 발표한 스탯이라고 합니다. 

### 투수에게 적용했을 때, 

- 그 당시에, 이 수치가 의미가 있었던 이유는 보로스가 이 스탯을 발표하면서 **"A급 투수나 C급 투수나 인플레이 볼이 안타가 되는지 범타가 되는지 여부는 전혀 차이가 없다"** 라고 말했기 때문인데, 이 말 자체가 논란이 되었기 때문이죠.
    - 아마도 지금의 우리는 저 말에 대해서 '수비시프트가 있는데 뭔 개소리냐! 라고 생각할 수 있을 것 같습니다'. 아마도 저 시기에는 타자별(당겨치는 유형, 밀어치는 유형 등) 수비시프트가 제대로 고안이 되지 못했던 것 같고, 따라서 항상 수비는 비슷한 위치에 존재해 있었겠죠. 그래서 어떤 투수의 공이든, 일단 타자가 쳤다면 그 공이 안타가 될 확률은 또이또이했던 것 같습니다. 
- 지금은 수비시프트로 인해서 과거와는 다른 야구가 펼쳐지고 있기 때문에, 그때의 BABIP 분포와 지금의 분포는 아예 다르게, 다른 데이터 셋으로 보는 것이 적합하지 않을까 싶습니다. 
- 또한, 이 수치는 '투수'보다는 '수비'에 의해 영향을 받습니다. 따라서 한 팀의 모든 투수는 비슷한 수비진과 플레이하기 때문에, 값이 비슷하게 나올 수 밖에 없지 않나 싶어요. 

### 타자에게 적용했을 때, 

- 단 투수와는 다르게 타자의 경우에는 이 수치가 유의미하다고 받아들여지는 편인 것 같습니다.
- 예를 들어, 우리는 다음의 경우를 많이 볼 수 있습니다. 
    - 2016시즌에 선수 A가 뜬금없이 고타율을 기록했고, BABIP의 값이 꽤 높았다고 합시다(친 공의 상당 비율이 안타가 되었다). 
    - 2017시즌에는 선수 A의 타구가 대부분 왼쪽으로 향하는 것을 발견하고, 수비 시프트를 걸었고, 따라서 BABIP는 떨어졌으며 타율도 함께 하락했다. 
- 만약, 이러한 상황을 극복하고(걸려있는 수비시프트를 뚫고) 타격기술로 안타를 만들어낸다면(시즌 내내 높은 BABIP를 유지한다면), 해당 선수는 좋은 타격 기술을 갖추었다, 라고 말할 수 있는것이죠. 
- 결국 BABIP가 계속 높다면, 스프레이히터에 가깝다, 라고 말할 수 있을 것이고, 혹은 타격폼을 변화하는 등의 방식으로 리그에 빠르게 적응한다, 라고도 말할 수 있겠네요. 

## reference 

- <http://blog.ncsoft.com/?p=34985>
- <https://namu.wiki/w/BABIP>