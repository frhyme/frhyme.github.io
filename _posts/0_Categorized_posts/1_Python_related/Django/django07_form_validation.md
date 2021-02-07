---
title: python - Django - Form, Validation
category: python
tags: python programming django backend server form
---

## python - Django - Form, Validation

- 보통 html에서 form 요소를 작성할 때는 다음과 같이 작성합니다.
- 간단한 input의 경우는 다음처럼 작성해도 아무 문제가 없습니다만, input이 여러 개이거나, 잘못된 input에 대해서 백엔드에서 프론트엔드로 메세지를 전달해주기 위해서도, front-end단보다 backend에서 처리해주는 것이 더 좋을 때가 있죠.

```html
<form action="/submitResult" method="post">
    <label>param1</label>
    <input name="param1Name">
    <button type="submit">Submit</button>
</form>
```