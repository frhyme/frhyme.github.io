---
title: Python - Selenium - Chrome driver
category: python-libs
tags: python python-libs seleinum chrome
---

## Python - Selenium - Chrome driver

- 맥에서 다음과 같은 코드로 selenium에서 chrome browser를 사용하려고 하는 경우에 아래와 같은 오류가 발생합니디. 

```python
from selenium import webdriver

target_url = ""

browser = webdriver.Chrome()
browser.get(target_url)
```

- chromedriver가 설치되어 있지 않다는 이야기죠. 

```bash
Traceback (most recent call last):
...
FileNotFoundError: [Errno 2] No such file or directory: 'chromedriver'

During handling of the above exception, another exception occurred:
...
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

- `brew install`를 사용해서 chrome driver를 설치해줍니다.

```bash
$ brew install chromedriver
==> Downloading https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_mac64.zip
######################################################################## 100.0%
==> Installing Cask chromedriver
==> Linking Binary 'chromedriver' to '/usr/local/bin/chromedriver'
🍺  chromedriver was successfully installed!
```

- 코드를 다시 실행해 봐도, "개발자를 확인할 수 없기 때문에 ‘chromedriver’을(를) 열 수 없습니다"라는 Warning과 함께 실행되지 않습니다.

```bash
$ python test.py
Traceback (most recent call last):
  ...
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: -9
```

## Solution 

- 우선 크롬 업데이트를 먼저 해두는 것이 좋을 수도 있습니다.
- 이를 해결하기 위해서는 chromedriver가 설치된 곳으로 우선 이동합니다. 저의 경우 `/usr/local/bin/chromedriver`에 설치되어 있죠.
- 해당 경로로 간 다음 아래 커맨드들을 순서대로 실행해줍니다. 사실 `xattr -d com.apple.quarantine chromedriver`만 실행하면 되는 것이기는 합니다.
  - `xattr filename`: filename의 속성을 확인합니다. 
  - `xattr -d com.apple.quarantine chromedriver`: `com.apple.quarantine` 속성을 chromedrive 파일에서 지워줍니다.

```bash
$ xattr chromedriver
com.apple.quarantine
$ xattr -d com.apple.quarantine chromedriver
$ xattr chromedriver
```

- 이렇게 처리하고 나면, chrome browser가 잘 열립니다.
