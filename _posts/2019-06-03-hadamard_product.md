---
title: hadamard product 를 알아보쟈. 
category: machine-learning
tags: ml machiine-learing har
---

## hadamard product?

- node2vec논문을 보면, 초반에는 쭉쭉, node embedding에 대해서 나오다가, 뒤쪽에 뜬금없이 edge embedding이 나오면서, 이거는 hadamard product로 처리하면 좋다, 정도의 언급이 있습니다. 
- 이건 그냥 binary operator이고, "이 두 노드의 벡터를 합해서 edge를 의미하는 새로운 벡터를 만든다"가 기본 골자인데, 어렵다고 생각했는데, 막상 써보니 존나 쉬워서 정리하기로 했습니다 하하. 

## element-wise product

- hadamard product는 우리가 쉽게 쓰는 element-wise product와 같습니다. 
- 아래 그림에서 보는 것처럼, 같은 위치에 있는 원소들을 그대로 곱해서 새롭게 넣어주면 되는 것이죠.

![](https://cdn-images-1.medium.com/max/1200/1*pU5dS3VF0f6xvEhziE-x6A.png)


## edge2vec

- jpeg처럼 그림을 압축할 때도 유용하게 사용될 수 있다고는 하는데, 그보다는 node를 조합해서 새로운 edge 벡터를 만드는데 유용하게 사용될 수 있을 것 같습니다. 
- 이걸 그대로 이용해서 일종의 link prediction으로 사용할 수도 있을 것 같구요.

## wrap-up

- 사실 이게 딱히 글을 쓸 정도의 꺼리는 아닌데, 오늘 배운거니까 정리하면 좋을 것 같아서 적었습니다 하하.