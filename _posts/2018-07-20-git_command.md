---
title: git command를 정리해봅시다. 
category: others
tags: git shell basic
---

## intro 

- 최근에 git repository에 문제가 생겼어요. related post를 잘 사용하려고 몇 가지 시도를 했는데, 그 결과로 블로그가 정말 너무 느려지는 상황이 발생했습니다. 
- 뭔가, 전부 뜯어고쳐야 할 것 같은데 전에 만들어둔 부분들이 날아갈까봐 조심스러운거에요. 
- 그래서 git을 좀 잘 이용하면 이걸 잘 할 수 있지 않을까? 라는 생각을 해봤습니다. 하핫

## 현재 나는 git command를 어떻게 쓰는가? 

- `git status`: 현재 스테이징, 커밋 되지 않은 파일들이 있는지 확인
- `git add .`: 현재 폴더에 있는 모든 파일들 관리대상으로 집어넣기(관리대상으로 집어넣지 않으면 git commit을 날려도 commit에 포함되지 못함)
- `git commit -m <msg>`: msg라는 명으로 커밋 날리기. 
- `git push origin master`: ...
- `git clone <github url>`: `git clone`을 통해 repository를 통째로 복사해와야 git push, pull 등을 할때 문제없이 잘됨. 

- 아마도 나 이외에도 많은 사람들이 이러한 형태로 간단한 레벨로만 사용하지 않을까? 

## git을 좀 더 잘 써보자. 

- `git remote add origin <remote repository url>`: 
    - `origin`을 등록해줍니다. 
    - git은 기본적으로 local, origin으로 구분되고, local에 있는 것을 오리진으로 보내거나(push), 오리진에 있는 것을 로컬로 가져오거나(pull) 의 행위로 나뉩니다. 
    - 일단은 local repository별로 origin은 단 하나만 있다, 라고 생각하는 것이 좋습니다. 

- `git push origin master`: 
    - 따라서, 위 코드는 현재 repository를 제가 등록해둔 `origin` 에 master branch로 넘기는 것을 의미합니다. 
    - 만약, 다른 branch에 push하거나, 새로운 branch를 만들 경우에는 master 부분을 변경해주면 좋습니다. 

### branching

- 저는 귀찮아서 매번 master branch에서 모두 작업했는데요, 최근에 뭔가를 새로 세팅하다가 문제가 생겨서 한참 고생했던 기억이 있습니다. 
- 다음부터는 가능하면 branching을 해서 테스트해보고 돌리면 좋을 것 같아요. 

- `git checkout -b <branch_name>`:
    - `branch_name`를 가진 가지를 만들어 주고 그 브랜치로 들어갑니다. 
- `git checkout -d <branch_name>`: 
    - `branch_name`를 가진 가지를 삭제해줍니다. 
- `git checkout master`:
    - 마스터 브랜치로 들어옵니다. 이런식으로 체크아웃은 현재 브랜치에서 나가서 다른 브랜치로 들어가는 것을 의미합니다. 

### pulling

- 저의 경우는 혼자 작업을 합니다. 맥북에서 작업을 하고, 어느 정도 된 것 같으면 그냥 `git push origin master`를 통해 오리진에 있는 마스터 브랜치로 넘겨버리죠. 제 맥북이 `git push`를 날리는 유일한 컴퓨터라서, pulling을 할 일이 별로 없습니다. 
- 다만, 제가 맥북으로도 작업하고, 데스크톱으로도 작업할 경우에는 양쪽에서 서로 `git push`를 날리는 일이 발생할 수 있습니다.
- 만약 다음 순서대로 일이 발생했다면
    1. 맥북에서 작업후 `git push origin master`
    2. 데스크톱에서 작업 후 `git push origin master`

- 현재 맥북의 로컬 리포지토리에 있는 내용은 up-to-date가 아닙니다. 따라서 이 경우에는 `git pull origin master`를 통해서 원격 서버에 있는 내용을 가져오는 것이 필요하죠. 

### merging 

- 자, 이제 로컬에서 여러 브랜치를 동시에 가지고 있다고 가정합니다. 개별 브랜치는 서로 다른 파일들을 가지고 있게 되고요. 

- `git merge <branch_name>`: 현재 작업 중인 브랜치에 branch_name 라는 이름의 가지를 합칩니다. 
    - 만약 두 브랜치에서 서로 충돌되는 작업 내용이 발생할 때도 있습니다. 

- `git diff <present_branch> <to_be_merged_branch>`
    - 하지만 그전에, 가능하다면 위 코맨드를 통해 뭐가 다른지 확인하는 것도 필요합니다. 

### 특정 commit 시점으로 되돌리기 

- `git revert  <commit hash code>`:
    - 이력을 남기고 원래대로 돌아가는 방법 

- `git reset --hard  <commit hash code>`:
    - 이력마저 초기화시키는 방법

## reference

- <http://www.devpools.kr/2017/02/05/초보용-git-되돌리기-reset-revert/>
- <https://rogerdudler.github.io/git-guide/index.ko.html>