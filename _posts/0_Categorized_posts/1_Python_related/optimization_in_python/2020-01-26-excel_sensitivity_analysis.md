---
title: Excel - Sensitivity Analysis
category: others
tags: excel linear-programming lp sensitivity-analysis
---

## Senstivity analysis. 

- 일반적으로 "민감도, 감응도 분석"이라고 부르는 Sensitivity Analysis는 Linear Programming을 통해 '(현재의 상황)에 최적인 해"를 이미 획득한 상황에서, 상황 자체가 달라지는 경우에 어떤 변화가 발생하는지를 파악합니다. constraint나 objective function의 값들이 바뀐다면, 최적값과 최적해가 어떻게 달라지게 되는지를 인지하고 있어야 한다는 것이죠. 
- 물론, 경우에 따라서는 일종의 시뮬레이션처럼 각 상수에 대해서 noise를 추가하여 다양한 상황에 대해 LP를 돌리고, 나름 최적 값을 찾는 방법도, 무식하지만, 좋은 방법이 될 수 있죠. 
- 아무튼, 여기서는 excel의 solver를 사용해서 LP 를 푼 다음, Senstivity Analysis Report를 통해 불확실성을 어느 정도 인지하는 방법을 알아봅니다. 


## Simplex method In EXCEL.

- 우선 민감도 분석을 하기 위해서는 simplex method를 통해 LP를 풀어야 합니다. 일단 풀어야, 어떤 변화가 발생했을 때, 그 값이 어떻게 달라지는지를 알 수 있는 것이니까요. 
- 해를 찾는 solver는 엑셀에서 기본적으로 제공하지 않습니다. 따라서, 맥의 경우 "도구" > "추가 기능" > "해 찾기 추가 기능"을 눌러 줍니다. 윈도우의 경우 다른 경로로 찾아야 할 수 있어요. 
- 그런데, [이 블로그](https://blog.naver.com/ksj8406/221431564032)에서 그림까지 추가하여 잘 정리해놓은 것을 볼 수 있었습니다. 사실, 어렵지는 않아요. 다음의 순서에 따라서 진행하면 되는데요. 
    - Decision Variable: `X1`, `X2`와 같이, 우리가 정의한 변수를 첫줄에 넣고 다음 줄은 비워둡니다. 비워두는 것은, 그곳에 각 변수의 값들이 들어와야 하는 것이죠. 가령 이 빈칸들이 `A3:B3` 이라고 합시다.
    - Constraint: 제한식들을 넣어야겠죠. X1, X2, Total, RHS 순으로 넣어줍니다. 즉 우리가 넣으려는 식이 `4X1 + 3X2 <= 30`이었다면, 4, 3, `=SUMPRODUCT(A7:B7, A3:B3)`, 30으로 들어가게 되겠죠. 모든 식에 대해서 이런 식으로 다 넣어줍니다.
    - Objective: 세번째 테이블에도 똑같이, Decisiion variable과 상수를 곱해주는 값을 넣어줍니다.
- 즉, 아래와 같이 표가 있다고 생각하고 보시면 대략 무슨 말인지 이해되실것 같아요. A, B, C에 각각 방정식을 채워넣어야 하는 것이죠.

```
Decision Variable				
X1  X2			

				
Constraints				
X1	X2	Totals	Signs	Limits
6	4	(A)	    <=	    30
1	2	(B)	    <=	    10
				
Objective function				
X1	X2	Total		
4	3	(C)		
```	

- 그 다음 solver를 켜서 값들을 설정해줍니다. 그리고, 보고서를 생성할 때, sensitivity analysis에 관한 report도 생성하도록 하면 됩니다.

## Senstivity Report Interpretation

- 일단, LP에서 발생할 수 있는 변화는 두 가지 입니다. 
    1) objective function의 계수가 바뀌는 경우 
    2) constraint의 RHS 등이 바뀌는 경우
- 각각의 변화에 대해서 현재의 최적해와 최적값이 어떻게 대응하는지를 설명해주는데요. 
- 변수셀: 
    - 허용 가능 증가치(Allowable increase): 이 값만큼 커지지 않는다면, 최적해는 유지된다.
    - 허용 가능 증가치(Allowable decrease): 이 값만큼 작아지지 않는다면, 최적해는 유지된다.
- 제한조건: 
    - 잠재 가격(shadow price): 해당 Constraint의 RHS가 1증가한다면, 최적값이 이만큼 증가하게 된다. 
    - 허용 가능 증가치(Allowable increase): 이 RHS가 이 값만큼 증가하지 않는다면, shadow price는 유지된다. 
    - 허용 가능 감소치(Allowable decrease): 이 RHS가 이 값만큼 감소하지 않는다면, shadow price는 유지된다. 

## wrap-up

- 공부를 했으니까, 쓰기는 쓰지만, 저는 그냥 python의 라이브러리들을 사용해서 푸는 것이 훨씬 편한 것 같아요.
- 물론, 엑셀은 훨씬 범용적인 툴이고, 이후에 어쩌면 사용할지도 모르지만, 너무 느리고 불편합니다.


## reference 

- <https://blog.naver.com/ksj8406/221432589524>
- <https://blog.naver.com/ksj8406/221431564032>