---
title: python - Django - Include Static files
category: python
tags: python programming django web backend server css 
---

## python - Django - Include Static files

- css, javascript, image와 같은 static 파일들을 Django 프로젝트 내에 집어넣기 위해서는 다음의 과정을 따르면 됩니다.
- 우선, `DjangoProj1 > App1 > templates > App1 > base.html`에서 static css file을 집어넣어주려고 합니다.
- head 부분에 다음의 부분을 넣어줍니다. 

```html
<!-- static 경로에 있는 파일들을 가져온다. -->
{% raw %}{% load static %}{% endraw %}
<!-- static 경로 아래의 css/base.css 파일을 가져온다. -->
<link rel="stylesheet" href="{% raw %}{% static 'css/base.css' %}{% endraw %}">
```

- 그리고 `base.css` 파일을 만들어 줍니다. 저는 `DjangoProj1 > staticFolderName > css > base.css`에 만들어 줍니다.
- 여기서, 저는 이해를 위해 `staticFolderName`이라는 이름을 붙였지만 보통은 그냥 "static"을 사용합니다.

```css
/* base.css */
h2 {
  font-size: 100px;
  color: red;
}
```

- 그리고, `DjangoProj1 > DjangoProj1 > settings.py`에 아래 내용을 추가해줍니다.

```python
STATIC_URL = '/staticFolderName/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticFolderName")]
```

- 그 다음 서버를 구동해서 확인해보면 CSS 가 잘 적용되어 있는 것을 알 수 있습니다.

```plaintext
python manage.py runserver    
```
