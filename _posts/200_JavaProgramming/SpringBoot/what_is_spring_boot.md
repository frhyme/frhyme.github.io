---
title: Spring Framework and Spring Boot
category: java
tags: java spring programming framework
---

## Spring Framework and Spring Boot

- Spring Framework는 자바 진영에서 가장 인기있는 어플리케이션 개발 프레임워크입니다. 하지만 Spring Batch처럼 Spring Framework를 사용해서 만들어진 새로운 Framework도 있기 때문에, 오히려 스프링은 단순한 프레임워크라기보다는 meta-Framework라고 불러도 될것 같습니다.
- 스프링의 주요 특징은 다음과 같습니다. 즉, 무엇이든 만들 수 있도록 모든 요소가 다 존재한다고 생각하면 됩니다.
  - 어플리케이션 내에서 Object의 Life-Cycle을 관리할 수 있는 Component contaiiner
  - 다양한 DataBase와 연동될 수 있는 data access framework
  - 사용자의 authentication, authorization을 지원하는 security framework
  - 어플리케이션의 모든 파트에 대해서 test할 수 있는 Testing framework
- 이렇게 보면 Spring이 정말 좋아 보이지만, 사실 저는 Spring을 제대로 사용해본 적이 없습니다. 익숙해지면 매우 활용도가 높은 프레임워크라고 하지만 그 프레임워크 뒤에는 다양한 디자인 패턴들과 Convention 들이 숨어 있어서 초심자가 접근하기에는 너무 복잡합니다. 어디서부터 어떻게 설정하고 코드를 어떻게 나누어서 작성해야 하는지에 대해서 전혀 감이 없죠. 
- 따라서, Spring Framework는 좀 더 경량화한 버전인, Spring Boot를 만들었습니다. 이 프레임워크는 기존의 번거로운 설정 작업을 삭제해주고 좀 더 편한 개발 환경을 만들어줬죠.




## Wrap-up

- 과거의 저는 박사 논문에서 제시한 방법론을 검증하기 위해서 웹 어플리케이션을 만드는 일이 필요했었죠. 그래서 찾아보다가 Spring으로 개발하려고 했으나 너무 복잡해서 멈췄고 python으로 넘어왓 django와 flask 중에서 거의 프레임워크 라는 것 자체가 없다시피 한, flask로 개발을 했었습니다. 하지만 이 아이는 너무 경령화되어 있어서 정신을 놓고 코딩을 하기 시작하면 스파게티코드가 되죠. 정말...한 달만 지나도 이게 무슨 코드인지 읽으면서도 정신 못차리죠 호호. 
- 특히, 