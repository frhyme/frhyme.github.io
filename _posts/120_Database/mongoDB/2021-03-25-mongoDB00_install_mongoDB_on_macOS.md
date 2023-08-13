---
title: mongoDB - Install mongoDB on macOS
category: mongoDB
tags: database sql nosql mongodb macOS brew 
---

## mongoDB - Intro

- 지금까지는 계산 중에 발생하는 결과물들을 json 혹은 pickle로 저장하곤 했습니다. 간단한 계산결과의 경우는 이렇게 처리해도 별 문제가 없었는데요. 동시에 여러 세션을 돌리면서 데이터를 저장하는 경우에는 문제가 발생하곤 합니다. 
- 사실 생각해보면, DB는 이미 어떤 데이터가 쓰이고 있을 때 락을 걸기도 하고, 데이터를 쓰는 중에 오류가 발생하면 rollback을 해서 데이터베이스의 무결성을 유지해주기도 하는데요. pickle이나 json을 사용해서 그냥 사용하는 경우에는 가끔 파일을 쓰는 중에, 프로그램이 멈춰서 해당 파일 자체가 작살나는 경우가 있습니다.
- 네, 저도 pickle로 그냥 데이터를 쓰다가 며칠동안 쌓아놓은 데이터가 모두 날아갔습니다.
- 아무튼, 그래서 mongoDB를 설치해보기로 했습니다.

## Install mongoDB()

### Brew install mongodb(fail)

- mac의 경우 `brew`를 사용해서 mongoDB를 설치할 수 있다고 해서 다음 명령어를 실행해줍니다.
- 하지만, 오류를 보면 알 수 있듯이 설치가되지 않는군요 호호호.

```plaintext
$ brew install mongodb
... 
==> Searching for similarly named formulae...
Error: No similarly named formulae found.
Error: No available formula or cask with the name "mongodb".
==> Searching for a previously deleted formula (in the last month)...
Error: No previously deleted formula found.
==> Searching taps on GitHub...
Error: No formulae found in taps.
```

- 아래 명령어를 실행하면 되다고 하는데 저는 이것도 안돼요.

```plaintext
$ brew install mongodb-community@4.2
...
Error: No formulae found in taps.
```

### mongoDB homepage

