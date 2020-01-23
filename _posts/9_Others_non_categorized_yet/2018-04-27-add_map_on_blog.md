---
title: 블로그에 map 추가하기 
category: other
tags: markdown html google-map blog

---

## intro 

- 저는 천안 사람이지만 대학교 이후에 늘 포항에서 살아왔기 때문에 천안 맛집을 잘 모릅니다. 아 디아스포라...아무튼 요 몇 달동안 집에 있게 되어 천안의 맛집과 까페와 술집들을 돌아다녀보고 있는데 이왕 다니는 거 이것도 정리를 좀 하면 좋지 않을까? 하는 생각을 했습니다. 
- 그 과정에서 다른 블로그들처럼 페이지에 지도가 표시되고 지도 안에는 `pin`이 꽂혀 있으면 좋겠다는 생각을 했습니다. 그래서 그 내용을 정리했습니다. 

### 각 지도별 차이점 

- 내가 원하는 장소에 `pin`을 꽂을 수 있는 것은 구글지도와 네이버지도 밖에 되지 않습니다. 다음지도는 이를 지원하지 않네요.
- 다만, 구글 지도는 음식점 등을 검색했을 때 없다고 나오는 경우가 있습니다. 이는 구글 맵이 한국의 정보를 충분히 가지고 있지 못해서 그런 것인데, 그렇다면 구글 맵에 직접 업로드를 하시면 좋습니다ㅎㅎㅎ
- 구글 맵만 `iframe`에 넣어서 html code를 제공하고, 나머지는 table의 형태로 지원하는데 이 차이가 무엇인지는 모르겠지만, 블로그에서 구글맵이 더 예쁘고 깔끔하게 보여지는 것은 사실입니다. 
- 그리고 구글 맵은 '지도'가 첨부되기 때문에 내부에서도 지도의 인터페이스(drag 등)이 지원되지만, 다른 맵들은 지도의 모양을 가진 "이미지"가 첨부됩니다. 해당 지도를 보려면 결국 사이트로 돌아가야 합니다.
- 결국 **역시 갓구글**

## solution 

- 구글, 네이버, 다음 모두 추가할 수 있씁니다만, 아래처럼 좀 다르네요. 
- 일단은 각각 사이트에 들어가서 찾아보면, '지도 퍼가기' 느낌의 부분이 있습니다. 거기서 `html` 코드를 그대로 복사하시면 됩니다. 
- `markdown`이라서 `html` 코드를 그대로 넣어도 괜찮을까? 생각했는데 일단은 아무 문제가 없네요. 

### 구글 지도

- 구글 맵에서 `공유` 버튼을 누른 다음 embeded 코드를 가져와서 여기에 합치면 된다. 
- 코드 내부를 보면 `width`와 `height` 등의 변수가 있는데 이를 변경할 수 있습니다.
    - 코드를 보시면 `iframe` 태그로 만들어진 것을 알 수 있습니다. 

- **code**

```html 
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12775.913897343044!2d127.14496974061093!3d36.81903572911351!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357b285b9e6c867d%3A0x94b180012706cce7!2s13+Mannam-ro%2C+Dongnam-gu%2C+Cheonan%2C+Chungcheongnam-do!5e0!3m2!1sen!2skr!4v1524815646894" width="400" height="300" frameborder="0" style="border:0" allowfullscreen>
</iframe>
```

- **result**

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12775.913897343044!2d127.14496974061093!3d36.81903572911351!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357b285b9e6c867d%3A0x94b180012706cce7!2s13+Mannam-ro%2C+Dongnam-gu%2C+Cheonan%2C+Chungcheongnam-do!5e0!3m2!1sen!2skr!4v1524815646894" width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>


### 네이버 지도

- `table`의 형태로 만들어진 `html`입니다. 그래서 그런지 좀 모양이 예쁘지 않네요. 

- **code**

