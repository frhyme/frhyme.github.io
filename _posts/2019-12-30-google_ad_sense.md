---
title: google ad-sense를 제대로 붙여넣었습니다.
category: others
tags: google ad-sense
---

## 광고를 깔끔하게 붙여보기로 했습니다.

- 사실, 이 블로그에 사람이 그렇게 많이 들어오지는 않습니다. 그리고, 여기에 광고를 단다고해서 그게 딱히 돈이 되지도 않아요. 그 시간에 다른 일을 하는 것이 훨씬 효율적입니다. 
- 다만, 그냥 좀 궁금하잖아요. 광고는 보통 어떤 것이 붙고, 붙으면 얼마나 발생하는걸까? 와 같은 것들 말이죠. 단지 그 이유 때문에 광고를 한번 달아보기로 했습니다. 

## first try: 

- [이 링크](https://shryu8902.github.io/jekyll/adsense/)의 내요을 참고해서 진행했습니다만, 전반적으로 블로그에 광고가 예쁘게 붙지 않았습니다. 가령, 맨 위에 너무 큼지막하게 붙는다거나, 콘텐츠 사이에 뜬금없이 광고가 나와서 콘텐츠의 질을 떨어뜨리고 가독성에 방해가 되는 것 같아요. 아시는 것처럼, 광고가 갑자기 나오면 짜증나시잖아요? 이게 별로 좋은 광고 배치 방식으로 보이지 않았어요. 

## second try: 

- 그래서, [footer, sidebar에 광고달기](https://devinlife.com/howto%20github%20pages/adsense/)의 블로그를 보고 참고해서 진행했습니다. 

### Google Ad-sense에서 코드 가져오기.

- 일단 Google Ad-sense에서 코드를 가져옵니다. 제 코드는 다음과 같죠. 

```html
<script data-ad-client="ca-pub-8703268960755247" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">
</script>
```

- 그리고 블로그에서는 이 내용을 본문의 `_includes/head/custom.html`에 다음과 같이 집어넣으라고 되어 있습니다. 하라는 대로, 해줍니다.
- 그냥 가져온 코드와 다음 부분에서 미묘하게 다른 것을 알 수 있습니다. 제시받은 코드를 그냥 그대로 넣어주면, 웹사이트에서 알아서 코드가 막 뜨는 것 같은데, 아래처럼 코드를 변경해서 쓸 경우에는, 광고가 막 뜨지는 않는 것 같아요. 그리고 필요한 부분에 광고를 정의해주는 것이죠.

```html 
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-8703268960755247",
          enable_page_level_ads: true
     });
</script>
```

### add ad in footer. 

- 이제, 모든 html 페이지에서 header부분에 제 구글 애드센스 코드를 집어넣었습니다. 
- 그러나, 아직 어떤 광고가 어떻게 뜰지에 대해서는 정의하지 않았죠. 즉, 무슨 광고를 어떻게 넣을 것인가? 를 집어넣어줍니다.
- 저는, 웹페이지의 마지막 부분에만 광고가 뜨면 좋겠습니다. 
- 구글 애드센스에서, 광고의 형태는 **텍스트/디스플레이**, **사각형**으로 광고 크기는 **반응형**으로 하여, 광고를 만들어줍니다. 
- 그러면, 다음과 같은 코드를 만들어줍니다. 그리고 이를 `_includes/footer/custom.html` 에 일괄적으로 넣어줍니다.

```html 
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- footer-ad -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8703268960755247"
     data-ad-slot="1181380610"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```


## reference

- <https://shryu8902.github.io/jekyll/adsense/>
- [footer, sidebar에 광고달기](https://devinlife.com/howto%20github%20pages/adsense/)