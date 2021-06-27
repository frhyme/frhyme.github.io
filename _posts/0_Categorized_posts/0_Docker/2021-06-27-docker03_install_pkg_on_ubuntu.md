---
title: docker - container 내 필요한 패키지 설치  
category: docker 
tags: docker container image
---

## docker - container 내 필요한 패키지 설치  

- docker에서 만든 ubuntu container 내에, 제가 사용하는 프로그램들을 설치해줍니다.

### install vim, zsh

- 각 명령어들에 대해서 간단하게 설명합니다.
  - `apt-get update`: apt-get은 "Advanced Packing Tool"을 말하며, 데비안 기반의 OS에서 사용하는 패키지 관리 툴입니다. python을 사용하시는 분들이 pip를 사용하여 필요한 라이브러리들을 가져오는 것처럼, `apt-get`을 사용해서 관련된 라이브러리들을 가져오는 것이죠. 그리고 `update`는 apt-get에서 관리되는 패키지들의 최신 정보를 가져오는 것이다, 라고 생각하시면 됩니다.
  - `apt-get install vim`: vim을 설치해 줍니다.
  - `apt-get install zsh`: 
  - `apt-get install git`: zsh 설정을 관리해주는 oh my zsh를 설치하려면 git을 설치해야 합니다.
  - `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"`: oh my zsh를 설치해줍니다.
- 아래 패키지들을 다 작성해서, 이미지를 만들려면 dockerfile을 작성해야 하는것 같은데.

```bash
$ apt-get update
$ apt-get install vim
$ apt-get install zsh
$ apt-get install wget 
$ sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

### install zsh theme - powerlevel10k 

- [PowerLevel100K](https://github.com/romkatv/powerlevel10k)라는 zsh theme을 설치합니다.

```bash
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
$ echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```

- 만약 powerlevel 10k 를 수정하고 싶으면 다음 명령어를 사용하면 됩니다.

```zsh
$ p10k configure
```

- 세부적으로 설정을 수정하고 싶으면 다음 명령어를 사용하면 됩니다.

```zsh
$ vi .p10k.zsh
```

### install python

- 이제 ubuntu환경에서 python을 사용하기 위해서 anaconda를 설치해줍니다.

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ bash Anaconda3-2021.05-Linux-x86_64.sh 
```

### set locale

- locale은 각 나라별로 맞는 언어, 시간에 대한 설정을 말합니다. 가령, 미국으로 맞춰져 있을 경우에는 미국 시간대로 나오고, 미국 캐릭터만 출력되는 반면, 한글로 설정되어 있을 경우에는 한국 시간대로 나오고, 한글도 자동으로 인식해 줍니다.
- 일단 `locale` 명령어를 사용해서 현재 설정된 값을 확인해 봅니다. 현재는 기본값인 POSIX로 설정되어 있네요.

```zsh
$ locale
LANG=
LANGUAGE=
LC_CTYPE="POSIX"
LC_NUMERIC="POSIX"
LC_TIME="POSIX"
LC_COLLATE="POSIX"
LC_MONETARY="POSIX"
LC_MESSAGES="POSIX"
LC_PAPER="POSIX"
LC_NAME="POSIX"
LC_ADDRESS="POSIX"
LC_TELEPHONE="POSIX"
LC_MEASUREMENT="POSIX"
LC_IDENTIFICATION="POSIX"
LC_ALL=
```

- 아래 명령어를 사용하여, 한글을 설정해줍니다.

```zsh
apt-get install language-pack-ko
locale-gen ko_KR.UTF-8
dpkg-reconfigure locales
update-locale
```

- 그리고 다시 locale 명령어를 사용해보면 다음과 같이 잘 변경되어 있는 것을 알 수 있죠.

