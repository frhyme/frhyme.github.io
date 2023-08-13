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
- `gh auth login`: 로그인을 합니다.
  - 처음에는 SSH protocol을 사용했는데, 에러가 발생해서 재고르인하여 HTTPS protocol을 사용하는 것으로 변경하였더니 잘 되었습니다.
- `gh repo clone repo_name`: repo를 가져옵니다. 잘 가져와집니다. 호호.

```bash
$ gh repo clone e9t/nsmc
Welcome to GitHub CLI!

To authenticate, please run `gh auth login`.

$ gh auth login
? What account do you want to log into? GitHub.com
? You're already logged into github.com. Do you want to re-authenticate? Yes
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: ####-####
- Press Enter to open github.com in your browser... 
✓ Authentication complete. Press Enter to continue...

- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as user_name

$ gh repo clone ...
Cloning into '...'...
remote: Enumerating objects: 14763, done.
remote: Total 14763 (delta 0), reused 0 (delta 0), pack-reused 14763
Receiving objects: 100% (14763/14763), 56.19 MiB | 22.30 MiB/s, done.
Resolving deltas: 100% (1749/1749), done.
Updating files: 100% (14737/14737), done.
```

## Wrap-up

- github에서만 제공되던 기능들인 pull request, issue들을 CLI에서도 처리할 수 있도록 해준 기능이기는 한데, 저는 아직까지는 이게 반드시 필요한지 잘 모르겠네요.
- 사실 저는 맨날 혼자 프로그래밍을 하기 때문에, 혼자 `git`을 사용하고....따라서 conflict가 발생하는 일이 없고...issue도 없고...pull request도 당연히 없고....그래서 필요가 없지만, 앞으로는 `clone repo`를 위해서 gh를 사용해야 하기 때문에 다음과 같이 정리해봤습니다 하하.

## Reference

- [github - cli](https://cli.github.com/)
- [github - cli - cli - installation](https://github.com/cli/cli#installation)
