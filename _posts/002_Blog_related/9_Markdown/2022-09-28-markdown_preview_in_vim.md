---
title: Vim - Markdown Preview
category: markdown
tags: markdown MarkdownPreview vim mkdp vi
---

## Vim - Markdown Preview

- 저는 모든 문서 작업을 vim에서 하려고 노력합니다. 과거에는 VScode를 사용했는데요, 어떻게 하면 최대한 마우스를 쓰지 않고 작업을 할 수 있을까 고민하다 보니 현재 vim으로 넘어왔습니다. 마우스를 쓰지 않기 때문에, 꽤 번거로운 일이 생기는 경우들도 있기는 하고, 특히 front end 작업을 해야할 때, 좀 번잡스러운 일들이 있기는 하지만, Vim 에서만 모든 작업을 하는 건 묘한 쾌감 같은게 있는 것 같습니다.
- 아무튼, vim에서 markdown file을 작성하다 보면 해당 markdown file이 제대로 작성되어 있는 것인지 확신이 들지 않을 때가 있습니다. VScode에서는 바로 markdown preview extension을 사용해서 확인하면 되었는데요.
- vim에서는 [github - iamcco - markdown preview](https://github.com/iamcco/markdown-preview.nvim) 을 사용하여 해당 마크다운을 브라우저에 띄울 수 있습니다.

## Install markdown preview

- 저는 vundle을 사용하여 설치하였읍니다. `.vimrc` file 에 아래 내용을 추가합니다.

```vim
Plugin 'iamcco/markdown-preview.nvim'
```

- 그리고 vim을 실행한 다음 아래 명령어를 실행해 줍니다.

```vim
:PluginInstall
:call mkdp#util#install()
```

- 그 다음 vim 화면에서 아래를 실행하면 preview를 실행하고 중지할 수 있습니다.

```vim
:MarkdownPreview
:MarkdownPreviewStop
```

## Markdown Preview Config

- 세부적으로 아래와 같은 설정을 변경할 수 있는데요, 저는 귀찮아서 일단은 모두 그대로 두었습니다. 추후 바꾸고 싶으면 바꿔볼게요.

```vim
" set to 1, nvim will open the preview window after entering the markdown buffer
" default: 0
let g:mkdp_auto_start = 0

" set to 1, the nvim will auto close current preview window when change
" from markdown buffer to another buffer
" default: 1
let g:mkdp_auto_close = 1

" set to 1, the vim will refresh markdown when save the buffer or
" leave from insert mode, default 0 is auto refresh markdown as you edit or
" move the cursor
" default: 0
let g:mkdp_refresh_slow = 0

" set to 1, the MarkdownPreview command can be use for all files,
" by default it can be use in markdown file
" default: 0
let g:mkdp_command_for_global = 0

" set to 1, preview server available to others in your network
" by default, the server listens on localhost (127.0.0.1)
" default: 0
let g:mkdp_open_to_the_world = 0

" use custom IP to open preview page
" useful when you work in remote vim and preview on local browser
" more detail see: https://github.com/iamcco/markdown-preview.nvim/pull/9
" default empty
let g:mkdp_open_ip = ''

" specify browser to open preview page
" for path with space
" valid: `/path/with\ space/xxx`
" invalid: `/path/with\\ space/xxx`
" default: ''
let g:mkdp_browser = ''

" set to 1, echo preview page url in command line when open preview page
" default is 0
let g:mkdp_echo_preview_url = 0

" a custom vim function name to open preview page
" this function will receive url as param
" default is empty
let g:mkdp_browserfunc = ''

" options for markdown render
" mkit: markdown-it options for render
" katex: katex options for math
" uml: markdown-it-plantuml options
" maid: mermaid options
" disable_sync_scroll: if disable sync scroll, default 0
" sync_scroll_type: 'middle', 'top' or 'relative', default value is 'middle'
"   middle: mean the cursor position alway show at the middle of the preview page
"   top: mean the vim top viewport alway show at the top of the preview page
"   relative: mean the cursor position alway show at the relative positon of the preview page
" hide_yaml_meta: if hide yaml metadata, default is 1
" sequence_diagrams: js-sequence-diagrams options
" content_editable: if enable content editable for preview page, default: v:false
" disable_filename: if disable filename header for preview page, default: 0
let g:mkdp_preview_options = {
    \ 'mkit': {},
    \ 'katex': {},
    \ 'uml': {},
    \ 'maid': {},
    \ 'disable_sync_scroll': 0,
    \ 'sync_scroll_type': 'middle',
    \ 'hide_yaml_meta': 1,
    \ 'sequence_diagrams': {},
    \ 'flowchart_diagrams': {},
    \ 'content_editable': v:false,
    \ 'disable_filename': 0,
    \ 'toc': {}
    \ }

" use a custom markdown style must be absolute path
" like '/Users/username/markdown.css' or expand('~/markdown.css')
let g:mkdp_markdown_css = ''

" use a custom highlight style must absolute path
" like '/Users/username/highlight.css' or expand('~/highlight.css')
let g:mkdp_highlight_css = ''

" use a custom port to start server or empty for random
let g:mkdp_port = ''

" preview page title
" ${name} will be replace with the file name
let g:mkdp_page_title = '「${name}」'

" recognized filetypes
" these filetypes will have MarkdownPreview... commands
let g:mkdp_filetypes = ['markdown']

" set default theme (dark or light)
" By default the theme is define according to the preferences of the system
let g:mkdp_theme = 'dark'
```

## Reference

- [github - iamcco - markdown preview](https://github.com/iamcco/markdown-preview.nvim)
