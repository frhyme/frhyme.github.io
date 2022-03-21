---
title: Lua 01 - Install Lua
category: lua
tags: lua programming
---

## Intro

- 최근에 vim 에서 ESC키를 눌렀을 경우 자동으로 영어로 전환되로록 하기 위해서 Hammerspoon이라는 아이를 사용했습니다. Hammerspoon은 Lua라는 스크립트 언어를 통해 macOS의 API를 사용할 수 있도록 해주는 아이였죠.
- 그래서 하는 김에 lua를 조금 공부해보기로 했습니다.
- 일단 설치부터 해줍니다.

```bash
curl -R -O http://www.lua.org/ftp/lua-5.4.3.tar.gz
tar zxf lua-5.4.3.tar.gz
cd lua-5.4.3
make all test
sudo make install
```

- 위처럼 설치를 하고 나면, command line에서 `lua`를 실행해서 interactive mode로 실행할 수도 있고, `lua a.lua`를 통해 코드를 실행할 수도 있습니다.

## 눈에 띄는 몇 가지 특징

- [learn lua in y minutes](https://learnxinyminutes.com/docs/lua/)에 lua를 사용하는 방법이 간단하게 나와 있습니다. 일단 대충 눈에 띄는 특징들을 정리하면 다음과 같습니다.
  1. 숫자는 그냥 double type 하나만 존재하는 것 같습니다.
  2. 대부분의 명령어를 끝낼 때, `end`를 붙이는 것 같네요.
  3. comment 를 쓰는 방식이 조금 특이하네요.
  4. function 내에서 새로운 function을 만들어서 리턴하는 것이 가능하고(closure), anonymous function도 존재합니다.
  5. `local`을 사용해서 지역 변수를 각각 설정할 수 있는 것으로 보입니다. 
  6. python의 dictionary와 유사한 자료구조가 존재합니다.

## Wrap-up

- 그 외에도 몇 가지가 더 있는 것 같기는 하지만, 오늘은 처음이므로 이정도만 정리하겠습니다.

## reference

- [lua programming language](https://www.lua.org/)
