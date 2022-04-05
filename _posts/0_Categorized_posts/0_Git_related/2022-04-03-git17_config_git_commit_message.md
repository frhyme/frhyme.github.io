---
title: git 17 - set commit message template
category: git
tags: git commit config
---

## git 17 - set commit message template

- git commit message를 작성할 때, 항상 template이 등장하도록 하려고 합니다.

```sh
cd frhyme.github.io/.git
vi .gitmessage
```

- `.gitmessage`에는 아래 내용을 작성해 봅니다.

```plaintext
This is template message
```

- 그리고 아래 command를 통해 template message를 설정해 줍니다.

```sh
cd frhyme.github.io/
git config commit.template ./.git/.gitmessage
```

- `.git/.gitmessage` file을 열어 보면 아래 내용에 추가되어 있는 것을 알 수 있습니다.

```sh
# 2022.04.03 - sng_hn.lee
[commit]
  template = ./.git/.gitmessage
```

- 이제 `git commit`을 할때마다, 해당 template에 있는 내용이 작성되어 있는 것을 알 수 있습니다.

## Wrap-up

- 저는 모든 commit message를 `2022.04.03(Sun)`로 시작합니다.
- 매번 날짜를 입력하는 게 꽤 귀찮은 일이기는 해서, vimscript를 사용해서 대치어를 만들어두기는 했는데요.
- 그냥 `git commit`이 될 때마다 알아서 해당 날짜가 안에 들어가면 좋겠다, 라는 생각을 해봅니다.
- 이걸 하려고 좀 뒤져봤는데, 아직은 뾰족한 방법을 못 찾았습니다. 다음에 찾게 되면 새로운 포스팅을 해보려고요.
