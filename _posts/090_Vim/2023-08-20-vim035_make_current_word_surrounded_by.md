---
title: vim035 - make current word surrounded by
category: vim
tags: vim vi markdown
---

## vim035 - make current word surrounded by

- While writing Markdown in Vim, I find the process of formatting words to appear as code, enclosed by backtick characters, to be quite cumbersome. To achieve this, I need to follow these steps:
1. In normal mode, position the cursor at the beginning of the word.
1. Switch to insert mode and type the opening backtick.
1. Return to normal mode and navigate the cursor to the end of the word.
1. Reenter insert mode and type the closing backtick.

- Doing these steps can be quite tedious and frustrating. Additionally, there are instances where these steps need to be repeated multiple times for a single Markdown file, which can be disheartening. Therefore, I've been actively seeking a solution to address this through a shortcut.
- A more efficient way to enclose a word with backtick characters can be achieved using the following command in normal mode:

```vim
ciw``<ESC>P
```

- `ciw`: This command changes the content of the word under the cursor. It doesn't delete the entire word from the buffer, but rather removes the content of the word while leaving an empty word in its place. The removed content is stored in the default register.
- Use the `backtick` character twice: In my scenario, I intend to enclose the target word with backtick characters, so I should type the backtick character twice. However, if your intention is to use a different character such as a single quote, make sure to replace the backticks with the desired character.
- `<ESC>`: This is the Escape key, used to exit insert mode and return to normal mode in Vim.
- `P`: This command pastes the text stored in the default register before the cursor position. In this case, it pastes the content of the word that was changed using the `ciw` command.

- However, manually typing that command is still a bit cumbersome. To streamline the process, I've registered it as an auto command in my Vim configuration, as demonstrated below.
- As the code snippet illustrates, by simply typing `__sbt` in normal mode, the word under the cursor becomes encased within backticks. This enhancement saves time and effort during editing.

```vim
" 2023-08-20 (Sun): markdown make target word with surrounded by backtick
autocmd FileType markdown nnoremap __sbt ciw``<ESC>Pw
```

## Reference

- [stackexchange - vimscript - surround word under cursor with quotes](https://vi.stackexchange.com/questions/21113/vimscript-surround-word-under-cursor-with-quotes/21119#21119?newreg=7c17970b304e42ba883c36fcc335bb94)
