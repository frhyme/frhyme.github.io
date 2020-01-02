---
title: google ad-sense를 제대로 붙여넣었습니다.
category: others
tags: google ad-sense
---

## 광고를 깔끔하게 붙여보기로 했습니다.

- 사실, 이 블로그에 사람이 그렇게 많이 들어오지는 않습니다. 그리고, 여기에 광고를 단다고해서 그게 딱히 돈이 되지도 않아요. 그 시간에 다른 일을 하는 것이 훨씬 효율적입니다. 
- 다만, 그냥 좀 궁금하잖아요. 광고는 보통 어떤 것이 붙고, 붙으면 얼마나 발생하는걸까? 와 같은 것들 말이죠. 단지 그 이유 때문에 광고를 한번 달아보기로 했습니다. 

## first try: bad

- [이 링크](https://shryu8902.github.io/jekyll/adsense/)의 내요을 참고해서 진행했습니다만, 전반적으로 블로그에 광고가 예쁘게 붙지 않았습니다. 가령, 맨 위에 너무 큼지막하게 붙는다거나, 콘텐츠 사이에 뜬금없이 광고가 나와서 콘텐츠의 질을 떨어뜨리고 가독성에 방해가 되는 것 같아요. 아시는 것처럼, 광고가 갑자기 나오면 짜증나시잖아요? 이게 별로 좋은 광고 배치 방식으로 보이지 않았어요. 

## second try: better.

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

### add ad-sence(side-bar)

- 이제 같은 방식으로 사이드바에 광고를 설치해줍니다. 
- 우선 구글 애드센스에서 광고 단위를 만들어주고, 그 다음, 여기서 만들어진 코드를 `_includes/GoogleAdSenseSidbar.html`를 만들어서 넣어줍니다. 사실, 매번 특정한 html 코드를 가져와서 다른 포스트에서 embed해서 쓰는 것이 훨씬 효율적이니까요. 그래서 이런식으로 만들어두고. 
- `_layouts/single.html`에서 찾아보면, `toc`에 대한 요소가 작성된곳이 있습니다. 다 아시겠지만, `single.html`은 포스트되는 글들이 기본적으로 참조하는 글의 형식이죠. 따라서, 여기의 내용들이 바뀌면, 모든 글들의 형식이 바뀌게 됩니다.

- 원래는 해당 요소의 코드는 다음과 같이, 작성되어 있습니다만, 

```html 
{% raw %}
{% if page.toc %}
<aside class="sidebar__right {% if page.toc_sticky %}sticky{% endif %}">
    <nav class="toc">
        <header>
            <h4 class="nav__title">
                <i class="fas fa-{{ page.toc_icon | default: 'file-alt' }}"></i> {{ page.toc_label | default: site.data.ui-text[site.locale].toc_label | default: "On this page" 
            </h4>
        </header>
    {% include toc.html sanitize=true html=content h_min=1 h_max=6 class="toc__menu" %}
    </nav>
</aside>
{% endif %}
{% endraw %}
```

- 이런 형태로 바뀌게 되죠. 의미를 대충 보면, toc 혹은 toc_ads가 트루이면, `GoogleAdSenseSidbar.html`로부터 html 코드를 가져와서 붙인다는 말입니다. 

```html
{% raw %}
{% if page.toc or page.toc_ads %}
    <aside class="sidebar__right {% if page.toc_sticky %}sticky{% endif %}">
        <nav class="toc">
            {% if page.toc %}
            <header>
                <h4 class="nav__title">
                    <i class="fas fa-{{ page.toc_icon | default: 'file-alt' }}"></i> {{ page.toc_label | default: site.data.ui-text[site.locale].toc_label }}
                </h4>
            </header>
            {% include toc.html sanitize=true html=content h_min=1 h_max=6 class="toc__menu" %} {%  endif %}
        </nav>
        <!-- devinlife comment : right-sidebar ads -->
        <nav class="toc-custom">
        {% if page.toc_ads %} {% include GoogleAdSenseSidbar.html %} {% endif %}
        </nav>
    </aside>
{% endif %}
{% endraw %}
```

- 그리고 `_config.yml`부분의 코드도 변경해줍니다. 여기서는 두 가지 변수를 변경해주는데, 아래와 같이 `toc`에 대한 부분이 작성된 곳에 나머지를 붙여주면 됩니다. 

## wrap-up

- 이렇게 변경했는데도 불구하고, 반복적으로 중간에 광고가 들어가고는 합니다. 사이드바에도 잘 들어가고, 아래쪽에도 잘 들어갔는데, 왜 중간에 광고가 들어가는건지 이해가 안되는군요. 일단은, 그냥 이전의 소스들이 아직 완전하게 덮어진 것이 아니라고 생각하고 있기는 한데, 아지은 잘 모르겠습니다.


## reference

- [footer, sidebar에 광고달기](https://devinlife.com/howto%20github%20pages/adsense/)