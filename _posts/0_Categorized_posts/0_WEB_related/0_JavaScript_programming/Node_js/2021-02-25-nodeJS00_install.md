---
title: nodeJS - install 
category: nodeJS
tags: nodeJS javascript server http web
---

## Node Js - install

- nodeJS는 서버 쪽(백엔드)에서 사용되는 소프트웨어 플랫폼입니다. 그냥 "javascript로 서버를 구축하려면 nodeJS를 사용하면 된다"라고 알고 있어도 문제가 없죠.
- [nodejs.org](https://nodejs.org/ko/download/)에서 node.js를 다운받습니다. 설치하고 확인해 보면 다음과 같은 두 패키지가 설치됩니다.

```plaintext
This package has installed:
    • Node.js v14.16.0 to /usr/local/bin/node
    • npm v6.14.11 to /usr/local/bin/npm
Make sure that /usr/local/bin is in your $PATH.
```

## Run nodeJS

- 이제 nodeJS를 사용해서 아주 간단한 서버를 구축해보도록 하겠습니다.
- 저는 `NodeJS_proj`라는 폴더를 따로 만들고, 내부에 `main.js` 파일을 생성한 다음 다음 코드를 작성해주었습니다.

```javascript
console.log("Hello, nodeJS");
```

- 그리고 다음 커맨트를 실행하면, 결과가 잘 나옵니다. 물론 지금은 nodeJs로 어플리케이션을 만들었다고 하기는 어렵죠.

```plaintext
$ node main.js
Hello, nodeJS
```

### First Application

- 이제 웹브라우저로 접속해 봤을 때, 메세지를 전달해줄 수 있는 서버를 만들어보겠습니다.
- 다음과 같이 작성한 `main.js`를 만들어줍니다.

```javascript
// 필요한 module을 import해줍니다.
// nodeJS는 require를 사용합니다.
var http = require("http");

http.createServer(function (request, response) {
    // createServer는 말 그대로 서버를 하나 만들어주는 것을 말합니다.
    // request, response를 전달받는 function을 인자로 넣어줍니다.
    // @request 는 웹브라우저를 통해 사용자에게서 전달받은 메세지를 말하고
    // @response는 서버에서 웹브라우저로 전달되는 메세지를 말합니다.
    
    // HTTP header를 작성해줍니다.
    // HTTP Status는 OK를 의미하는 200을 넣어주고
    // Content Type은 'text/plain'을 넣어줍니다.
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.write("Hello nodeJS!!")
    response.end();
    // .listen(8085)는 8085포트에서 request를 전달받는다는 것을 의미합니다.
}).listen(8081);

// Console will print the message
console.log('Server running at http://localhost:8081/');
```

- 그리고 다음을 통해 실행한 다음 웹 브라우저를 통해 `http://localhost:8081`에 접속해 보면 `"Hello nodeJS!!"`가 뜨는 것을 알 수 있습니다.

```plaintext
$ node main.js
Server running at http://localhost:8081/
```
