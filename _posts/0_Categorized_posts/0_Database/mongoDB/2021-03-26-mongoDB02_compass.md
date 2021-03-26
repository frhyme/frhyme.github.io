---
title: mongoDB - Compass
category: mongoDB
tags: database sql nosql mongodb macOS brew 
---

## mongoDB - Compass

- mongoDB를 shell로 접속해서 사용해도 문제 없지만, GUI도 한번 설치해보기로 합니다.
- [mongoDB - download - compass](https://www.mongodb.com/try/download/compass)에서 다운받습니다. 저는 다음 Spec으로 다운받습니다.
  - Version: 1.26.0(Stable)
  - Platform: OS X 64bit(10.10+)
  - Package: dmg
- 다운받아서 설치한 다음, 실행을 시켜보면 String URI format을 집어넣으라고 합니다. 저는 다음 경로에 mongoDB 서버를 띄워줬기 때문에, 아래 경로를 넣어줍니다.

```shell
mongodb://localhost:27017/
```

- 그러고 나면 제가 원하는 mongoDB가 GUI로 잘 떠 있는 것을 알 수 있습니다.

## Wrap-up

- 다만, 문제는 dark mode가 지원되지 않습니다. 눈이 아파요...

## Reference

- [mongoDB - download - compass](https://www.mongodb.com/try/download/compass)
- [mongodb - manual - reference - connection string](https://docs.mongodb.com/manual/reference/connection-string/)
