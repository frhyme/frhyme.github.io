---
title: macOS - pkg 로 설치한 프로그램 삭제하기 
category: macOS
tags: macOS pkg pkgutil dmg 
---

## macOS - pkg 로 설치한 프로그램 삭제하기

## things to write

- apple에서 pkg로 설치한 프로그램들을 삭제하고 싶을 때가 있습니다. 이 프로그램들을 삭제하려면 어떻게 해야 하는지를 정리합니다.
- 더불어, pkg로 설치하는 것은 무엇인지도 함께 정리합니다.
- dmg와 pkg로 설치하는 방식의 차이는 무엇인가?

---

## Intro - 제대로 제거되지 않은 프로그램 삭제하기

- 잠시 사용할 일이 있는 프로그램을 pkg 파일로 다운받아서 맥에 설치했습니다. 
- 잠시 사용한 다음, 맥에서 프로그램을 지우는 사용하는 방법인 Finder > 응용 프로그램 > 해당 프로그램 을 휴지통으로 옮겨주었습니다.
- 그러나, 해당 프로그램은 완전히 지워지지 않았고, 프로세스 상에서 계속 남아 있더군요. 혹시나 하는 마음에 해당 pkg 파일을 다시 실행하여 Uninstall 메뉴가 있는지도 확인해 봤지만, 존재하지 않았습니다.
- 그냥 프로세스만 죽이면 끝나는게 아닐까 싶어서, 프로세스만 강제종료 해봤지만, 종료되지 않거나 종료되어도 다시 실행되는 일이 빈번하더군요.
- 따라서, 직접 해당 패키지가 설치된 폴더를 가서 프로그램들을 일일이 지워줘야 했죠.
- 아래의 글들은 제대로 지워지지 않는 프로그램을 지우기 위해서, 알아보고 정리한 내용들입니다.

## Install by App Store, dmg, pkg

- 맥에 프로그램을 설치하는 방법은 총 다음 3가지가 있습니다.
  1. 맥 App Sotr에서 설치하는 방법이 있지만, 사실 이 방법은 잘 사용하지 않습니다. 저의 경우는 App Store를 통해 설치한 프로그램은 "카카오톡"과 "Elmedia Player", slack 등 다양한 프로그램들이 있네요.
  2. dmg 파일을 다운받아서 설치하는 방법이 있습니다. dmg 파일은 일종의 가상 CD 이미지라고 생각하시면 되고, 얘를 실행하면 바로 설치 프로그램으로 넝머가는 것이 아니라, 새로운 가상 디스크 드라이브가 마운트되죠. 사실 맥북에는 시디롬이 없지만, 시디롬에 씨디가 삽입되어 있는 상태라고 보시면 됩니다. 과거에 컴퓨터를 사용할 때는 새로운 프로그램을 설치하기 위해서, 씨디를 집어넣어주었잖아요? 같은 개념이라고 보시면 될 것 같아요.
  3. pkg 파일을 다운받아서 설치하는 방법이 있습니다. dmg 파일의 경우 가상 이미지를 마운트 시킨 다음, 설치 프로그램을 실행하는 반면, pkg 파일은 바로 설치 프로그램을 실행하는 개념이다, 라고 보시면 될 것 같아요.

## 프로그램을 제거 하는 방법

- 설치 방식에 따라서 프로그램을 제거 하는 방법도 조금씩 다릅니다.
- 우선, 맥 App Store를 사용해서 설치한 경우에는, LaunchPad에서 제거하려는 프로그램 아이콘을 꾹 눌러주면 아이콘 오른쪽 위로 X 버튼이 뜨는데요. 얘를 눌러주면 알아서 삭제해줍니다. 즉, 설치도, 제거도 관리도 모두 편한 가장 좋은 방식이죠.
- 만약, pkg, dmg 등의 파일로 설치한 프로그램을 삭제할 때는 그냥 Finder > 응용 프로그램 > 해당 프로그램을 선택하고 삭제를 해주면 끝난다...라고 알려져 있기는 합니다. 하지만, 이렇게 삭제 했을 때는, 프로그램이 깔끔하게 지워지지 않고, 남아 있는 경우들이 꽤 있는 것 같아요. 

