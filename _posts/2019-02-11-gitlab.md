---
title: gitlab을 사용합니다. 
category: others
tags: git gitlab 
---

## gitlab을 사용합니다. 

- 이 블로그는 github에서 제공?하는 지킬을 가지고 만들어졌고, 운영됩니다만, 가끔 코드 중에서 private하게 지켜져야 하는 것들이 있습니다. 
- github은 돈을 내지 않으면 모든 리퍼지토리가 공개되니까요. 다만 gitlab은 돈을 내지 않아도 리퍼지토리를 프라이빗하게 사용할 수 있습니다. 
- 사실 특별히 새로운 내용을 쓰지는 않을 것 같습니다. 다만, git을 복습한다고 생각하고 글을 쓰고 있습니다. 

## gitlab.

- 일단 가입을 하고, 리퍼티토리를 하나 만듭니다. 
- 그리고 기본적인 이름과 이메일을 세팅해줍니다. 

```git
git config --global user.name "<YOUR NAME>"
git config --global user.email "<YOUR EMAIL>"
```

- `git init`: 초기화해주고, 
- `git remote add origin <gitlab repository>`
    - `origin`으로 `<gitlab repostory>`을 등록해준다. `origin`은 기본적으로 설정해주는 저장소라고 생각하면 됩니다. 
    - `git remote add another_repo_name <gitlab repository>`으로 세팅하면, `another_repo_name`이라는 이름으로 특정 리퍼지토리를 등록해주는 것을 말합니다. 
    - 즉, 여러 리퍼지토리에 대해서 등록을 하고, push, pull을 해줄수 있다는 것이겠죠. 
- `git add .`
    - 해당 폴더 내의 모든 파일을 트래킹하도록 세팅해주고, 
- `git commit -m "<Initial commit>"`
    - 처음 커밋을 하나 날려줍니다. `-m`은 메시지변수라는 의미죠.
- `git push -u origin master`
    - push해줍니다. `-u`는 앞으로 origin과 master를 연결해서 기억하여 앞으로는 `git push`, `git pull`등만으로도 사용할 수 있게 세팅해줍니다. 한번만 하고 나면 다음부터는 `-u`를 사용하지 않아도 문제가 없습니다. 

```git 
git init 
git remote add origin <gitlab repository>
git add .
git commit -m "Initial commmit"
git push -u origin master
```


## wrap-up

- 사소하지만, 처음에 gitlab을 로그인할 때, google로 로그인을 해서, 패스워드가 세팅이되어 있지 않았습니다. 그런데. git command로 push, pull을 할때는 패스워트가 세팅되어야 해서, 약간 헤맸던 기억이 있네요 하하핫.