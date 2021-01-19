---
title: Git - commit 전에 staged 파일 diff
category: git
tags: git commit stage diff
---

## Git - commit 전에 staged 파일 diff

- 현재 디렉토리에서 이전 commit과 차이점이 뭐가 있는지 확인하려면 다음을 실행합니다.

```git
git diff
```

- 하지만, `git add .`을 사용해서 이미 파일들을 staging area에 올린 상황이라면 위 명령어가 무의미하죠.
- 그럴때는 `--staged`를 붙이면 됩니다.

```git
git diff --staged
```