## pkgutil 

- 검색해 보던 중에, [how do i uninstall any apple pkg pakcage file](https://superuser.com/questions/36567/how-do-i-uninstall-any-apple-pkg-package-file)를 읽어 보니, pkg를 사용하여 설치한 프로그램을 삭제하기 위해서는 pkgutil이라는 명령어를 사용해야 한다는 내용이 있었습니다.
- [pkgutil](https://www.real-world-systems.com/docs/pkgutil.1.html)은 "pkgutil -- Query and manipulate Mac OS X Installer packages and receipts", 즉, 맥에서 package를 관리하는 command line tool로 보입니다.

### receipt, bom

- 위 내용에서 "Receipts"라는 말이 좀 특이해서 찾아보니, [zhimingwang - os x package receipts](https://archive.zhimingwang.org/blog/2014-10-25-os-x-package-receipts.html)에서 "macOS에서는 `/var/db/receipts` 경로 내에 설치된 package들의 명세를 정리해둔다"라는 내용이 써 있네요. 
- 실제로 해당 경로로 가서, 확인해 보면. `.bom` 으로 끝나는 파일들이 쭉 있죠. 얘들이 바로, 해당 패키지에서 어떤 파일들을 설치했는지에 대한 그 명세를 쭉 작성해둔 것으로 보입니다.
- 해당 파일은 모두 binary이기 때문에, `vi`를 사용해서 열수는 없으며, `lsbom`이라고 하는 명령어를 사용해서 다음과 같이 실행하면 됩니다.

```zsh
lsbom -f <filename>
```

- 따라서, 해당 파일 내에 작성되어 있는 파일들을 모두 지우면, 해당 패키지를 문제없이 삭제할 수 있는 것으로 보입니다.

### pkgutil forget

- 그리고 관련 폴더들을 모두 삭제해 주었다면, 아래 명령어를 통해, pkgutil의 관리에서 해당 패키지를 제외해줍니다.
- 혹은 그냥 `/var/db/receipts`의 bom, plist 파일들을 지워져도 상관없는 것 같아요. 

```sh
sudo pkgutil --forget <package_name> 
```

## Remove Citrix

- 제가 지우려고 하는 프로그램은 Citrix 라는 프로그램이었습니다. 위에서 작성한 방법은 사실, 삽질을 하던 끝에 나온 깔끔한 방식이고, 저는 `pkgutil forget`을 실행하면 다 지워주는줄 알고, 얘를 먼저 실행해버려서, 어떤 파일들을 일일이 지워줘야 하는지 알지 못했죠.
- 따라서, 저는 [How to Remove Files Remaining on System after Uninstalling Receiver for Mac](https://support.citrix.com/article/CTX134237)을 읽고 이 글에서 지워주라고 하는 것들을 다 지워줬더니, 더이상 백그라운드에서 해당 프로그램이 돌지 않았습니다.
- 주요 경로는 다음과 같아요. 해당 경로 내에서 관련 파일들이 있는지 한번 쭉 훑어보시면 도움이 될 겁니다. 그냥 Finder에서 찾아도 웬만한 건 나옵니다만.

```plaintext
/Applications

/Library
- /Internet plug-ins/
- /LaunchAgents/

/Users/Shared

~/Library
- /Internet plug-ins/
- /Application Support/
- /Preferences/

~/Applications

/private/var/db/receipts
```

## Wrap-up

- pkg 파일을 실행할 때, 실행기록을 저장해둘 수 있습니다. 해당 로그를 보면 어떤 경로에 어떤 파일이 저장되는지 알 수 있는데요. 그 내용을 바탕으로 파일들을 다 지워줘도 됩니다.
- 몇 가지 정리할 내용들이 좀 더 있었던 것 같긴 하지만 귀찮으므로 그만 합니다 하하하.

## reference

- [superuser - how do i unnstall any apple pkg package file](https://superuser.com/questions/36567/how-do-i-uninstall-any-apple-pkg-package-file)
- [zhimingwang - os x package receipts](https://archive.zhimingwang.org/blog/2014-10-25-os-x-package-receipts.html)
