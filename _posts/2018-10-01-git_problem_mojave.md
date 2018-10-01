---
title: 맥의 새 OS mojave를 설치했더니, git은 인식하지 못합니다. 
category: others
tags: macOS mojave git 
---

## intro

- 지난 주말에는 [mac의 새 OS인 Mojave](https://namu.wiki/w/macOS/%EB%B2%84%EC%A0%84#s-18)를 설치했씁니다. 
- 사실 아직은 뭐가 좋은지 잘 모르겠어요 하하핫. 
- 좀 더 섹시해보여서 다크모드로 해놓고 있기는 한데, 이걸 꼭 해야만 하는지도 사실 모르겠고. 그렇습니다. 
    - 스크린샷을 처리하는게 좀 더 편하기는 한 것 같고(스크린 샷을 찍자마자 맥에서 편집할 수 있으니까요)
    - 아이폰에서 사진을 찍으면 바로 맥에서 처리할 수 있다 정도
- 가 다 인 것 같아요. 

## 중요한 건.

- 사실 중요한 건 이게 아니고. 
- 업데이트 이후에 git이 인식이 안되더군요. 
- 평소처럼 아래 커맨드를 사용했는데 그 결과는 아래와 같습니다. 

```bash
git status
```

```bash
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

- 뭐라는지 모르겠으니, 이럴 때는 그냥 해당 코드를 그대로 구글에 치면 보통 해결 방법이 나옵니다 하하핫. 

- 쳐보니까, [이 블로그에서 해결방법을 찾았습니다](http://redutan.github.io/2015/10/05/osx-after-update-git-error).

- Xcode를 재설치하면 된다고 하는데, 해당 블로그에서는 그저 커맨드라인툴만 설치했다고 합니다. 
- 즉, 아래 명령어를 치면 뭔가를 설치해야 하는데, 설치하고 나면 잘 됩니다. 

```bash
xcode-select --install
```

## wrap-up

- 저는 xcode를 안 쓰는데, xcode가 뭘까요. 하하핫. 

## reference

- <http://redutan.github.io/2015/10/05/osx-after-update-git-error>