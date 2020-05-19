---
title: Github - 이전 commit에서 잘못 작성된 author 변경하기.
category: git
tags: git github 
---

## Intro - 왜 commit log에 author가 잘못 작성되었는가

- 얼마전 새 맥북을 샀습니다. 계속 말하는 것 같기는 하지만, 이전 맥북은 2015년(early)년형 맥북에어였고, 지금 쓰는 맥북은 2020년 형 맥북에어입니다. 일단 레티나 디스플레이라는 점에서 아주 큰 감동이 밀려오죠.
- 아무튼, 중요한 건 맥북을 사고 대략 세팅을 끝내고 나서 주요 github repository를 `git clone`으로 간단하게 가져온 다음에 `git commit`을 몇 개 날렸습니다. 그런데, 자세히 살펴보니 `git commit`을 남길 때마다, 다음과 같은 메세지가 터미널에서 뜨는 것이죠.

```code
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

```

- 번역하자면, **"니 이름과 email은 너의 username과 hostname에 의해서 자동으로 설정되었다. 걔네가 정확한지, 확인해라. 니 identity를 수정하고 싶으면 수정해라"**라는 말이죠.
- 만약, 저 메세지가 떴다면 아직 회생의 여지가 있습니다. commit은 했으나 아직 원격 저장소에 보내진 상황은 아니고(즉, local에 있는 상황이고), 따라서 local내에서 수정한 다음 보내면 되죠. local에서 수정하는 방법은 다음과 같습니다.

```bash
git commit --maned --reset-author
```

- 그러나 매우 안타깝게도 저는 이미 별 생각없이 원격 저장소로 push한 상황입니다. 네, 존나 귀찮아진다는 이야기죠.

## Set global e-mail

- 뭐 일단 망한 건 망한거고 현재 맥북에서 작성되는 모든 git commit의 작성자(author)를 제 이메일로 세팅해줍니다. 이렇게 하고 나면, 이후의 제 컴퓨터에서 발생하는 모든 commit은 제 이메일로 진행되게 되죠.

```bash
git config --global user.email "email@example.com"
```

- 다만, 이렇게 한다고 해서 이전 commit의 author들이 바뀌는 것은 아닙니다. 심지어 저는 commit을 했을 뿐만 아니라, push까지 했기 때문에, 좀 난감해진 상황이죠. 다행히 관련 내용을 올려두신 분이 있습니다.
- [git commit author 변경 (커밋 작성자 이름 변경하기)](https://madplay.github.io/post/change-git-author-name)을 참고하여 아래의 내용들을 진행하였습니다.

- 우선 `git log`를 통해 이전 commit의 로그들을 확인합니다. 확인해보면 몇몇 commit의 경우 아래와 같이, Author가 다르게 적용되어 있는 것을 알 수 있죠.

```
Author: seunghoon Lee <seunghoonlee@seunghoonui-MacBookAir.local>
```


```
git log
```


나머지는 이후에 진행하자!!

다 진행했음. 아래의 방법대로 하면 다 되는데, 이제 왜 되는건지에 대해서만 정리하면 됨. 

https://madplay.github.io/post/change-git-author-name


## wrap-up

- 다만, 지금 commit이 좀 꼬여있기는 함. 문제가 좀 있는데 그 원인에 대해서도 분석해서 정리하는 것이 필요함.