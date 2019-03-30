---
title: onclick을 이용하기 
category: others
tags: javascript html 
---

## 아주 간단합니다. 

- 그냥 html의 특정 부분을 눌렀을때, 어떤 javascript요소가 수행되도록 하려면 그냥 `onclick`을 설정해주면 됩니다. 
- 기본적으로는 `button`에 대해서만 가능한 것 같지만, `a`도, `div`도 어떤 html 요소든 모두 가능하죠. 
- 다음처럼 해주면 됩니다 

```html 
<button onclick="myFunction()">Click me</button>
```

- 여기서 `myFunction`은 해당 html 파일의 script 부분에 포함되어 있는 것이 좋겠죠. 


## wrap-up

- 원래는 페이지의 내용을 바꿔야 할때, `a` 태그를 사용해서 새로운 페이지로 전달해주는 방식으로 수행했습니다. 
- 그러나, 여기서처럼 클릭시에 동작해야 하는 것들을 정의해주게 되면, 새로운 html 파일을 만들고 해당 파일로 전달되도록 하지 않아도, javascript를 이용해서 특정한 부분을 변경해서 진행할 수 있습니다 
- 아 javascript를 사용해보니까 아주 편한 부분이 많군요 하하하.