```zsh
$ locale
LANG=ko_KR.UTF-8
LANGUAGE=
LC_CTYPE="ko_KR.UTF-8"
LC_NUMERIC="ko_KR.UTF-8"
LC_TIME="ko_KR.UTF-8"
LC_COLLATE="ko_KR.UTF-8"
LC_MONETARY="ko_KR.UTF-8"
LC_MESSAGES="ko_KR.UTF-8"
LC_PAPER="ko_KR.UTF-8"
LC_NAME="ko_KR.UTF-8"
LC_ADDRESS="ko_KR.UTF-8"
LC_TELEPHONE="ko_KR.UTF-8"
LC_MEASUREMENT="ko_KR.UTF-8"
LC_IDENTIFICATION="ko_KR.UTF-8"
LC_ALL=
```

- 다만, 이렇게 해도 해당 컨테이너를 껐다가 다시 켜면 locale이 다시 POSIX로 변경됩니다. 따라서, 저는 그냥 `.zshrc`에 아래 내용을 추가하여, 해결했습니다.

```zsh
export LANG=ko_KR.UTF-8
```

### Set timezone

- timezone을 바꿔 줍니다. 

```zsh
$ date
2021. 06. 27. (일) 03:16:49 -09
❯ dpkg-reconfigure tzdata
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
Configuring tzdata
------------------

Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list of cities, representing the time zones in which they are located.

  1. Africa  2. America  3. Antarctica  4. Australia  5. Arctic  6. Asia  7. Atlantic  8. Europe  9. Indian  10. Pacific  11. SystemV  12. US  13. Etc
Geographic area: 6

Please select the city or region corresponding to your time zone.

  1. Aden      9. Baghdad   17. Chita       25. Dushanbe     33. Irkutsk    41. Kashgar       49. Macau         57. Omsk        65. Rangoon        73. Taipei    81. Ujung_Pandang  89. Yekaterinburg
  2. Almaty    10. Bahrain  18. Choibalsan  26. Famagusta    34. Istanbul   42. Kathmandu     50. Magadan       58. Oral        66. Riyadh         74. Tashkent  82. Ulaanbaatar    90. Yerevan
  3. Amman     11. Baku     19. Chongqing   27. Gaza         35. Jakarta    43. Khandyga      51. Makassar      59. Phnom_Penh  67. Sakhalin       75. Tbilisi   83. Urumqi
  4. Anadyr    12. Bangkok  20. Colombo     28. Harbin       36. Jayapura   44. Kolkata       52. Manila        60. Pontianak   68. Samarkand      76. Tehran    84. Ust-Nera
  5. Aqtau     13. Barnaul  21. Damascus    29. Hebron       37. Jerusalem  45. Krasnoyarsk   53. Muscat        61. Pyongyang   69. Seoul          77. Tel_Aviv  85. Vientiane
  6. Aqtobe    14. Beirut   22. Dhaka       30. Ho_Chi_Minh  38. Kabul      46. Kuala_Lumpur  54. Nicosia       62. Qatar       70. Shanghai       78. Thimphu   86. Vladivostok
  7. Ashgabat  15. Bishkek  23. Dili        31. Hong_Kong    39. Kamchatka  47. Kuching       55. Novokuznetsk  63. Qostanay    71. Singapore      79. Tokyo     87. Yakutsk
  8. Atyrau    16. Brunei   24. Dubai       32. Hovd         40. Karachi    48. Kuwait        56. Novosibirsk   64. Qyzylorda   72. Srednekolymsk  80. Tomsk     88. Yangon
Time zone: 69


Current default time zone: 'Asia/Seoul'
Local time is now:      Sun Jun 27 21:18:07 KST 2021.
Universal Time is now:  Sun Jun 27 12:18:07 UTC 2021.
```

## wrap-up

- 일단 제가 사용하는 주요 패키지들 및 설정을 적용해줬습니다. 다음에는 이걸 한번에 쭉 적용된 이미지로 만들기 위해서 dockerfile로 만들어볼 계획입니다.

## Reference

- [Linux - Docker 우분투 18.04 한글 패치 하기](https://flymogi.tistory.com/28)
- [도커(Docker) 컨테이너 로케일 설정 - 데비안(Debian), 우분투(Ubuntu) 이미지에서 한글 입력 문제](https://www.44bits.io/ko/post/setup_linux_locale_on_ubuntu_and_debian_container)
