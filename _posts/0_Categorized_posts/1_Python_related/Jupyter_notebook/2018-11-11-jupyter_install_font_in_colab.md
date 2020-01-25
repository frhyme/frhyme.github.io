---
title: colab에서 nanum font 사용하기 
category: python-libs
tags: python python-libs font colab jupyter-notebook 
---

## intro 

- 저는 요즘 모든 코딩을 colab에서 하고 있습니다. 강점이쟈 약점은, 세팅해놓은 환경을 다시 시작하면 초기화된다는 것이죠. 
- 저는 이걸 강점이라고 생각해요. 라이브러리를 설치하거나, 뭔가를 하다보면 의존성 문제등으로 인해서 충돌하는 경우가 꽤 자주 발생하는데, 이 때 이를 효율적으로 다루는 것이 어렵습니다. 설치한 다음에는 깔끔하게 지우는 것이 보통 어려우니까요. 
- 아무튼 그러한 이유로 저는 요즘 매번 초기화되는 colab를 사용하고 있습니다.

## font를 설치하자. 

- 뭐 라이브러리야 그렇다고 치는데, font를 설치하는 것이 좀 어렵더군요(matplotlib의 기본 font는 너무 별로거든요)
- 현재 설정에 새롭게 깔아줘야 하므로, 간단하게 다음을 이용해서 설치합니다. 
    - 선택해서 설치할 수도 있으나, 저는 귀찮으므로 그냥 모두 설치해줍니다.

```python
!apt-get install fonts-nanum*
all_fonts_I_can_use = fm.findSystemFonts(fontpaths=None, fontext='ttf')
all_fonts_I_can_use
```

```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'fonts-nanum-eco' for glob 'fonts-nanum*'
Note, selecting 'fonts-nanum' for glob 'fonts-nanum*'
Note, selecting 'fonts-nanum-gothic-light' for glob 'fonts-nanum*'
Note, selecting 'fonts-nanum-coding' for glob 'fonts-nanum*'
Note, selecting 'fonts-nanum-extra' for glob 'fonts-nanum*'
The following NEW packages will be installed:
  fonts-nanum fonts-nanum-coding fonts-nanum-eco fonts-nanum-extra
0 upgraded, 4 newly installed, 0 to remove and 5 not upgraded.
Need to get 37.0 MB of archives.
After this operation, 145 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic/universe amd64 fonts-nanum all 20170925-1 [9,604 kB]
Get:2 http://archive.ubuntu.com/ubuntu bionic/universe amd64 fonts-nanum-eco all 1.000-6 [14.0 MB]
Get:3 http://archive.ubuntu.com/ubuntu bionic/universe amd64 fonts-nanum-extra all 20170925-1 [12.2 MB]
Get:4 http://archive.ubuntu.com/ubuntu bionic/universe amd64 fonts-nanum-coding all 2.5-1 [1,083 kB]
Fetched 37.0 MB in 2s (21.5 MB/s)
Selecting previously unselected package fonts-nanum.
(Reading database ... 22280 files and directories currently installed.)
Preparing to unpack .../fonts-nanum_20170925-1_all.deb ...
Unpacking fonts-nanum (20170925-1) ...
Selecting previously unselected package fonts-nanum-eco.
Preparing to unpack .../fonts-nanum-eco_1.000-6_all.deb ...
Unpacking fonts-nanum-eco (1.000-6) ...
Selecting previously unselected package fonts-nanum-extra.
Preparing to unpack .../fonts-nanum-extra_20170925-1_all.deb ...
Unpacking fonts-nanum-extra (20170925-1) ...
Selecting previously unselected package fonts-nanum-coding.
Preparing to unpack .../fonts-nanum-coding_2.5-1_all.deb ...
Unpacking fonts-nanum-coding (2.5-1) ...
Setting up fonts-nanum-extra (20170925-1) ...
Setting up fonts-nanum (20170925-1) ...
Setting up fonts-nanum-coding (2.5-1) ...
Setting up fonts-nanum-eco (1.000-6) ...
['/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareRoundB.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjoExtraBold.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjoBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareRoundR.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunGothicLight.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunGothicUltraLight.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareRoundL.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareEB.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicEcoExtraBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicExtraBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumPen.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjoEcoBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareB.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjoEcoExtraBold.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicEcoBold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBrush.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareRoundEB.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicLight.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicCoding-Bold.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf',
 '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunpenR.ttf',
 '/usr/share/fonts/truetype/nanum/NanumBarunpenB.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareL.ttf',
 '/usr/share/fonts/truetype/nanum/NanumMyeongjoEco.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf',
 '/usr/share/fonts/truetype/nanum/NanumSquareR.ttf',
 '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf']
```

## other font 

- 저는 보통, 배달의 민족 폰트를 좋아합니다. 
- 우선 `apt-get`은 우분투 환경에서 사용하는 패키지 매니저입니다(`pip` 같은 것이죠). 따라서 제가 사용하려고 하는 다른 폰트가 우분투 패키지로 등록되어 있는지를 먼저 봐야 합니다. 
- [여기를 들어가시면 한글 폰트가 뭐가 있는지 볼 수 있습니다](https://packages.ubuntu.com/search?suite=all&section=all&arch=any&keywords=korean+font&searchon=all). 한나는 열한살 체는 있네요. 

- 대략적인 코드를 다시 정리하면 다음과 같습니다. 

```python
import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

!apt-get install fonts-nanum*
!apt-get install fonts-woowa-hanna

BM_HANNA = fm.FontProperties(fname='/usr/share/fonts/truetype/woowa/BM-HANNA.ttf')
NANUM_GOTHIC = fm.FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothic.ttf')
NANUM_GOTHIC_CODING = fm.FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf')


# 
"""
- font의 위치를 가져와서 font properties로 사용할 때는 해당 폰트파일이 어디에 있든 문제가 없지만, 
- font_family(font의 이름과 동일한 의미)를 사용해서 세팅할 때는 matplotlib 내에서 해당 폰트 파일을 가지고 있어야 함. 
- 따라서 아래처럼 빌드 해주는 것이 필요함. 
"""
fm._rebuild()

plt.rc('font', family=NANUM_GOTHIC.get_name() )
mpl.rcParams['axes.unicode_minus'] = False

# all_fonts_I_can_use = fm.findSystemFonts(fontpaths=None, fontext='ttf')

```

## wrap-up

- 이제 colab을 쓰는데도 일정 이상의 설정이 늘어나고 있습니다. 매번 colab을 사용할 때마다 일정 이상의 세팅을 자동으로 포함해서 쥬피터 노트북을 생성하도록 할 수는 없는지 궁금해지는 군요.