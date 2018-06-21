---
title: GAN을 사용해 봅시다. 
category: machine-learning
tags: python python-lib keras machine-learning neural-network
---

## GAN이 뭡니까. 

- GAN은 Generative Adversarial Network의 약자인데, 이를 한국말로 말하면, "생성적 적대적 네트워크"라고 할 수 있는데, 그냥 영어로 GAN 갠 혹은 간 이라고 읽읍시다. 
- 우리는 데이터를 가지고 있습니다. 어떤 크기인지, 뭐 그런건 중요하지 않고요, 아무튼 가지고 있습니다. 
- 두 가지 뉴럴넷을 설계합니다. 
    - 뉴럴넷 G는 생성하는 놈이구요. 데이터를 읽고, 비슷한 데이터를 생성해냅니다. 
    - 뉴럴넷 A는 분류하는 놈입니다. 
- 이 둘이 막 싸웁니다. 
    - G는 데이터를 읽고 비슷한 데이터를 생성해냅니다. 
    - A는 G가 생성해낸 데이터와 원래 데이터 를 받아서, 이 두가지 종류를 구분합니다.
- 이를 반복하면, G도 똑똑해지고, A도 똑똑해집니다. 생각해보면, 아주 단순한데, 정말 창의적인 생각인 것 같아요. 
- 또한 이는 unsupervised learning입니다. 쓸모가 많다는 이야기겠죠. 일종의 simulation을 하기 위해서도 유용하게 쓰일 수 있을 것 같아요. 

## 

- [이 포스트](https://datascienceschool.net/view-notebook/7788014b90364dd5ba9dc76f35b4cd7d/)를 참고하여 만들었습니다. 

## reference 

- <https://datascienceschool.net/view-notebook/7788014b90364dd5ba9dc76f35b4cd7d/>
- <https://en.wikipedia.org/wiki/Generative_adversarial_network>