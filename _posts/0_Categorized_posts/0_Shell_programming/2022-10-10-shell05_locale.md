---
title: Shell - locale
category: shell
tags: shell locale
---

## Shell - local

- shell locale에 대해서 정리하려고 시작한 것은 아닌데, `git difftool`을 사용할 때 계속 한글로 message 가 발생하는 것이 성가셔서 찾다보니 locale에서 발생한 문자였다는 사실을 깨달았습니다. 생각해보니, 한글날에 locale을 english로 바꾼다는 나의 마음이 뭔가 참혹한데요...한글 사랑합니다. 킹세종 갓세종
- 아무튼, `git difftool`을 사용할 때 다음과 같은 한글 메세지가 발생합니다. 그냥 한글이기는 한데, 다 영문으로 작성되어 있는데 저 부분만 한글로 작성되어 있는 것이 일관성이 떨어지는 기분이 들더군요.

```sh
❯ git difftool
2 파일을 고치기
```

- 그렇다면 우선은 `git difftool`이 어떻게 실행되는지를 확인해야합니다. `git config`을 사용하여 확인해 보면, 저의 경우는 `vimdiff`를 사용하고 있는 것으로 확인됩니다. vimdiff는 vim에서 제공하는 기본 diff tool이죠.

```sh
> git config --list
diff.tool=vimdiff
diff.prompt=false
difftool.tool=vimdiff
difftool.prompt=false
```

- 이를 변경하기 위해 `export LC_MESSAGES="en_US.UTF-8"`를 사용했습니다.

```sh
❯ locale
LANG="ko_KR.UTF-8"
LC_COLLATE="ko_KR.UTF-8"
LC_CTYPE="ko_KR.UTF-8"
LC_MESSAGES="ko_KR.UTF-8"
LC_MONETARY="ko_KR.UTF-8"
LC_NUMERIC="ko_KR.UTF-8"
LC_TIME="ko_KR.UTF-8"
LC_ALL=
❯ export LC_MESSAGES="en_US.UTF-8"
❯ date
2022년 10월 10일 월요일 22시 07분 28초 KST
❯ git difftool
2 files to edit
❯ locale
LANG="ko_KR.UTF-8"
LC_COLLATE="ko_KR.UTF-8"
LC_CTYPE="ko_KR.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_MONETARY="ko_KR.UTF-8"
LC_NUMERIC="ko_KR.UTF-8"
LC_TIME="ko_KR.UTF-8"
LC_ALL=
```

## wrap-up

- setting이 vimdiff에 의존적이라고 생각했는데 vim 쪽이 아닌 bash 쪽에 의존이었던 것으로 보입니다. 이 변경을 유지하려면 `~/.zshrc`에 값을 추가해주는 것도 좋겠네요.
