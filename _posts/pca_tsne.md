---
title: 데이터의 차원을 줄여봅시다. 
category: python-lib
tags: python python-lib sklearn matplotlib dimensionality-reduction

---

## 데이터 차원을 왜 줄여야 하나요? 

- 우선 쓸모가 없으니까요. 사람들이 **빅데이터**라는 말을 하기 시작한 이후부터는(물론 저 단어는 정말 쓸모없습니다만), 가령 엑셀같은 데이터에 그냥 칼럼이 엄청 많아도 너무너무 좋다고 생각할 지도 모릅니다. "우리에게는 빅데이터가 있어" 라고 생각할지도 모르죠. 그런데, 그 데이터의 대부분의 칼럼이 단 하나의 변화를 표현할 뿐이라면요? 계산 시간과 리소스는 많이 잡아먹지만, 별 필요가 없다면요? 그래도 괜찮을까요? 쓸모없는 데이터를 줄입시다. 필요업어요. 
- 데이터를 예쁘게 보고싶으니까요. 인간이 시각화된 데이터를 인지하는 차원은 아직은 3차원이 맥스입니다. x,y축 그리고 색. 3차원으로 렌더링을 하면 그림이 안 이쁘죠. 아무튼 그렇기 때문에 사람이 인지적으로 그림을 직관적으로 이해하려면 차원을 줄이는 것이 필요합니다. 

## PCA(Principal Component Analysis)

- 한국말로 하면 '주성분분석'정도가 되려나요? 

## t-SNE 

## isomap?? 



## conclusion

- 당장 구글에만 검색을 해봐도, pca가 좋은지, t-sne가 좋은지에 대한 이슈들이 많습니다. 가장 큰 차이라면 PCA는 모든 벡터들이 linear하다고 가정하고 시작한다는 점. 따라서 local structure가 무너질 수 있다는 점. 

## reference 

- https://medium.com/@luckylwk/visualising-high-dimensional-datasets-using-pca-and-t-sne-in-python-8ef87e7915b