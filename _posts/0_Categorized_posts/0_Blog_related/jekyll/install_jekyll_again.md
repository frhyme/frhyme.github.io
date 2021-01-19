---
title: 
category: 
tags: 
---

## Install Jekyll

- jekyll을 설치합니다. 
- 현재는 jekyll을 설치하지 않은 상태죠. 깃헙에서 jekyll을 사용해서 정적으로 페이지를 생성해주기 때문에, 사실 jekyll이 내부에 없어도 큰 문제가 없기는 함.
- 그러나, 로컬에서 현재 진행 상황을 파악하면서 로컬 서버를 만들어서 웹피이지가 어떻게 생성되는지를 파악하면서 진행하고 싶다면, 이렇게 하지 않고 내부에 jekyll을 설치하여 진행할 수 있습니다.
- ruby를 설치하고, 이미 ruby가 깔려 있다. 언제 깔았지??
  - dd





```
(base) seunghoonlee@seunghoonui-MacBookAir ~ % ruby -v
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

- jekyll을 설치합니다. 흠...안되는데 흠...

```
(base) seunghoonlee@seunghoonui-MacBookAir ~ % gem install --user-install bundler jekyll

Fetching bundler-2.2.5.gem
WARNING:  You don't have /Users/seunghoonlee/.gem/ruby/2.6.0/bin in your PATH,
	  gem executables will not run.
Successfully installed bundler-2.2.5
Parsing documentation for bundler-2.2.5
Installing ri documentation for bundler-2.2.5
Done installing documentation for bundler after 2 seconds
Fetching addressable-2.7.0.gem
Fetching colorator-1.1.0.gem
Fetching eventmachine-1.2.7.gem
Fetching http_parser.rb-0.6.0.gem
Fetching em-websocket-0.5.2.gem
Fetching public_suffix-4.0.6.gem
Fetching concurrent-ruby-1.1.7.gem
Fetching i18n-1.8.7.gem
Fetching ffi-1.14.2.gem
Fetching sassc-2.4.0.gem
Fetching jekyll-sass-converter-2.1.0.gem
Fetching rb-fsevent-0.10.4.gem
Fetching rb-inotify-0.10.1.gem
Fetching listen-3.4.1.gem
Fetching jekyll-watch-2.2.1.gem
Fetching kramdown-2.3.0.gem
Fetching kramdown-parser-gfm-1.1.0.gem
Fetching liquid-4.0.3.gem
Fetching mercenary-0.4.0.gem
Fetching forwardable-extended-2.6.0.gem
Fetching pathutil-0.16.2.gem
Fetching rouge-3.26.0.gem
Fetching safe_yaml-1.0.5.gem
Fetching unicode-display_width-1.7.0.gem
Fetching jekyll-4.2.0.gem
Fetching terminal-table-2.0.0.gem
Successfully installed public_suffix-4.0.6
Successfully installed addressable-2.7.0
Successfully installed colorator-1.1.0
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.

    current directory: /Users/seunghoonlee/.gem/ruby/2.6.0/gems/eventmachine-1.2.7/ext
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/bin/ruby -I /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0 -r ./siteconf20210119-69963-1b24eug.rb extconf.rb
checking for -lcrypto... *** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
	--with-opt-dir
	--without-opt-dir
	--with-opt-include
	--without-opt-include=${opt-dir}/include
	--with-opt-lib
	--without-opt-lib=${opt-dir}/lib
	--with-make-prog
	--without-make-prog
	--srcdir=.
	--curdir
	--ruby=/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/bin/$(RUBY_BASE_NAME)
	--with-ssl-dir
	--without-ssl-dir
	--with-ssl-include
	--without-ssl-include=${ssl-dir}/include
	--with-ssl-lib
	--without-ssl-lib=${ssl-dir}/lib
	--with-openssl-config
	--without-openssl-config
	--with-pkg-config
	--without-pkg-config
	--with-cryptolib
	--without-cryptolib
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:467:in `try_do': The compiler failed to generate an executable file. (RuntimeError)
You have to install development tools first.
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:546:in `block in try_link0'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/tmpdir.rb:93:in `mktmpdir'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:543:in `try_link0'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:570:in `try_link'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:789:in `try_func'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:1016:in `block in have_library'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:959:in `block in checking_for'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:361:in `block (2 levels) in postpone'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:331:in `open'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:361:in `block in postpone'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:331:in `open'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:357:in `postpone'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:958:in `checking_for'
	from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/mkmf.rb:1011:in `have_library'
	from extconf.rb:8:in `block in check_libs'
	from extconf.rb:8:in `all?'
	from extconf.rb:8:in `check_libs'
	from extconf.rb:95:in `<main>'

To see why this extension failed to compile, please check the mkmf.log which can be found here:

  /Users/seunghoonlee/.gem/ruby/2.6.0/extensions/universal-darwin-19/2.6.0/eventmachine-1.2.7/mkmf.log

extconf failed, exit code 1

Gem files will remain installed in /Users/seunghoonlee/.gem/ruby/2.6.0/gems/eventmachine-1.2.7 for inspection.
Results logged to /Users/seunghoonlee/.gem/ruby/2.6.0/extensions/universal-darwin-19/2.6.0/eventmachine-1.2.7/gem_make.out
1 gem installed
```


- 근데 일단 설치가 안된다. 이건 아마도, 현재 내가 로컬에 설치할 수 있는 권한이 없어서 그런 것으로 보이는데.
- 

## Reference

- [맥OS 에 Jekyll 설치](https://jekyllrb-ko.github.io/docs/installation/macos/)
