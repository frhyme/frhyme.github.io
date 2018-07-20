---
title: related post 더 잘 찾도록 만들기
category: others
tags: jekyll blog html plugin
---

## Is it really related posts?

- 제 블로그는 지킬로 만들어졌습니다. 정확히는 (몇 가지 규칙에 따라서) 만들어진 포스트들이 콘텐츠로 존재하고, 이를 지킬과 테마를 사용하여 렌더링해서 블로그로 보여집니다.
- 뭐, 제가 직접 만드는 것에 비해서는 월등히 좋으니까 다 좋긴 한데, 아쉬운 것이 포스트 아래에 있는 **related** 콘텐츠입니다.
- 저는 비교적 단순하게 알아서 적당한 알고리즘으로(하다못해 키워드 유사도라도 해서) 찾아주는 것인줄 알았는데, 여기에는 그냥 가장 최근에 올린 포스트들이 쭉 나열되어 있습니다.
- "몇 달 전에 쓴 포스트 아래 에서 추천해주는 포스트들 == 오늘 쓴 포스트 아래에서 추천해주는 포스트들" 인 상황인 것이죠.
- 사람들이 들어와서 다른 포스트도 보게 하려면, 즉 bounce rate를 낮추려면 이 추천해주는 알고리즘이 좀 더 좋아야 합니다.

- 제 (이기적인) 생각으로는 이를 잘 만들어둔 플러그인이나 뭐가 있지 않을까요?(먼산)

## single.html

- 우선 제 포스트를 렌더링하는 템플릿을 체크해봅니다. 맨 아래 쪽에 related post가 있는 부분이 있습니다.

```html
{% raw %}
{% comment %}<!-- only show related on a post page when `related: true` -->{% endcomment %}
 {% if page.id and page.related and site.related_posts.size > 0 %}
   <div class="page__related">
     <h4 class="page__related-title">{{ site.data.ui-text[site.locale].related_label | default: "You May Also Enjoy" }}</h4>
     <div class="grid__wrapper">
       {% for post in site.related_posts limit:4 %}
         {% include archive-single.html type="grid" %}
       {% endfor %}
     </div>
   </div>
 {% comment %}<!-- otherwise show recent posts if no related when `related: true` -->{% endcomment %}
 {% elsif page.id and page.related %}
   <div class="page__related">
     <h4 class="page__related-title">{{ site.data.ui-text[site.locale].related_label | default: "You May Also Enjoy" }}</h4>
     <div class="grid__wrapper">
       {% for post in site.posts limit:4 %}
         {% include archive-single.html type="grid" %}
       {% endfor %}
     </div>
   </div>
 {% endif %}
{% endraw %}
```

- 다음 두 가지로 구분되어 있습니다.
   - `site.related_posts`가 있는 경우
   - `site.related_posts`가 없는 경우 

- 즉, `site.related_posts`를 만들어 주면 알아서 잘 찾아서 보여준다 라고 해석할 수 있겠네요. 그래서 이걸 검색해보았습니다.

## site.related_posts

- [이 링크](https://jekyllrb.com/docs/variables/)를 보다보면 `site.related_posts` 부분에 다음과 같은 내용이 작성되어 있습니다.

> If the page being processed is a Post, this contains a list of up to ten related Posts. By default, these are the ten most recent posts. For high quality but slow to compute results, run the  jekyll command with the --lsi (latent semantic indexing) option. Also note GitHub Pages does not support the lsi option when generating sites.

- 뭐, 페이지를 포스트로 처리해줄 때, 관련된 related post를 찾아준다는 것이죠. 원래는 그냥 가장 최근 포스트로 세팅하는데, `jeklyll build --lsi`를 실행해주면, latent semantic indexing을 사용하여 `related_posts`를 세팅해준다 라고 해석하면 되겠죠.

## --lsi

- 그래서 `--lsi`를 찾아보니 [이 링크](https://jekyllrb.com/docs/configuration/)가 나왔습니다.

> Produce an index for related posts. Requires the classifier-reborn plugin.

- 설치하도록 합니다.

## plugin - classifier-reborn

- [여기](https://www.classifier-reborn.com)를 참고하시면 됩니다.
- 순서대로

- `Gemfile`을 열어서 아래 부분을 넣어주고

```
gem 'classifier-reborn'
```

- 터미널에서 다음을 순서대로 수행합니다. 저는 다음만 수행했는데도 문제없이 되었습니다만, 만약 문제가 있다면 해당 링크로 들어가서 확인해보시면 좋을 것 같아요.

```bash
$ bundle install
```

## build

- 자 이제 만들어봅시다.

```bash
jekyll build --lsi
```

- 다만, 시간이 아주 오래걸립니다. 맥북에어가 죽으려고 합니다....아무래도 콘텐츠의 양이 많아서 그런것 같기도 한데....

- 너무 오래 걸려서 찾아보니, [이 포스트](https://footle.org/2014/11/06/speeding-up-jekylls-lsi/)에서는 다음 두 커맨드를 실행하고 하면 훨씬 빨라진다고 하더군요.

```bash
brew install gsl
gem install rb-gsl
```

- pm 20:57분에 다시 시작해보는데, 정말 빨라지는지 모르겠군요 흠.

```
jekyll build --lsi
```

- 이전에는 정말 3시간이 걸려도 안 끝났는데, 이제는 2시간 조금 넘으니까 끝났습니다. 크...

```
Leeseunghoonui-MacBook-Air:frhyme.github.io frhyme$ jekyll serve --lsi
Configuration file: /Users/frhyme/frhyme.github.io/_config.yml
           Source: /Users/frhyme/frhyme.github.io
      Destination: /Users/frhyme/frhyme.github.io/_site
Incremental build: disabled. Enable with --incremental
     Generating...
 Populating LSI...
Rebuilding index...
                   done in 149.467 seconds.
Auto-regeneration: enabled for '/Users/frhyme/frhyme.github.io'
   Server address: http://127.0.0.1:4000
 Server running... press ctrl-c to stop.
```


## 그러나....

- 블로그 속도가 현저하게 느려지고, 깃헙페이지에서는 이러한 related-post가 적용되지 않는 다는 것을 깨달았습니다...

- 다시 원래대로 돌아가야 할 것 같아요.

## wrap-up

- 그 외에도 몇 가지 방법은 있습니다만, 제가 볼 때 뭔가 부족한 부분이 있는 것 같아서 우선 제외하였어요. 제가 한 방법은 가장 올바른 방법인 것 같아요.

- 다만, 이 세팅을 하고 났더니 웹페이지가 조금 늦게 열리는 것 같은 기분이 있어요. 나중에 체크해봐야할 것 같아요. 아니 확실히 늦게 열리네요. 지금 설치한 부분을 오히려 삭제하는 편이 더 좋을 수도 있을 것 같아요.


## reference

- <https://www.classifier-reborn.com>
- <https://jekyllrb-ko.github.io/docs/plugins/>
- <https://jekyllrb.com/docs/configuration/>
- <https://blog.webjeda.com/jekyll-related-posts/>
- <https://github.com/alfanick/jekyll-related-posts>
- <https://jekyllrb.com/docs/variables/>

