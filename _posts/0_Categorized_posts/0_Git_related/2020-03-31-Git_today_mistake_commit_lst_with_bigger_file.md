---
title: 오늘의 Git 실수 - Local에서 Commit을 했는데 파일 용량이 커서 push를 할 수 없다!!
category: others
tags: git git-commit git-reset 
---

## Background: 갑자기 local에 있는 많은 것들을 git에 올리고 있습니다

- 원래는 대부분의 자료들을 그냥 local에 두었는데, 요즘에는 대부분을 git에 올리고 있습니다. 
- 프로젝트로 진행을 했다면 프로젝트 폴더로 나누어서 올리고, 혹은 좀 scratch처럼 쓰는 폴더라도 올려두기로 했습니다. 
- 이유는 우선 "github이 private을 지원한다는 것"이고, 두번째로는 "내가 코딩하는 양을 좀 더 정확하게 정리하기 위해서"죠. 
- 저는 대부분의 github을 그냥 블로그 글을 올리는데 쓰기는 그 글을 쓰기 위해서 발버둥치는 노력들이 있거든요. 그 부분이 뭔가 그냥 없어지는 것 같아서, 다 github에 private으로 올려서 관리해보기로 했습니다. 
- 그리고, 지금 쓰는 글은 그 과정에서 발생한 아주 빡치는 일이죠. 

## I'm Git 초보

- 네, 저는 git 초보입니다. 대부분 혼자 코딩을 하니까, 협업으로 인해 발생하는 문제를 거의 인지하지 못하고, 보통은 그냥 다음의 과정이 다죠 

```bash 
git status 
git add .
git commit -m 'write posts'
git push origin master
```

- `git pull`을 써본적은 진짜 손을 꼽습니다. 가끔 실수로, 웹에서 마크다운 파일들을 직접 변경한 경우, 그런 경우에만 종종 쓰는게 다죠. 사실 결국 그냥 클라우드 쓰듯이 쓰는 겁니다. 

## 아무튼 폴더를 git의 관리하에 둡니다

- 우선, github에서 새로운 repository를 만들어 줍니다. 
- 그리고, 그 repository를 clone으로 가져와서 local에 새로운 folder를 만들어줍니다. 

```plaintext
git clone ~~
```

- 그리고, 이전에 쓰던 local의 folder에 있던 파일들을 이 폴더로 모두 가져옵니다. 
- 그리고 다시 다음을 수행하죠 

```git 
git status
git add .
git commit -m 'write posts'
git push origin master 
```

- 그런데, 갑자기, `git push origin master` 에서 문제가 발생합니다. 에러는 다음과 같죠. 
- 용량이 넘어서, 안된다, 라는 이야기죠. 뭐 그럴 수 있죠. 그럼 그냥 해당 파일을 `.gitignore`에 등록해주면 됩니다.

```plaintext
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: error: File Gensim/GoogleNews-vectors-negative300-SLIM.bin is 345.25 MB; this exceeds GitHub's file size limit of 100.00 MB
```

- 따라서, `.gitignore`를 만들고, 저는 지금 `.bin`파일이 문제이므로 얘네를 그냥 통으로 모두 제외합니다.
- 중간에 갑자기 `.gitignore`를 추가해준 것이므로 다음을 순차적으로 수행해줍니다. 

```plaintext
git rm -r --cached .
git add .
git commit -m 'UPDATE gitignore and EXCLUDE them'
git push origin master
```

- 이제 끝나야 하지만, 여전히 끝나지 않습니다. 아까와 똑같이, 용량이 초과되었다면서 더 진행되지 않더군요. 
- 이 단계에서, 저는 제가 뭔가 실수한 줄 알고 `.gitignore`를 바꾸었는데, 사실은 그 문제가 아니었죠. 

## Commit은 되었지만, 용량 제한을 넘겼으므로, push는 안된다

- 아까 보셨지만, 처음부터 이미 **commit**은 되었습니다. 
- 순서대로 보면, `git add`를 통해 관리해야 하는 파일들을 추가해주고, 그 다음 `git commit`을 통해 현재 파일들에 대해 커밋을 넘기죠. 여기까지는 아무 문제가 없습니다. 아니, 정확하게는 문제가 있지만 문제가 발견되지 못합니다. 100MB가 넘는 줄 여기서는 모르니까요. 
- 그리고, `git push origin master`를 합니다. 그럼, local에서 만들어진 commit list를 origin으로 보내겠죠. 보내는데, 보내면서 체크해보니, 제한 용량을 넘는 파일이 있습니다. 그럼, 여기서 아까의 에러가 발생합니다. 용량이 넘으니까, `remove:error`가 발생하죠. 
- 즉, 이미 **발생한 commit**을 remote로 넘길 수가 없다는 겁니다. commit 자체가 잘못되었다는 이야기죠. 
- `git push`라는 것은 local에서 발생한 commit list를 한번에 remote로 넘겨준다는 것인데, 이미 commit(완료)에 등록된 파일은 바꿀 수 없습니다. `.gitignore`를 등록하거나 해도 뭐 될 수가 없는 거에요. 

## git reset

- 네. 그래서 우선 `git log`를 쳐보니, `commit`이 이미 여러 번 발생했씁니다. 다 필요업는 것들이죠. 
- 따라서, `git reset`을 통해 제일 처음의 상태로 돌아갑니다. 

```plaintext
git reset COMMIT_NAME
```

## wrap-up

- 용량이 100MB가 넘으면 push되지 않습니다. 
- 그리고, 이미 commit이 되었다면 commit을 되돌리는 수밖에는 방법이 없어요 흐헝ㅇ
