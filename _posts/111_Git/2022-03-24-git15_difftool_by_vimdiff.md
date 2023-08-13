---
title: Git 15 - Used difftool by Side by Side Compare
category: git
tags: git config diff difftool compare vim vi gitconfig
---

## Git 15 - Use difftool by Side by Side compare

- command line에서 Side by Side Diff 되도록 설정하려면 다음과 같이 실행하면 됩니다.

```sh
git difftool --tool=vimdiff
```

- 다만, 위처럼 하는 경우 항상 위처럼 길게 작성해줘야 합니다.
- 따라서, `~/.gitconfig` 파일에 아래 내용을 추가하여, difftool 사용시 항상 `vimdiff`가 사용되도록 설정해줍니다.
  - `prompt = false`: "y/n"을 묻지 않고 바로 실행하도록 설정

```.gitconfig
[diff]
    tool = vimdiff
    prompt = false
# 2022.03.24 - sng_hn.lee difftool 사용시 기본적으로 vimdiff 사용하도록 설정
[difftool]
    tool = vimdiff
    prompt = false
```

## Wrap-up

- 그동안 git config을 거의 신경 쓰지 않았는데, 조금씩 수정해서 설정해 봐야겠어요.

## Reference

- [stackoverflow - how can i get a side by side diff when i do git diff](https://stackoverflow.com/questions/7669963/how-can-i-get-a-side-by-side-diff-when-i-do-git-diff)
- [git diff side by side](https://zeldor.biz/2019/09/git-diff-side-by-side/)
- [git diff를 gui 프로그램으로 설정하는 방법](https://itmir.tistory.com/670)