```html
<table cellpadding="0" cellspacing="0" width="462"> 
    <tr> 
        <td style="border:1px solid #cecece;"><a href="http://maps.naver.com/?searchCoord=fbc6fd17ae5527ac223bdee8baf1b6b1f3da169dc9a9f4d6981977cbbd4a3dab&query=64uk7Jq07Ja4642U&tab=1&lng=f2579be10da8f527f54782fb7a9de5e5&mapMode=0&mpx=15131580%3A36.7809%2C127.1529004%3AZ11%3A0.0233057%2C0.0139049&_=&lat=1c13e908d88dce1981d18fd1174e0c62&dlevel=12&enc=b64&menu=location" target="_blank"><img src="http://prt.map.naver.com/mashupmap/print?key=p1524816568503_-100898067" width="460" height="340" alt="지도 크게 보기" title="지도 크게 보기" border="0" style="vertical-align:top;"/></a>
        </td> 
    </tr> 
    <tr> 
        <td> 
            <table cellpadding="0" cellspacing="0" width="100%"> 
                <tr> 
                    <td height="30" bgcolor="#f9f9f9" align="left" style="padding-left:9px; border-left:1px solid #cecece; border-bottom:1px solid #cecece;"> 
                        <span style="font-family: tahoma; font-size: 11px; color:#666;">2018.4.27</span>&nbsp;
                        <span style="font-size: 11px; color:#e5e5e5;">|</span>&nbsp;<a style="font-family: dotum,sans-serif; font-size: 11px; color:#666; text-decoration: none; letter-spacing: -1px;" href="http://maps.naver.com/?searchCoord=fbc6fd17ae5527ac223bdee8baf1b6b1f3da169dc9a9f4d6981977cbbd4a3dab&query=64uk7Jq07Ja4642U&tab=1&lng=f2579be10da8f527f54782fb7a9de5e5&mapMode=0&mpx=15131580%3A36.7809%2C127.1529004%3AZ11%3A0.0233057%2C0.0139049&_=&lat=1c13e908d88dce1981d18fd1174e0c62&dlevel=12&enc=b64&menu=location" target="_blank">지도 크게 보기</a> 
                    </td> 
                    <td width="98" bgcolor="#f9f9f9" align="right" style="text-align:right; padding-right:9px; border-right:1px solid #cecece; border-bottom:1px solid #cecece;"> <span style="float:right;"><span style="font-size:9px; font-family:Verdana, sans-serif; color:#444;">&copy;&nbsp;</span>&nbsp;<a style="font-family:tahoma; font-size:9px; font-weight:bold; color:#2db400; text-decoration:none;" href="http://www.nhncorp.com" target="_blank">NAVER Corp.</a></span> 
                    </td> 
                </tr> 
            </table>
        </td> 
    </tr> 
</table>
```

- **result**

