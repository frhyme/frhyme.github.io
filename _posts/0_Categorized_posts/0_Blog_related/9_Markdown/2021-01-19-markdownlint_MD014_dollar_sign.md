---
title: MarkdownLint - MD014 - Dollar signs used before commands without showing output
category: MarkdownLint
tags: markdown markdownlint
---

## MarkdownLint - MD014 - Dollar Sign

- MD014는 shell command를 작성할 때, `$` dollar sign과 command가 함께 등장할 경우에는 출력결과가 함께 있지 않으면 오류라고 판정한다는 이야기입니다.
- 가령 다음처럼 dollar sign없이 쓰거나.

```bash
ls
```

- 다음처럼 출력 결과와 함께 쓰라는 이야기죠.

```bash
$ ls
a.png
```
