---
title: Github - 이전 commit에서 잘못 작성된 author 변경하기.
category: git
tags: git github 
---

## Intro - 왜 commit log에 author가 잘못 작성되었는가

- 얼마전 새 맥북을 샀습니다. 계속 말하는 것 같기는 하지만, 이전 맥북은 2015년(early)년형 맥북에어였고, 지금 쓰는 맥북은 2020년 형 맥북에어입니다. 일단 레티나 디스플레이라는 점에서 아주 큰 감동이 밀려오죠.
- 아무튼, 중요한 건 맥북을 사고 대략 세팅을 끝내고 나서 주요 github repository를 `git clone`으로 간단하게 가져온 다음에 `git commit`을 몇 개 날렸습니다. 그런데, 자세히 살펴보니 `git commit`을 남길 때마다, 다음과 같은 메세지가 터미널에서 뜨는 것이죠.

```plaintext
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

- 뭐 일단 망한 건 망한거고 현재 맥북에서 작성되는 모든 git commit의 작성자(author)를 제 이메일로 세팅해줍니다. 이렇게 하고 나면, 이후의 제 컴퓨터에서 발생하는 모든 commit은 제 이메일로 저장되죠.

```bash
git config --global user.email "email@example.com"
```

- 다만, 이렇게 한다고 해서 이전 commit의 author들이 바뀌는 것은 아닙니다. 이 설정 이후에 발생하는 모든 commit의 author가 지금 지정한 email로 설정된다는 이야기죠.
- 뿐만 아니라, 저는 push까지 했기 때문에 git commit history를 다 뜯어고쳐줘야 하는 상황이니까요.

## Git rebase

- 이미 commit되어 push까지 완료된 commit history를 고치기 위해서는 `git rebase`를 사용해야 합니다. 다만, 우선 `git rebase`가 무엇이며 무엇을 위해서 사용하는 것이 필요한지 정리해야겠죠.
- `Git rebase`는 보통 과거에 만든 commit을 수정하는 목적으로 자주 사용됩니다.
- `git commit --amend`가 현재의 commit만을 수정할 수 있다면, `git rebase`는 과거의 commit으로 돌아가서 해당 commit만을 수정함으로써 commit history를 깔끔하게 관리할 수 있다는 것이죠.
- 찾다보니 [이 링크에서](https://suhwan.dev/2018/01/27/Git-Rebase-2/) 매우 자세하게 나와 있는 것을 확인하였습니다. 이보다 잘 쓰기는 어려울 것 같아서, 해당 내용을 요약하는 선상에서 아래에서 정리하였습니다.

### Git rebase를 이용하여, 이전 commit author를 변경

- 우선 아래 명령어를 사용하여 git rebase를 실행합니다.
  - 우선 rebase는 `<돌아갈 commit의 hash>`로 돌아가서, 거기서부터 이후 반영될 commit을 모두 일일이 확인하면서 고칠지 안 고칠지를 판단하며 넘어가는 것을 말합니다. 따라서, 유효하다고 판단되는(혹은 고칠 필요가 없는 마지막) commit의 해쉬번호를 사용해야 하구요.
  - `-i`는 "interactive mode"를 실행하는 것을 말합니다. 위에서 보듯 하나씩 체크하면서 넘어가므로 상호작용모드를 사용하죠.

```bash
git rebase -i <돌아갈 commit의 hash>
```

- 실행하고 나면 갑자기 vim 창이 뜹니다. 무슨 말인가 싶지 잘 보면 제일 위에는 유효한 커밋 이후에 뜬 모든 commit이 뜨고 `pick`이라는 글자들이 공통적으로 작성되어 있죠. 아래에는 사용할 수 있는 몇 가지 커맨드들이 있습니다.
  - `pick`: "해당 commit을 그대로 사용하겠다"라는 의미입니다.
  - `reword`: "commit message를 변경한다"라는 의미입니다.
  - `edit`: "commit의 내용, 변경 내용을 바꾼다"라는 의미입니다. 즉, 해당 commit으로 인해 변경된 내용 자체를 다르게 변형해준다는 이야기죠.
- 그 외로 이전 commit들과 합친다거나 하는 명령어들도 있지만, 굳이 필요하지는 않을 것 같아서 여기서는 그냥 넘어갑니다. 자세한 내용은 [이 링크](https://jupiny.com/2018/05/07/git-rebase-i-option/)에서 확인할 수 있습니다. 또한, commit의 순서를 다르게 적용하고 싶다면 이 아이들의 위치를 다르게 작성해주면 되는 것이죠.
- 따라서, 각 commit에 대해서 변경할지 어떻게 할지를 죽 적용해주면 됩니다. 유효하다면 `pick`을 두고, 내용을 바꾼다면 `edit`이 되겠죠. 여기서, author를 변경하기 위해서는 각 commit에 대해서 `edit`을 적용해줘야 합니다.
- 대상 commit, 즉 저자가 잘못 작성된 commit에 대해서 모두 `edit`을 사용해준 다음 `:wq`를 통해 vim을 빠져 나옵니다.
- 그러고 나면 다음의 메세지가 뜨죠. 이 아이는 제가 `edit`을 해준 commit이고 여기서 고칠 거냐 아니면 만족하니까 다음으로 넘어갈 것 이냐고 묻는 것을 말합니다.

```plaintext
Stopped at 41abb21... WRITE: set new macbook setting
You can amend the commit now, with

    git commit --amend

Once you are satisfied with your changes, run

    git rebase --continue
```

- 저는 author를 바꿔줘야 하니까 다음의 명령어를 실행해줍니다. 이렇게 하고 나면 현재의 commit의 author를 바꾸게 되는 것이죠.

```bash
git commit --amend --author="Seunghoon Lee <freerhein@gmail.com>"
```

- 그리고 현재의 commit을 수정했고 문제가 없으므로 다음으로 넘어가기 위해 다음 명령어를 실행해줍니다.

```bash
git rebase --continue
```

- 이를 반복하면 됩니다. 다시 정리하자면, 다음과 같죠.
  - 유효한 마지막 commit으로 이동한다.
  - 이후 이동한 commit부터 최신 commit까지 중에서 고쳐야 하는 아이들은 `edit`으로 바꿔준다.
  - commit들을 하나씩 훑어 가면서 변경해야 하면 변경해주고 아니면 그냥 넘어가준다.

- 그리고 만약 저처럼 local에서 원격으로 push까지 해버린 경우에는 다음으로 강제로 푸쉬를 해줘버립니다.

```bash
git push origin +master
```

## wrap-up

- 솔직히 말하자면, 지금 글을 쓴대로 진행을 했었어야 했는데, 저는 급하다고 마구잡이로 해서 commit들이 좀 꼬여 있는 상황입니다. 뭐 하지만 어쩔 수 없죠. 귀찮으므로 그냥 무시하기로 했습니다.
- 그래도, 이글을 쓰면서 `git rebase`가 어떤 역할을 하는지에 대해서 이해했으니 된거죠 뭐 호호.

## reference

- [git commit author 변경 (커밋 작성자 이름 변경하기)](https://madplay.github.io/post/change-git-author-name)
- [Git Rebase (2)](https://suhwan.dev/2018/01/27/Git-Rebase-2/)
- [git rebase -i 사용하기](https://jupiny.com/2018/05/07/git-rebase-i-option/)