<table cellpadding="0" cellspacing="0" width="462"> <tr> <td style="border:1px solid #cecece;"><a href="http://maps.naver.com/?searchCoord=fbc6fd17ae5527ac223bdee8baf1b6b1f3da169dc9a9f4d6981977cbbd4a3dab&query=64uk7Jq07Ja4642U&tab=1&lng=f2579be10da8f527f54782fb7a9de5e5&mapMode=0&mpx=15131580%3A36.7809%2C127.1529004%3AZ11%3A0.0233057%2C0.0139049&_=&lat=1c13e908d88dce1981d18fd1174e0c62&dlevel=12&enc=b64&menu=location" target="_blank"><img src="http://prt.map.naver.com/mashupmap/print?key=p1524816568503_-100898067" width="460" height="340" alt="지도 크게 보기" title="지도 크게 보기" border="0" style="vertical-align:top;"/></a></td> </tr> <tr> <td> <table cellpadding="0" cellspacing="0" width="100%"> <tr> <td height="30" bgcolor="#f9f9f9" align="left" style="padding-left:9px; border-left:1px solid #cecece; border-bottom:1px solid #cecece;"> <span style="font-family: tahoma; font-size: 11px; color:#666;">2018.4.27</span>&nbsp;<span style="font-size: 11px; color:#e5e5e5;">|</span>&nbsp;<a style="font-family: dotum,sans-serif; font-size: 11px; color:#666; text-decoration: none; letter-spacing: -1px;" href="http://maps.naver.com/?searchCoord=fbc6fd17ae5527ac223bdee8baf1b6b1f3da169dc9a9f4d6981977cbbd4a3dab&query=64uk7Jq07Ja4642U&tab=1&lng=f2579be10da8f527f54782fb7a9de5e5&mapMode=0&mpx=15131580%3A36.7809%2C127.1529004%3AZ11%3A0.0233057%2C0.0139049&_=&lat=1c13e908d88dce1981d18fd1174e0c62&dlevel=12&enc=b64&menu=location" target="_blank">지도 크게 보기</a> </td> <td width="98" bgcolor="#f9f9f9" align="right" style="text-align:right; padding-right:9px; border-right:1px solid #cecece; border-bottom:1px solid #cecece;"> <span style="float:right;"><span style="font-size:9px; font-family:Verdana, sans-serif; color:#444;">&copy;&nbsp;</span>&nbsp;<a style="font-family:tahoma; font-size:9px; font-weight:bold; color:#2db400; text-decoration:none;" href="http://www.nhncorp.com" target="_blank">NAVER Corp.</a></span> </td> </tr> </table> </td> </tr> </table>

- 네이버 지도 소스(`src`)를  `iframe`에 넣어서 다시 해보면, 더 깔끔하게 나오기는 하는데 좀 번거롭죠. 

```html
<iframe src="http://prt.map.naver.com/mashupmap/print?key=p1524816568503_-100898067" width="400" height="300" frameborder="0" style="border:0" allowfullscreen>
```

### 다음 지도

- 특정 음식점 pin을 꽂을 수 없다는 것이 아쉽네요. 

- **code**

```html
<a href="http://map.daum.net/?urlX=534287&urlY=922357&urlLevel=3&map_type=TYPE_MAP&map_hybrid=false&SHOWMARK=true" target="_blank">
    <span style="background:#000;position:absolute;width:557px;opacity:.7;filter:alpha(opacity=70);color:#fff;overflow:hidden;font:12px/1.5 Dotum, '돋움', sans-serif;text-decoration:none;padding:7px 0px 0px 10px; height: 24px;">지도를 클릭하시면 위치정보를 확인하실 수 있습니다.</span>
    <img width="565" height="308" src="http://map2.daum.net/map/mapservice?MX=534287&MY=922357&SCALE=2.5&IW=565&IH=308&COORDSTM=WCONGNAMUL" style="border:1px solid #ccc">
</a>
```

- **result**

<a href="http://map.daum.net/?urlX=534287&urlY=922357&urlLevel=3&map_type=TYPE_MAP&map_hybrid=false&SHOWMARK=true" target="_blank"><span style="background:#000;position:absolute;width:557px;opacity:.7;filter:alpha(opacity=70);color:#fff;overflow:hidden;font:12px/1.5 Dotum, '돋움', sans-serif;text-decoration:none;padding:7px 0px 0px 10px; height: 24px;">지도를 클릭하시면 위치정보를 확인하실 수 있습니다.</span><img width="565" height="308" src="http://map2.daum.net/map/mapservice?MX=534287&MY=922357&SCALE=2.5&IW=565&IH=308&COORDSTM=WCONGNAMUL" style="border:1px solid #ccc"></a>


- 다음 지도도 iframe에 소스를 넣을 수 있습니다.

```html
<iframe src="http://map2.daum.net/map/mapservice?MX=534287&MY=922357&SCALE=2.5&IW=565&IH=308&COORDSTM=WCONGNAMUL" width="400" height="300" frameborder="0" style="border:0" allowfullscreen>
```
