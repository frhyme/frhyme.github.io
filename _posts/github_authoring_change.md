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
- 

- 일단 제 이메일을 gloabl로 세팅해줍니다.

```bash
$ git config --global user.email "email@example.com"
```

