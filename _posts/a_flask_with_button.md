---
title: flask) form 형식을 통해 값을 입력받고 뭔가 출력하기 
category: python-lib 
tags: python python-lib flask html
---

## intro

- 웹 브라우저 상에서 직접 값을 입력받아서 진행하면 좋을 것 같아요. 
- 간단하게 값을 입력받고 그 값만큼의 별을 출력하는 아주 간단한 구조로 진행합니다. 

## http: GET, POST

- 둘다 값을 넘기는 것이니까 어떻게 써도 상관없다고 할 수는 있지만....

- GET, POST의 차이 설명 

- `http://url/aa.html?id=5` 와 같은 방식이 GET, form을 이용해서 submit하는 방식이 보통 post
- GET의 경우 url에 붙어서 쓰이기 때문에 길이에 제한이 있는 반면, POST는 큰 길이의 데이터에 적합(이 경우에도 용량제한은 있다고 함)

- GET의 경우는 해당 url을 사용하여 서버에서 특정한 리소스를 검색하는 경우(select)에 많이 사용되고 
- POST의 경우는 form을 통해 서버로 넘겨진 데이터를 데이터베이스 등에 저장하기 위해서 많이 사용한다. 

- 라고 합니다. 이를 다르게 사용하자면 
    - 게시판에 있는 글을 검색하는 경우 ==> GET
    - 게시판에 글을 쓰는 경우 ==> POST
- 라고 해석하는 것이 좋겠네요. 


- 하나 더. 
- 명확한 URL을 제공하는 것이 필요한가? 로 생각해보면 좋습니다. 
    - 네이버의 검색결과를 링크하는 경우 => get으로 전달하여 url에 표시되는 것이 좋음
    - 글을 작성 완료한 경우 => 글을 쓴 결과 페이지만 보여지면 되므로 url이 따로 필요하지 않음. 

- 즉, 이 두 가지를 잘 구분하여 작성하는 것이 좋다는 이야기입니다. 


## reference

- <http://doorbw.tistory.com/46?category=679147>
- <https://medium.com/wasd/웹-페이지-client-에서-정보-보내기-bf3aff952d3d>
- <https://blog.outsider.ne.kr/312>