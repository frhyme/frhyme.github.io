---
title: python requests - 403 Forbidden because of User agent
category: python
tags: python requests
---

## python requests - 403 Forbidden because of User agent

### Problem

- python requests package 를 사용해서 웹 크롤링을 할 때, 웹브라우저에서는 잘 보이는 문서가, requests 로 가져올 때는 403 forbidden이 발생하는 경우가 있습니다. code는 간단히 다음과 같죠.

```python
import requests

if __name__ == '__main__':
    target_url = "https://url"

    headers = {}
    response = requests.get(target_url, headers=headers)

    print(response.content)
```

- 웹브라우저에서는 문제없이 해당 url에 접속이 되지만, requests를 사용할 경우, 다음처럼 Forbidden 문서가 읽히는 경우가 있습니다.

```html
<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

### Solution

- `requests.get()`에 header 내에 'User-Agent'를 넘겨주면 해결됩니다.
- User-Agent는 [what is mybrowser - detect - what is my user agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)에서 확인할 수 있습니다.

```python
import requests

if __name__ == '__main__':
    target_url = "https://url"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    response = requests.get(target_url, headers=headers)

    print(response.content)
```

### Background

- User-Agent 는 http 요청을 보내는 디바이스 와 브라우저에 대한 정보를 의미합니다. 요청자가 PC인지 혹은 휴대폰인지에 따라서 만약 다른 response를 보내줘야 한다면, 이 User-Agent 값을 참고할 수 있는 것이죠.
- 제가 접속한 웹 서버는 nginx를 웹서버로 사용하는 것으로 보이며, User-Agent 값이 header에 포함되어 있지 않을 경우에는 해당 URL에 접속할 수 없도록 설정되어 있는 것으로 보입니다. 그래서, 접속이 안됨 셈이죠.

## wrap-up

- 이전에는 web crawaling을 위해 selenium을 사용했습니다. selenium의 경우 실제 사람이 브라우저를 사용하는 것처럼 detail한 동작을 제어할 수 있다는 장점이 있습니다. 그러나 속도가 느리고 코드가 복잡해진다는 단점이 있죠. python 외부에서 gecko driver라는 브라우저를 사용해서 리소스도 꽤 잡아먹는 단점이 있습니다. 다만, selenium의 경우는 requests처럼 403 forbidden이 발생하지는 않았습니다. 아마 사이에서 실제 브라우저처럼 돌아가는 것처럼 보이니 웹서버가 block을 하지 못한 것으로 생각되네요.
- 반대로, request는 훨씬 간단한 모듈이지만, 잘못하면 대상 웹서버 단에서 block을 먹일 수도 있는 것으로 보입니다. 이건 웹 크롤링할 때, 항상 조심해야 되는 이슈이기는 하지만 대상 서버에 무리가 되지 않도록 또 그로 인해 제가 블록을 먹는 일이 없도록 조심해서 개발해야 할 것으로 보입니다.

## Reference

- [stackoverflow - python requests 403 forbidden](https://stackoverflow.com/questions/38489386/python-requests-403-forbidden)
- [what is mybrowser - detect - what is my user agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)
- [User-agent 정확하게 해석하기](https://velog.io/@ggong/User-agent-%EC%A0%95%ED%99%95%ED%95%98%EA%B2%8C-%ED%95%B4%EC%84%9D%ED%95%98%EA%B8%B0)
