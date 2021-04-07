---
title: python - requests
category: python-lib
tags: python python-lib requests
---

## python - requests

- python library인 [requests](https://docs.python-requests.org/en/master/user/quickstart/)는 http 통신을 위한 python library입니다.
- 그냥 "웹의 리소스들에게 데이터를 보내고 받는 일들을 한다"라고만 생각하셔도 됩니다.

### Install requests

- 일단 설치부터 해보겠습니다. 
- 저는 `conda`를 사용하기 때문에 `conda install requests`를 사용해서 설치합니다.
- 의존성이 있는 다른 라이브러리들이 아주 많군요 호호호. 당연히 다 설치해줍니다.

```bash
conda install requests
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
  latest version: 4.9.2

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /Users/.../opt/anaconda3/envs/python_scratch

  added / updated specs:
    - requests


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    brotlipy-0.7.0             |py39h9ed2024_1003         333 KB
    certifi-2020.12.5          |   py39hecd8cb5_0         141 KB
    cffi-1.14.5                |   py39h2125817_0         216 KB
    chardet-4.0.0              |py39hecd8cb5_1003         195 KB
    cryptography-3.4.7         |   py39h2fd3fbb_0         693 KB
    idna-2.10                  |     pyhd3eb1b0_0          52 KB
    pip-21.0.1                 |   py39hecd8cb5_0         1.8 MB
    pysocks-1.7.1              |   py39hecd8cb5_0          31 KB
    python-3.9.2               |       h88f2d9e_0         9.9 MB
    requests-2.25.1            |     pyhd3eb1b0_0          52 KB
    setuptools-52.0.0          |   py39hecd8cb5_0         724 KB
    six-1.15.0                 |   py39hecd8cb5_0          27 KB
    sqlite-3.35.3              |       hce871da_0         1.1 MB
    tzdata-2020f               |       h52ac0ba_0         113 KB
    urllib3-1.26.4             |     pyhd3eb1b0_0         105 KB
    ------------------------------------------------------------
                                           Total:        15.4 MB

The following NEW packages will be INSTALLED:

  brotlipy           pkgs/main/osx-64::brotlipy-0.7.0-py39h9ed2024_1003
  ca-certificates    pkgs/main/osx-64::ca-certificates-2021.1.19-hecd8cb5_1
  certifi            pkgs/main/osx-64::certifi-2020.12.5-py39hecd8cb5_0
  cffi               pkgs/main/osx-64::cffi-1.14.5-py39h2125817_0
  chardet            pkgs/main/osx-64::chardet-4.0.0-py39hecd8cb5_1003
  cryptography       pkgs/main/osx-64::cryptography-3.4.7-py39h2fd3fbb_0
  idna               pkgs/main/noarch::idna-2.10-pyhd3eb1b0_0
  libcxx             pkgs/main/osx-64::libcxx-10.0.0-1
  libffi             pkgs/main/osx-64::libffi-3.3-hb1e8313_2
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  openssl            pkgs/main/osx-64::openssl-1.1.1k-h9ed2024_0
  pip                pkgs/main/osx-64::pip-21.0.1-py39hecd8cb5_0
  pycparser          pkgs/main/noarch::pycparser-2.20-py_2
  pyopenssl          pkgs/main/noarch::pyopenssl-20.0.1-pyhd3eb1b0_1
  pysocks            pkgs/main/osx-64::pysocks-1.7.1-py39hecd8cb5_0
  python             pkgs/main/osx-64::python-3.9.2-h88f2d9e_0
  readline           pkgs/main/osx-64::readline-8.1-h9ed2024_0
  requests           pkgs/main/noarch::requests-2.25.1-pyhd3eb1b0_0
  setuptools         pkgs/main/osx-64::setuptools-52.0.0-py39hecd8cb5_0
  six                pkgs/main/osx-64::six-1.15.0-py39hecd8cb5_0
  sqlite             pkgs/main/osx-64::sqlite-3.35.3-hce871da_0
  tk                 pkgs/main/osx-64::tk-8.6.10-hb0a8c7a_0
  tzdata             pkgs/main/noarch::tzdata-2020f-h52ac0ba_0
  urllib3            pkgs/main/noarch::urllib3-1.26.4-pyhd3eb1b0_0
  wheel              pkgs/main/noarch::wheel-0.36.2-pyhd3eb1b0_0
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3


Proceed ([y]/n)?  


Downloading and Extracting Packages
sqlite-3.35.3        | 1.1 MB    | ################################################################################################################################################################# | 100% 
idna-2.10            | 52 KB     | ################################################################################################################################################################# | 100% 
tzdata-2020f         | 113 KB    | ################################################################################################################################################################# | 100% 
cffi-1.14.5          | 216 KB    | ################################################################################################################################################################# | 100% 
six-1.15.0           | 27 KB     | ################################################################################################################################################################# | 100% 
brotlipy-0.7.0       | 333 KB    | ################################################################################################################################################################# | 100% 
python-3.9.2         | 9.9 MB    | ################################################################################################################################################################# | 100% 
urllib3-1.26.4       | 105 KB    | ################################################################################################################################################################# | 100% 
certifi-2020.12.5    | 141 KB    | ################################################################################################################################################################# | 100% 
cryptography-3.4.7   | 693 KB    | ################################################################################################################################################################# | 100% 
pip-21.0.1           | 1.8 MB    | ################################################################################################################################################################# | 100% 
pysocks-1.7.1        | 31 KB     | ################################################################################################################################################################# | 100% 
setuptools-52.0.0    | 724 KB    | ################################################################################################################################################################# | 100% 
chardet-4.0.0        | 195 KB    | ################################################################################################################################################################# | 100% 
requests-2.25.1      | 52 KB     | ################################################################################################################################################################# | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

## Tutorial - GET google result

- request를 사용하여 google 사이트에 접속해서 `python`을 검색하고 그 결과를 가져와봅시다.
- 일단 웹브라우저에서 구글 사이트에 들어가서, "python"을 검색하고 그때 URL을 확인해 보면 다음과 같습니다.
- 중간에 `q=python`이라는 부분이 눈에 띄는데, 이는 google과 통신할 때 GET 방식으로 `{"q": "python}`를 parameter로 넘겨줬다라는 말이죠.

```plaintext
https://www.google.co.kr/search?q=python&... 
```

- 따라서, `requests`를 사용해서 같은 방식으로 GET 방식으로 같은 parameter를 넘겨주면 됩니다.

### Do it

- Code는 다음과 같습니다.

```python
import requests

"""
google 서비스에 아래 URL로 접속하여, 
그 결과를 google_result.html에 저장하는 코드
https://www.google.co.kr/search?q=python
"""

target_url = "https://google.com/search?"
query = {"q": "python"}

# GET 방식으로 target_url에 접속하여, query를 parameter로 넘김
r = requests.get(target_url, params=query)

with open("google_result.html", "w") as f:
    f.write(r.text)  # type(r.text): str
```

- 저장된 `google_result.html` 파일을 웹브라우저로 열어보면, 진짜 구글의 결과인것을 알 수 있습니다.
- 위 코드에서는 GET 방식을 사용했지만, POST 방식을 포함하여 다른 방식도 가능합니다. 이는 나중에 필요할 때 해볼게요.

## Wrap-up

- web에서 데이터를 crawling할 때 지금까지는 항상 selenium을 사용해왔습니다. selenium의 경우 Firefox와 같은 브라우저 인스턴스를 생성한 다음 해당 브라우저를 통해 데이터를 가져오는 방식이죠. 브라우저 자체가 좀 무겁기 때문에, 약간 느리고 무겁습니다.
- 반면, request의 경우는 브라우저 없이 직접 통신하는 것처럼 보여서, 제가 보기에는 좀 더 가볍게 느껴져요. 따라서 다음에 데이터를 크롤링해야 한다면 seleinum을 사용하는 것보다, requests를 사용하는 것이 더 효율적일 것으로 보입니다.
