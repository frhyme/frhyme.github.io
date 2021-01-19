---
title: 왜 jekyll serve가 안될까? 
category: others
tags: jekyll server blog
---

## 요즘 블로그를 좀 뜯어 고치고 있습니다

- 블로그를 만든 게 약 1년 반정도가 되었습니다. 초기에 이런저런 세팅을 다 해두고, 이후에는 거의 그냥 마크다운으로 글만 써서 올리는 형태로 지속해왔습니다. 
- 그러던 중에, 최근에는 광고를 달아봤습니다. 사실, 광고로 버는 돈은 매우 적고, 이 광고가 오히려 블로그를 보시는 분들에게는 더 귀찮고 번거로운 일이 될 수도 있겠죠.
- 그런데, 솔직히 저는 좀 궁금했습니다. 내가 지금까지 블로그에 써온 글들이 수익적으로 어떤 의미가 있는 것일까? 또한, 내가 이런 종류의 글쟁이로 직업을 가져가는 것은 가능한 것일까? 라는 것들이요. 간단히 말하면, 이걸로 밥 내가 밥 먹이를 할 수 있을까? 라는 것들이죠. 
- 그래서 광고를 달아놓고 보니, 솔직히 제 블로그가 너무 더럽게 느린 거에요. 광고때문이 아니라 원래도 느렸습니다만, 이전에는 크게 신경쓰지 않았는데, 너무 느린거죠. 그래서 전반적으로 이전에 했던 튜닝을 모두 제외하고, 모두 순정의 상태로 되돌리는 작업을 하고 있었습니다. 그런데. 

## 왜 jekyll serve가 안되는걸까요? 

- 원래는 제 로컬에서 `jekyll serve`를 통해서 로컬에서 4000 번 포트로 접근해서 블로그의 바뀐 모습을 적용해볼 수가 있었습니다. 그런데, 갑자기 이게 안되는 거죠. `bundle exec jekyll serve`로 실행을 하면 되긴 되는데, 좀 느리고 번거로워요. 그래서, 이걸 그냥 무시할까 하다가, 아 어떻게든 고쳐야 내 마음이 편하겠다 싶어서 고쳐버리기로 했습니다. 
- 우선 `jekyll serve`를 그냥 명령하면, 다음과 같은 결과가 나옵니다. 

```plaintext 
Leeseunghoonui-MacBook-Air:frhyme.github.io frhyme$ jekyll serve
Traceback (most recent call last):
	10: from /usr/local/bin/jekyll:23:in `<main>'
	 9: from /usr/local/bin/jekyll:23:in `load'
	 8: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/exe/jekyll:11:in `<top (required)>'
	 7: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/lib/jekyll/plugin_manager.rb:52:in `require_from_bundler'
	 6: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler.rb:107:in `setup'
	 5: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `setup'
	 4: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `map'
	 3: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
	 2: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
	 1: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:31:in `block in setup'
/Library/Ruby/Gems/2.6.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:319:in `check_for_activated_spec!': You have already activated i18n 1.7.0, but your Gemfile requires i18n 0.9.5. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)
```

- 해석을 해보자면, **너는 벌써, i18n 1.7.0.이 활성화되어 있는데, 너의 Gemfile들은 i18n 0.9.5. 를 필요로 해. 그러니까, 이걸 해결하려면 `bundle exec`를 니 명령어 앞에 붙여서 실행해** 라는 말이죠. 
- 물론, 여기서 말한 것과 같이 `bundle exec jekyll serve`로 실행해도 실행은 됩니다. 

## remind what I knew before

- 전에 배운 것들을 좀 간단하게라도 정리해보겠습니다. 
- `Gem`: 루비에서 지원하는 라이브러리 관리 시스템입니다. pip, conda, 같은 것들이 모두 여기에 속하죠. 즉, `gem install`과 같은 방식으로 필요한 라이브러리들을 다운받아서 사용할 수 있습니다. 
- `Gemfile`: 필요한 Gem들의 규격(스펙)들이 정리된 명세서입니다.
- `bundler`: [ruby-korea](https://ruby-korea.github.io/bundler-site/v1.5/)에 정의된 바에 따르면, '번들러는 루비 애플리케이션을 위한 일관된 환경을 제공하는데, 필요한 루비젬을 추적하여, 어플리케이션이 항상 정확한 gem과 버전을 쓰도록 환경을 설정하는 것'을 의미합니다. 즉, 앞에서 `bundle exec`를 앞에 붙여서 명령어를 실행한다면, 해당 라이브러리를 사용하는데 필요한 모든 의존성을 해결하고 그 환경에 맞춰서 실행하도록 한다는 것을 의미하죠. 사실, 이렇게 해도 됩니다만, 저는, 아예 현재 시스템 자체를 뜯어고치고 싶거든요. 
- `Gemfile.lock`: 젬파일.락 은 번들러가 실행되었을 때 해당 라이브러리를 구동하기 위해서 필요한 정확한 다른 라이브러리들의 버전을 저장해둔 것을 말합니다. 즉, 제가 만약 `bundle install`을 현재 지킬이 설치되어 있는 라이브러리에서 실행한다면, `Gemfile.lock`에 정리되어 있는 규격으로부터 정확한 자료를 가져와서, 실행한다는 것이죠. 마찬가지로 `bundle exec`를 실행한다고 해도, `Gemfile.lock`에 저장되어 있는 규격으로부터 관련 라이브러리들을 아주 정확하게 가져와서, 실행한다는 것을 의미합니다.
- 이걸 좀 더 정확하게 보면, Gemfile은 다음과 같고, 

```plaintext
source "https://rubygems.org"

