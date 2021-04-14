---
title: github - Github CLI(gh)
category: git
tags: git github cli
---

## github - Github CLI(gh)

- 간만에 github에서 특정 repo를 `git clone`하려고 했는데, 복사해서 보니 command가 아래와 같이 좀 달라져 있더군요.

```bash
$ gh repo clone repo_name
```

- 찾아보니 [gh](https://cli.github.com/)는 github 전용 Command Line Interface더군요. 
- 일단 `brew install gh`를 사용해서 설치해 보겠습니다.

```bash
$ brew install gh
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
minisat                                                                                                organize-tool
==> Updated Formulae
Updated 155 formulae.
==> Renamed Formulae
fcct -> butane
==> New Casks
dingtalk-lite                                                                                          pop
==> Updated Casks
Updated 207 casks.
==> Deleted Casks
flash-npapi                       flash-player                      flash-player-debugger             flash-player-debugger-npapi       flash-player-debugger-ppapi       screen

==> Downloading https://ghcr.io/v2/homebrew/core/gh/manifests/1.8.1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/gh/blobs/...
==> Downloading from https://pkg-containers-az.githubusercontent.com/ghcr1/blobs/...
######################################################################## 100.0%
==> Pouring gh--1.8.1.big_sur.bottle.tar.gz
==> Caveats
zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/gh/1.8.1: 76 files, 20.7MB
```

- 이제 repo를 clone하려고 했는데, 로그인을 하라고 합니다.

```
$ gh repo clone e9t/nsmc                                                               ✔  ⚙  1245  19:10:18
Welcome to GitHub CLI!

To authenticate, please run `gh auth login`.


```

## Reference

- [github - cli](https://cli.github.com/)
- [github - cli - cli - installation](https://github.com/cli/cli#installation)
