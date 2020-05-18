---
title: Github - author 변경 
category: git
tags: git github 
---

## Intro

- 새 맥북을 샀습니다. 맥북을 새로 사서 하나하나 세팅해주는거 매우 성가시죠. 거의 다 끝냈다고 생각했는데, 오늘 보니, github에 문제가 하나 있더군요. 그냥 이전에 쓰던 repository를 `git clone`으로 가져오고, ID/PW를 세팅하고 commit을 날렸는데, commit 기록에 author의 이름이 제 ID가 아닌 제 이름이 남겨져 있습니다.
- 꼼꼼히 보니, commit을 남기면 다음과 같은 기록이 뜨더군요.

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

- 번역하자면, "니 이름과 email은 너의 username과 hostname에 의해서 자동으로 설정되었다. 걔네가 정확한지, 확인해라. 니 identity를 수정하고 싶으면 아래 부분을 진행해라"라는 말이죠. 흠. 귀찮아지는군요.




- 일단 제 이메일을 gloabl로 세팅해줍니다. 이렇게 하고 나면, 이후의 제 컴퓨터에서 발생하는 모든 commit은 제 이메일로 진행되게 되죠.

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