- [mongoDB - community server](https://www.mongodb.com/try/download/community)에서 macOS, 4.4.4 version을 다운받아줍니다. 
- 다운받은 다음 압축을 풀어줍니다. 현재 다운받아서 압축을 푼 폴더는 `~/Downloads`에 존재합니다.
- 사실 해당 폴더에 그대로 두고 사용해도 문제는 없습니다만, `Downloads`에 있으면 제가 실수로 지우거나 할 수도 있으므로, 파일을 다음과 같이 옮겨줍니다.
- `usr/local`에 넣어준건 별 이유 없습니다. 그냥, 많은 설치 파일들이 보통 해당 폴더 내에 넣어주곤 하니까 여기서도 그냥 넣어준 것이죠.

```bash
$ sudo mv Downloads/mongodb-macos-x86_64-4.4.4 ../../../usr/local/mongodb
Password:
$ cd ../../../usr/local/mongodb
$ ls
LICENSE-Community.txt MPL-2                 README                THIRD-PARTY-NOTICES   bin
```

- 이제 설치했으니까, 커맨트라인에서 `mongod`를 쳐보면 되나? 싶지만, 안됩니다. 커맨드라인에서 해당 명령어를 인식하지 못하기 때문이죠.
- 따라서, 명령어를 인식하도록 설정해줍니다.
- 저는 zsh를 사용하기 때문에, `~/.zshrc`에 들어가서 다음 내용을 작성하고 저장해줍니다.

```bash
# 20210325 mongoDB path 
export PATH=$PATH:/usr/local/mongodb/bin
```

- 자. 이제 되어야 할 것 같네요. 실행해봅니다. 
- 하지만, 권한 문제로 실행되지 않습니다. mongoDB가 macOS에서 정식으로 다운받은 것이 아니기 때문에, 보안 문제로 인해, 실행이 되지 않도록 처리되어 있습니다.

```bash
$ mongod -help
[1]    46450 killed     mongod -help
```

### Brew again

- 이전에 설치한 내용을 모두 원래대로 되돌려줍니다.
- [mongodb - turorial - install mongodb on os X](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)에서 말해주는 방식으로 다시 설치해봅니다.

```bash
$ brew tap mongodb/brew                                                                                                                     1 ↵  1958  20:52:13
==> Tapping mongodb/brew
Cloning into '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
remote: Enumerating objects: 67, done.
remote: Counting objects: 100% (67/67), done.
remote: Compressing objects: 100% (64/64), done.
remote: Total 570 (delta 23), reused 11 (delta 3), pack-reused 503
Receiving objects: 100% (570/570), 122.25 KiB | 818.00 KiB/s, done.
Resolving deltas: 100% (261/261), done.
Tapped 11 formulae (39 files, 195.5KB).
```

- 이제 mongodb를 설치해봅니다. 진행이 되다가, 에러가 발생하네요. 
- 내용을 잘 읽어보면, "너 Command Line Tool이 후져"라는 이야기입니다.

```bash
$ brew install mongodb-community@4.4
==> Installing mongodb-community from mongodb/brew
==> Downloading https://fastdl.mongodb.org/tools/db/mongodb-database-tools-macos-x86_64-100.3.1.zip
######################################################################## 100.0%
==> Downloading https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.4.3.tgz
######################################################################## 100.0%
==> Installing dependencies for mongodb/brew/mongodb-community: mongodb-database-tools
==> Installing mongodb/brew/mongodb-community dependency: mongodb-database-tools
Error: Your Command Line Tools (CLT) does not support macOS 11.
It is either outdated or was modified.
Please update your Command Line Tools (CLT) or delete it if no updates are available.
Update them from Software Update in System Preferences or run:
  softwareupdate --all --install --force

If that doesn't show you any updates, run:
  sudo rm -rf /Library/Developer/CommandLineTools
  sudo xcode-select --install

Alternatively, manually download them from:
  https://developer.apple.com/download/more/.

Error: An exception occurred within a child process:
  SystemExit: exit
```

- 후진 Command Line Tool을 업데이트해주려고 다음 두 명령어를 각각 실행해보았지만, 업데이트할 게 없다고 합니다.

```bash
$ softwareupdate --all --install --force
Software Update Tool

Finding available software
No updates are available.

$ seunghoonlee@seunghoonui-MacBookAir  ~  sudo xcode-select --install
xcode-select: error: command line tools are already installed, use "Software Update" to install updates
```

- 좋~아요. 그렇다면, 설치된 커맨드라인툴을 삭제하고 다시 실행해봅니다.
- 실해한 다음에는 xcode를 통해 CLT를 다운 받을 수 있습니다.

```bash
$ sudo rm -rf /Library/Developer/CommandLineTools
$ softwareupdate --all --install --force
Software Update Tool

Finding available software
No updates are available.
$ sudo xcode-select --install
xcode-select: note: install requested for command line developer tools
```

- 그리고, 다시 mongodb-community4.4를 설치해보면, 이번에는 잘 되는 것을 알 수 있습니다 호호호.

```bash
brew install mongodb-community@4.4
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/cask).
==> Updated Casks
Updated 1 cask.

==> Installing mongodb-community from mongodb/brew
==> Downloading https://fastdl.mongodb.org/tools/db/mongodb-database-tools-macos-x86_64-100.3.1.zip
Already downloaded: /Users/seunghoonlee/Library/Caches/Homebrew/downloads/6cc17321e1e8cd71c9a41b1aa722eba5ca0a9e759234e25b71eb9c8ff71e0033--mongodb-database-tools-macos-x86_64-100.3.1.zip
==> Downloading https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.4.3.tgz
Already downloaded: /Users/seunghoonlee/Library/Caches/Homebrew/downloads/269692f6b2d908000ecd7602021f4826947a782576c1fea760d25ece5ccbb521--mongodb-macos-x86_64-4.4.3.tgz
==> Installing dependencies for mongodb/brew/mongodb-community: mongodb-database-tools
==> Installing mongodb/brew/mongodb-community dependency: mongodb-database-tools
🍺  /usr/local/Cellar/mongodb-database-tools/100.3.1: 13 files, 150.9MB, built in 16 seconds
==> Installing mongodb/brew/mongodb-community
==> Caveats
To have launchd start mongodb/brew/mongodb-community now and restart at login:
  brew services start mongodb/brew/mongodb-community
Or, if you don't want/need a background service you can just run:
  mongod --config /usr/local/etc/mongod.conf
==> Summary
🍺  /usr/local/Cellar/mongodb-community/4.4.3: 11 files, 156.8MB, built in 14 seconds
==> Caveats
==> mongodb-community
To have launchd start mongodb/brew/mongodb-community now and restart at login:
  brew services start mongodb/brew/mongodb-community
Or, if you don't want/need a background service you can just run:
  mongod --config /usr/local/etc/mongod.conf
```

## wrap-up

- 다음 시간에는 mongodb를 사용해서 데이터베이스 서버를 직접 실행해보겠습니다 호호. 

## Reference

- [mongodb - tutorial - install mongodb on os x](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
