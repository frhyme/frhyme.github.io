---
title: vim033 - linebreak showbreak
category: vim
tags: vim vi linebreak
---

## vim033 - linebreak showbreak

- When writing text using Vim, some words can be broken in the middle of the word due to the word's position at the end of the line, causing the line length to exceed and split the word. Unlike many modern editors that automatically move the entire word to the next line for better readability, Vim doesn't do this by default. However, it's possible to achieve this behavior by modifying the configuration in the `vimrc` file.

- The solution is relatively simple and involves two settings:
  - `set linebreak`: This setting ensures that when a line's length exceeds in the middle of a word, Vim will move the entire word to the next line.
  - `set showbreak`: This setting allows you to define a specific character or string that visually represents the line break. It helps writers and readers recognize the line continuation.

To enable this behavior in Vim, add the following lines to your `vimrc` file:

```vim
set linebreak
set showbreak=...
```

- With these configurations, Vim will automatically move words to the next line when the line length exceeds, and the specified string (in place of `...`) will be displayed to indicate the line continuation.

- By setting these options in your `vimrc` file, you can enhance the readability of your text in Vim and enjoy a more modern editing experience.
