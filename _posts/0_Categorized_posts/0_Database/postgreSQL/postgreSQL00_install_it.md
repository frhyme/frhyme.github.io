---
title: PostegreSQL - install it.
category: others
tags: database sql postgresql relationalDB
---

## PostegreSQL - install it on Mac

- PostregreSQL을 설치해보기로 했습니다. 
- [PostgreSQL](https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=438)을 통해 13.1 버전을 다운받아서 설치했는데...비밀번호가 자꾸 안 맞는다고 해서, 지웠습니다.
- brew를 사용해서 다운받으려고 했지만, 

```plaintext
brew install postgresql
```

- 다음 오류와 함께 되지 않습니다. 읽어보면, 그냥 지금 제 user에 권한이 없다는 것이니까, user에게 해당 폴더에 파일을 쓸 수 있는 권한을 주면 되는 것이기는 한데요 좀 불안합니다. 분명히 예전에는 그냥 잘 되었거든요.
- 찾아보니, macOS가 업그레이드되면서, /usr/local/에 대한 권한이 변경되었습니다. 그래서 아래 오류가 발생하는 것이죠.

```plaintext
(base) sss-MacBookAir ~ % brew install postgresql
Error: The following directories are not writable by your user:
/usr/local/lib/pkgconfig
/usr/local/share/info
/usr/local/share/man/man3
/usr/local/share/man/man5

You should change the ownership of these directories to your user.
  sudo chown -R $(whoami) /usr/local/lib/pkgconfig /usr/local/share/info /usr/local/share/man/man3 /usr/local/share/man/man5

And make sure that your user has write permission.
  chmod u+w /usr/local/lib/pkgconfig /usr/local/share/info /usr/local/share/man/man3 /usr/local/share/man/man5
```

- 이럴 때 습관적으로 그냥 `sudo`를 사용해서 쓰기는 하는데, 그래도 안되는 건 마찬가지네요.

```plaintext
(base) sss-MacBookAir ~ % sudo brew install postgresql
Password:
Error: Running Homebrew as root is extremely dangerous and no longer supported.
As Homebrew does not drop privileges on installation you would be giving all
build scripts full access to your system.
```

## 왜 이러는가

- 분명히 예전에는 잘 되었는데 갑자기 안되는 것 같아요. 그렇다면, 왜 안되는 것인지 파악해야 저는 다음 단계로 넘어갈 수 있습니다.



## reference

- [Mac OS 에 jq 설치하기](https://cleanupthedesk.tistory.com/12)

