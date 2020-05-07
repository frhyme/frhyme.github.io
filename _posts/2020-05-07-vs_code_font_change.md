---
title: VS-code의 font 를 변경합니다.
category: vs-code
tags: vs-code font
---

## Intro

- 사실, 민감하지 않은 사람이라면, 그냥 기본 font를 그대로 써주는 것이 더 좋을 수 있습니다. 다만, 저는 안타깝게도 예민한 사람이죠. 가령, 파워포인트로 뭘 만들 때, 미묘한 정렬이나, 간격등에 예민한 사람이구요. 그리고 그 중에서도 font는 가장 중요합니다. 어떤 심미성뿐만 아니라, 읽기에 좋아야 하거든요.
- vs code는 개발을 위한 IDE이며, 대부분의 프로그래밍 언어들은 영어 알파벳을 기본으로 표현되기 때문에, 굳이 한글 폰트에 대해서는 고려하지 않습니다. 따라서, 그냥 해당 OS의 기본 한글 폰트가 적용되어 있을 가능성이 높죠. 저는 맥북을 쓰고 있기 때문에, 맥북 기본 폰트가 적용되어 있는 것으로 보입니다.
- 다만, 이 글자들은 좀 답답합니다. 대략 아래의 이미지를 보면 뭐가 답답한지 알 수 있는데요, 읽는 것 자체가 답답해서 어려워요. 일반적인 '맑은 고딕'이라거나, '나눔고딕'등에 비해서 위아래가 빽빽해서 가독성이 매우 좋지 못하죠. 특히, 만약 해당 글꼴을 font로 바꾼다면 문제는 더욱 심각해집니다
![apple고딕 from 나무위키](https://w.namu.la/s/0efe0ba7cb3693255e8523190a95bc3a8639e23d99af1a6b838814865664ac86d86752875f730d16c96ca06256d0bc3f76f2db563179d9936c5714fc8c3a48b645851bf5aa56a07aedfbe687a73219e546bffb54e54dacfad4deefe786ded183)
- 따라서, 저는 font를 바꾸기로 결정했습니다.

## VS-code: Change Korean font in file

- 저는 그림을 따와서 넣는 것을 귀찮아하므로 글로 모든 것을 때우겠습니다.
- vs-code를 실행하고, setting(설정)으로 들어갑니다. 단축키로는 `command`+`,`를 사용해도 되죠.
- 들어가서, font를 검색하면 해당 부분으로 들어가게 되죠. 그리고 기본 값으로 다음과 같이 작성되어 있습니다. 그리고 이 아이들은 모두 영어 폰트죠.

```nothing
Menlo, Monaco, 'Courier New', monospace
```

- 저는 다음처럼 이 끝에 한글 폰트인 `NanumGothicCoding`을 집어넣습니다. 앞의 폰트들은 모두 영어 폰트이기 때문에 순서대로 적용되고, 그 이후 한글에 대해서 한글폰트가 적용되는 것이죠.

```nothing
Menlo, Monaco, 'Courier New', monospace, NanumGothicCoding
```

- 당연하지만, 폰트가 우선 현재의 컴퓨터에 설치되어 있는지 파악하는 것이 우선이고, 없다면 설치를 하시면 됩니다.
- 그리고, 맥북 유저라면, spotlight를 켜서 "font"를 입력하여 font들이 설치된 곳으로 간 다음, 원하는 font의 파일명을 가져오셔서 붙여넣으시면 해결되죠.

## wrap-up

- 이렇게 해서 file내, 즉 text-editor에 대해서는 font 종류를 변경할 수 있지만, 왼쪽의 sidebar에 해당하는 부분은 font가 변경되지 않습니다. 사실, 대부분은 오른쪽인 본문만 보면 되니까 큰 문제가 없는데, 저는 중간중간 file이름을 읽을 때도 기본 font는 좀 거슬리거든요. 그래서 왼쪽의 sidebar(혹은 파일 탐색기 부분)에 대해서도 font를 변경할 수 있으면 좋겠다, 라는 생각을 가지고 있습니다.

## reference

- [비주얼 스튜디오 코드(Visual Studio Code) - 폰트 변경](https://recoveryman.tistory.com/385)
- [VS code 한글 font change](https://tttsss77.tistory.com/97)
