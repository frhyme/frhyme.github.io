---
title: slideshare에서 한글 폰트를 읽지 못할 때 
category: others
tags: slideshare korean font ppt powerpoint mac macos
---

## 슬라이드쉐어에서 한글폰트를 못 읽습니다.

- 아마도 이 경우에 이 문제를 겪으신 분은 mac을 쓰고 계실 확률이 높습니다. 
- 저의 경우는 mac에서 파워포인트로 작업을 하고(물론 왜 맥에서 파워포인트를 쓰냐? 라고 묻는다면 할말이 없습니다만...그런데 연구실이나 다른 사람들이랑 작업 파일이 공유될 때는 아무래도 파워포인트가 도미넌트한 툴이다보니까 이걸 많이 쓰게 되는 것 같아요), 그 자료를 슬라이드쉐어에 올리거나 할 일이 많습니다. 
- 그래서 어쩔 수 없이 mac에서 파워포인트로 작업을 하고, 그 자료를 슬라이드쉐어에 올리는데, 
    - ppt 파일을 그대로 올림: 잘 올라오는데 한글폰트가 굴림체 같은 이상한 걸로 다 바뀜
    - pdf로 변환해서 올림: 한글이 모두 인식이 안되서 표시되지 않음 
- 이라는 문제들이 발생하게 되죠. 즉 맥에서는 어떻게 해도 이게 잘 안된다는 이야기입니다. 
- 단 사용하는 폰트에 따라서 다를 수 있습니다. [슬라이드쉐어에서 가능한 한글폰트](http://blog.softdevstory.net/개발/2016/10/31/pdf_for_slideshare/)에 잘 정리되어 있습니다. 

## 해결방법

- 윈도우에서 합니다. 가 아니고 

- 찾아보면 이걸 처리하는 쉘스크립트를 만드신 분이 있습니다. [여기서](https://item4.github.io/2016-10-31/Way-to-Use-Homeland-Fonts-on-SlideShare/) 자세한 내용을 보실 수 있구요. 
- 아래 쉘스크립트를 사용해서 pdf 파일의 내부 내용을 변경해주면 된다고 하던데요. 

```
LANG=C LC_ALL=C sed -i '' s'|/Registry (Adobe) /Ordering (Korea1) /Supplement [0-9]|/Registry(Adobe) /Ordering(Identity) /Supplement 0|g' /path/to/pdf.pdf
```

- 제가 잘못한 것일지도 모르지만, 저는 안되었습니다 하하하핫. 

- 다른 분께서 [여기에서](https://github.com/softdevstory/pdfForSlideshare) 간단한 오픈소스 프로젝트를 만들어서 설치하고 맥의 automator를 이용해서 사용하는 간단한 해결방법을 제시했는데요, 음. 저는 이거까지 해보지는 않았습니다. 

- 나중에 필요할 수 있으니 일단 여기에 적어두기만 합니다 하하핫. 