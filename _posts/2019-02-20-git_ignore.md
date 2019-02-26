---
title: git 프로젝트 폴더에 특정 파일 제외해서 push하기 
category: others
tags: git

---

## 특정 폴더나 파일이 git에 걸리지 않게 하기

- 작업을 하다보면 약간 security에 걸리는 부분이 있을 수 있습니다만, 물론 제가 그렇게 중요한 사람은 아니지만 어쨌든 간에, 몇 가지 파일들을 git의 관리에서 제외되도록 하고싶을 때가 있습니다. 이걸 어떻게 할 수 있을까요? 

- 우선은 `.gitignore` 파일을 만들고(이미 있을 수도 있습니다), 제외되어야 하는 파일을 명을 넣습니다. 
    - 그리고 해당 내용에 다음처럼 git으로 관리될 필요가 없는 file의 이름을 추가해서 넣어두면 이후 `git status`등을 처리해도 무시하고 업로드됩니다. 

```
# comment
ignored_file.md
```

## wrap-up

- 쓰고보니 이렇게 간단한 것을 저는 왜 지금까지 사용하지 않았을까요 허허허.


## reference

<https://emflant.tistory.com/127>