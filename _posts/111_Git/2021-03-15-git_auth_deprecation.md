---
title: github - token based authtntication
category: git
tags: git github token
---

## git hub authtntication 

```plaintext
You recently used a password to access the repository at frhyme/frhyme.github.io with git using git/2.24.3 (Apple Git-128).

Basic authentication using a password to Git is deprecated and will soon no longer work. 
Visit https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information around suggested workarounds and removal dates.
```

- 더 자세히 알아봐야 할 것 같아서, [2020-12-15 token authentication requirements for git operations](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/)에 들어가 봅니다.

## Summrary - token authentication requirements

- 내용이 긴데 요약하면 대략 다음과 같습니다.
  - 2021년 8월 13일부터, 모든 Git operation에 대해서 token 기반 인증(token-based authentication)을 사용할 겁니다. 기존의 패스워드 기반의 방식은 파기 될 거에요. 따라서, git 을 사용하는 대부분의 프로그램들은 영향을 받게 될 겁니다.
  - 그 이유는, 당연히 보안 때문이고요.
- 결과적으로는 [github - authenticating to github - creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)에서 하라는 대로 하면 됩니다. 아, 발급되는 토큰은 꼭 어딘가에 저장해두시길 바랍니당.

## Wrap-up 

- 일단 하라는 대로 하기는 했는데, 흠. 어떤 변화가 있는지는 앞으로 지켜보도록 하겠습니다 호호호.