gem "jekyll", "~> 3.5"
gem "minimal-mistakes-jekyll"
```

- `Gemfile.lock`부분은 대략 다음과 같습니다. 내용이 길어서, 일부분만 가져왔고, 다음처럼 `jekyll`을 실행하려면, 필요한 다른 라이브러리들의 규격이 다음과 같다는 것을 정리해둔 것이죠. 

```plaintext
jekyll (3.8.6)
	addressable (~> 2.4)
	colorator (~> 1.0)
	em-websocket (~> 0.5)
	i18n (~> 0.7)
	jekyll-sass-converter (~> 1.0)
	jekyll-watch (~> 2.0)
	kramdown (~> 1.14)
	liquid (~> 4.0)
	mercenary (~> 0.3.3)
	pathutil (~> 0.9)
	rouge (>= 1.7, < 4)
	safe_yaml (~> 1.0)
```

- 위 `jekyll`을 실행하기 위해서 정리된 규격 중에서 `i18n`이라는 라이브러리가 눈에 띕니다. 앞서 나온 에러메세지가 여기서 출발했고, 실제로 `Gemfile.lock`의 다른 코드를 보면 다음과 같이 작성되어 있습니다. 즉, 현재 Gemfile.lock에 i18n (0.9.5)가 정의되어 있기 때문에, 이 버전이 실행되어야 하는데, 저는 i18n 1.7.0이 이미 활성화되어 있다는 것이죠. 

```plaintext
i18n (0.9.5)
	concurrent-ruby (~> 1.0)
```

- 그렇다면, i18n을 그냥 지워버리면 되는 것 아닐까요? 

## uninstall i18n 

일단 [i18n](https://rubygems.org/gems/i18n/versions/0.7.0)이 뭔가 하고 찾아봤더니, 

> Internationalization (i18n) library for Ruby

이라고 합니다. 흠, 더, 무슨 말인지 알 도리가 없네요. 그냥 지워버리기로 합니다. 

기존에 깔려 있는 라이브러리를 지우고, jekyll의 규격에 맞춰서 업데이트를 진행합니다. 

이렇게 하고 나면, i18n에 대해서 Gemfile.lock에 정의된 규격대로, 다운이 됩니다. 네 필요한 i18n 0.9.5. 버전이 설치되죠. 

```plaintext
sudo gem uninstall i18n
bundle update jekyll 
```

```plaintext
Installing i18n 0.9.5
Using rb-fsevent 0.10.3
Using rb-inotify 0.10.0
Using sass-listen 4.0.0
Using sass 3.7.4
Using jekyll-sass-converter 1.5.2
Using listen 3.2.1
Using jekyll-watch 2.2.1
Using kramdown 1.17.0
Using liquid 4.0.3
Using mercenary 0.3.6
Using pathutil 0.16.2
Using rouge 3.14.0
Using safe_yaml 1.0.5
Using jekyll 3.8.6
Using jekyll-feed 0.13.0
Using sawyer 0.8.2
Using octokit 4.14.0
Using jekyll-gist 1.5.0
Using jekyll-include-cache 0.2.0
Using jekyll-paginate 1.1.0
Using jekyll-sitemap 1.4.0
Using minimal-mistakes-jekyll 4.17.2
Bundler attempted to update jekyll but its version stayed the same
Bundle updated!
```

- 그리고 이제 실행을 해봅니다. 

```plaintext
jekyll serve 
```

- 그러니까, 이제 비슷한데 다른 라이브러리, `jekyll-sass-converter`가 버전이 다르다고 하네요. 즉, 제 Gemfile.lock에서 정의된 규격은 1.5.2 인데, 실제로는 2.0.1이 실행되고 있다는 것이죠. 
- 따라서, 다시 저걸 지우고, 번들링으로 깔아주면 되는 것이 아닐까 싶습니다. 

```plaintext
Traceback (most recent call last):
	10: from /usr/local/bin/jekyll:23:in `<main>'
	 9: from /usr/local/bin/jekyll:23:in `load'
	 8: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/exe/jekyll:11:in `<top (required)>'
	 7: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/lib/jekyll/plugin_manager.rb:52:in `require_from_bundler'
	 6: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler.rb:149:in `setup'
	 5: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/runtime.rb:26:in `setup'
	 4: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/runtime.rb:26:in `map'
	 3: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/spec_set.rb:147:in `each'
	 2: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/spec_set.rb:147:in `each'
	 1: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/runtime.rb:31:in `block in setup'
