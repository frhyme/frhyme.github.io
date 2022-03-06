---
title: Javascript - url parsing
category: javascript
tags: javascript url html http nodejs
---

## Javascript - url parsing

- Javascript에서 http 모듈을 사용하여 http request를 처리할 수 있는 웹 서버를 하나 만들고, request에서 url 부분만을 쪼개어 parsing하는 코드를 다음과 같이 정리하였습니다.

```javascript
// 아래 URL로 접속했습니다.
// http://localhost:3000/?id=css
var http = require('http');
var url = require('url');

var app = http.createServer(function(request, response) {
  /*
  request에는 http 프로토콜에 의해 들어오는 모든 정보가 담김.
  */
  var _url = request.url;
  console.log("= request");
  console.log(request);

  console.log('= request.url')
  console.log(request.url);
  /*
  /?id=css
  */

  console.log('= url.parse(_url, true)');
  console.log(url.parse(_url, true));
  /*
  Url {
    protocol: null,
    slashes: null,
    auth: null,
    host: null,
    port: null,
    hostname: null,
    hash: null,
    search: '?id=css',
    query: [Object: null prototype] { id: 'css' },
    pathname: '/',
    path: '/?id=css',
    href: '/?id=css'
  }
  */
});
app.listen(3000);
```
