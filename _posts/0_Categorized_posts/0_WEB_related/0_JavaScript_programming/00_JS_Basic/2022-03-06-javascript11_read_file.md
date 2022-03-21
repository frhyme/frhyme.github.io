---
title: Javascript - Read File, Dir
category: javascript
tags: javascript file nodejs sync async
---

## Javascript에서 file을 읽는 방법

- local file을 읽기 위한 JS Code는 다음과 같습니다.
- [nodejs - fs](https://nodejs.org/api/fs.html)는 "FileSystem"의 약자이며, File을 읽거나 쓰기 위해서 사용되는 모듈입니다.
- nodejs를 설치했다면 기본적으로 내장되어 있는 모듈이므로 추가로 더 설치할 필요는 없습니다.

```javascript
// CommonJS, ES에 따라 module load방법이 다름.
// CommonJS: require
// ES: import
const fs = require('fs');

// 'utf-8'을 명시하지 않으면 buffer를 출력하므로, 문자형식을 명시할것
fs.readFile('sample.txt', 'utf-8', function(err, data) {
  console.log(data);
})
```

## Javascript 에서 File Directory 읽는 방법

```javascript
var http = require('http');
var fs = require('fs');

var app = http.createServer(function(request, response) {
  fs.readdir('./data/', function(err, files) {
    files.forEach(function(eachFile) {
      console.log(eachFile)
    })
  })
});
app.listen(3000);
```

## Javascript Read file - async

- 만약 file을 순서에 맞춰서(sync)로 출렭하고 싶을 경우에는 `readFileSync` 함수를 사용하면 됩니다.

```javascript
const fs = require('fs');

console.log('Code Start');

// sync 없이 결과를 출력
fs.readFile('./a.txt', 'utf8', function(err, data) {
  console.log(`async: ${data}`);
});

// 위 아래 code의 순서를 맞춰서 결과를 출력
var data = fs.readFileSync('./a.txt', 'utf8');
console.log(`sync: ${data}`);

console.log('Code End');
```

- 위 코드의 실행 결과는 다음과 같습니다.

```plaintext
Code Start
sync: This is a.txt

Code End
async: This is a.txt
```

## Reference

- [nodejs - fs](https://nodejs.org/api/fs.html)