/Library/Ruby/Gems/2.6.0/gems/bundler-2.1.0/lib/bundler/runtime.rb:312:in `check_for_activated_spec!': You have already activated jekyll-sass-converter 2.0.1, but your Gemfile requires jekyll-sass-converter 1.5.2. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)
```

- 지우고 다시 깔아줍니다. 

```plaintext
sudo gem uninstall jekyll-sass-converter
sudo bundle update jekyll-sass-converter
```

- 네, 다시 잘 깔렸습니다. 

```plaintext
Installing jekyll-sass-converter 1.5.2
```

- 그리고, 다시 `jekyll serve`를 실행해 보니, 이번에는 다른 에러 메세지가 발생합니다. 
- 정리하자면, ruby 2.6.0 버전에 정의된 스펙에서는 jekyll-sass-converter이 2.0보다 커야 한다고 하는데, 니가 지금 설치한 버전은 1.5.2. 버전이다. 따라서, `Gem::MissingSpecVersionError`이 실행되었다. 더 정보가 필요하면, `gem env`를 실행하라고 되어있네요. 실행해보기로 합니다.

```plaintext
System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/dependency.rb:313:in `to_specs': Could not find 'jekyll-sass-converter' (~> 2.0) - did find: [jekyll-sass-converter-1.5.2] (Gem::MissingSpecVersionError)
Checked in 'GEM_PATH=/Users/frhyme/.gem/ruby/2.6.0:/Library/Ruby/Gems/2.6.0:/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0', execute `gem env` for more information
```

- 어쩌라는 건지....Gem과 jekyll에서는 필요로 하는 버전이 다릅니다 호호호호호. 

## wrap-up 및 포기

- 네 포기했습니다. 그냥 `bundle exec jekyll serve`를 사용해서, 따로 처리해주기로 했습니다.
- 뭐, 조금 더 공부를 하면 더 정확하게 할 수도 있을텐데, 그정도의 시간은 없어요. 그래도 오늘 한일들을 정리해보자면, 
  - 루비는 gem별로 필요로 하는 라이브러리들이 다르고, 그건 bundle을 통해서 관리될 수 있다. 
  - 즉 `bundle update jekyll`등을 통해서 지킬에서 필요로 하는 젬들의 버전을 일괄적으로 다운받을 수 있으며, 그 내용은 `Gemfile.lock`에 저장된다. 
  - 따라서, 같은 버전일지라도 그냥 깔려 있는 gem과 특정 라이브러리에서 필요로 하는 gem의 버전이 다를 경우 그냥 실행해서는 실행이 안될 수 있다. 
  - 이는, `bundle exec`를 앞에 붙이고 시작할 경우, 해당 젬을 실행하기 위해 필요한 정확한 라이브러리들을 가져와서 (일종의 가상환경이라고 생각해도 될듯) 실행하게 해준다. 이렇게 하면 되기는 함.
- 아무튼, 그냥 `bundle exec`쓰겠습니다 호호호
