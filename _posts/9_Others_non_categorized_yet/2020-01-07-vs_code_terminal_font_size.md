---
title: vs code의 terminal font 크기 수정.
category: others
tags: vs-code terminal font-size
---

## intro. 

- 저는 IDE로 vs-code를 쓰고 있습니다. 사실 딱히 큰 불편함을 느끼지는 않았는데, 요즘들어 조금씩 이것저것 적용하면서 개선해보려고 하고 있어요. 
- 우선, 모니터의 상부와 하부를 분할하여, 위는 python code로 아래는 terminal로 쓰는 중에, terminal의 font size가 너무 크게 느껴지는 것이죠. 저는 또 맥북 프로를 쓰기 때문에 화면의 크기가 작아서, 폰트를 좀 줄이면 좋을 것 같더군요. 

## how to reduce your font-size

- vs code에서 `commnad`+`p`를 누르고, `settings.json`으로 들어갑니다. 이는 사용자 설정으로 들어가겠다는 말이죠. 혹은 `command`+ `,`를 누르면 바로 설정으로 들어가게 됩니다.
- 들어가서 보면, 해당 창 부분이 왼쪽과 오른쪽으로 구분되는 것을 알 수 있습니다. 왼쪽은 '초기 설정(default)'을 말하고, 오른쪽은 '사용자 설정'을 말하죠
- 왼쪽에는 변경 할 수있는 설정등의 목록이 나옵니다. 저는 터미널을 바꿔야 하므로, 터미널을 눌러주죠.
- 죽 내려보면, `font-size`라는 코드가 있는 것을 알 수 있는데요, 이 부분을 누르고, 사용자 설정으로 복사해줍니다.
- 그리고 원하는 크기의 사이즈를 입력하죠.

## wrap-up

- 당연하지만, 가능하다면, 너무 지나친 커스토마이징을 하시지 않기를 추천드립니다. 늘 그렇듯이, 순정이 좋은 거에요.

## reference

- [Vs code 환경설정 및 기본 사용법](https://gwonsungjun.github.io/articles/2018-06/vscodeSetting)