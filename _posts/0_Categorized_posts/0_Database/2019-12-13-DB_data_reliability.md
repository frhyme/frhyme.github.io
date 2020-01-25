---
title: data reliability
category: others
tags: graphdb database nosql 
---

## intro. 

- 요새는 DB를 좀 공부하고 정리하고 있습니다. 그 과정에서, 전통적인 relational DB에 비해서 새롭게 각광받고 있는 NoSQL류의 데이터베이스가 훨씬, data-reliable 측면에서 훨씬 안정적이라고 알려져 있습니다.
- 사실, 한국말로 바꾸면, data reliability는 데이터 신뢰도, 데이터 신뢰성 이라고 변환할 수 있죠. 대략 생각하자면, 데이터가 얼마나 정확하냐, 라는 것인데, 사실 저는 좀 이해가 안가는 거죠. 아마도, 이것은 지식의 문제로 보이기는 하지만. 
- 아무튼, 그래서 이게 무슨 말인지 [Data reliability](https://itlaw.wikia.org/wiki/Data_reliability)를 번역했습니다.

### definition 

> Data reliability is "the accuracy and completeness of computer-processed data, given the uses they are intended for."
- Data reliability(데이터 신뢰도)는 "컴퓨터로 처리된 데이터와 그 데이터가 목적으로 하는 것에 대한 정확도(accuracy)와 완전성(completeness)를 의미한다.

### overview 

> This context, reliability means that data are reasonably complete and accurate, meet the intended purposes, and are not subject to inappropriate alteration.
- 이 맥락에서, reliability는 데이터가 합리적으로 완전하고(complete) 정확하다는 것(accurate)을 의미하고, 그 목적에서, 데이터가 적절하지 못한 변경(alteration)이 되어서는 안된다.

> Completeness refers to the extent that relevant records are present and the fields in each record are populated appropriately. Accuracy refers to the extent that recorded data reflect the actual underlying information. Consistency, a subcategory of accuracy, refers to the need to obtain and use data that are clear and well defined enough to yield similar results in similar analyses. For example, if data are entered at multiple sites, inconsistent interpretation of data entry rules can lead to data that, taken as a whole, are unreliable.
- 완전성(completeness)는 "관련된 레코드(relevant record)가 존재하고, 각 레코드의 값들이 적절하게 채워져 있는 정도"를 말합니다. 
- 정확성(Accuracy)은 "기록된 데이터가 얼마나, 실제 근본적인/드러나있지 않지만 사실인(underlying) 정보를 반영하는지"를 의미합니다.
- 일관성(consistency)는 정확성(accuracy)의 하위 분류로, 같은 분석에 대해서 동일한 결과를 발생할 수 있기에 충분한, 방식으로 정리된 데이터를 획득할 수 있는지를 의미합니다.
- 만약, 데이터가 다양한 장소에서 들어온다면, 데이터에 대한 비일관적인 해석이 데이터를 신뢰하지 못하게 만들 수도있으니까요.

> Assessing data reliability can entail reviewing existing information about the data, including conducting interviews with officials from the organization being audited; performing tests on the data, including advanced electronic analysis; tracing to and from source documents; and reviewing selected system controls.
- 데이터의 신뢰성을 평가하는 것은, 데이터의 기본적인 정보들을 검토하는 것부터, 대상 조직의 관련 간부들을 인터뷰하는 것, 데이터에 대해 테스트하는 것, 최신 전자 분석을 수행하는 것, 데이터베이스에 대한 도큐멘테이션을 추적하는 것, 그리고 선택된 시스템을 제어하는 것 까지를 모두 포함한다.

## wrap-up

- 정리하자면, reliablity는 completeness와 accuracy라는 두 가지에 기반을 둡니다. 이를 그냥 엑셀 파일로 생각하고 설명하자면, missing value가 없을수록 completeness가 높고, 저장된 데이터가 실제로 존재하는 데이터일수록 accuracy가 높다, 라고 말할 수 있겠죠. 결국 데이터베이스는 데이터를 담는 것이고, 얼마나 실제 일어난 현상을 정확하게, 그리고 일관적으로 표현하는가를 의미합니다. 사실 앞서 말한 엑셀 파일의 경우는, 혼자 쓰니까 큰 문제가 없지만, 마치 구글 시트를 공유해서, 약 1000명의 사람에 동시에 쓰고 있다면, 이거는 데이터가 누락될 가능성이 생기겠죠. 즉, 내가 데이터를 업데이트했는데, 하자마자, 다른 데이터가 변경되거나 하는 식으로 맞물려서 데이터가 유실될 가능성이 있습니다. 추가로, 쓰는 사람의 인터넷 환경이 좋지 않다거나 아무튼 다양한 변수가 존재할 수 있죠. 
- 데이터가 얼마나 '완전하게' 데이터베이스로 전송되었느냐, 그리고 그 데이터가 얼마나 정확하게 담겼는가, 이를 총체적으로 의미하는 것이 data reliability인 것으로 이해됩니다.