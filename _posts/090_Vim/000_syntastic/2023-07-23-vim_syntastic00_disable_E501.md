---
title: vim syntastic00 - disable E501
category: vim
tags: syntastic pyflake8 python
---

## vim syntastic00 - disable E501

- Recently, I installed the latest version of PyFlake8, a widely used Python linting tool. However, I noticed that after the installation, my Vim editor with the Syntastic plugin started showing an alarm message regarding the E501 issue, indicating that some lines were too long (145 characters, exceeding the recommended 79-character limit). To address this, I tried disabling the E501 alarm using the `syntastic_python_pycodestyle_args` configuration in my `vimrc` file, but unfortunately, it didn't have the desired effect:

```vim
" E501 line too long (145 > 79 characters)
let g:syntastic_python_pycodestyle_args='--ignore=E501'
```

- Since the above approach didn't work, I explored an alternative solution. PyFlake8 provides configuration options through a `.flake8` file, where you can customize its behavior and ignore specific checks. To utilize this, I created a `.flake8` file in my project's root directory, and I added the following content to disable the E501 check:

```.flake8
[flake8]
ignore = E501
```

- This configuration explicitly instructs PyFlake8 to ignore the E501 check for line length issues. With this setup in place, Syntastic no longer displays the E501 alarm when working with Python files in my Vim editor.

- By leveraging the `.flake8` configuration, I can easily control the behavior of PyFlake8 and fine-tune the linting checks based on my preferences. This ensures that my coding workflow remains efficient, with relevant feedback on code quality and adherence to coding standards while avoiding unnecessary alarms for line length issues.

## Syntastic

### Syntastic - wrap-up

- Syntastic is a popular Vim plugin that provides code checking and linting capabilities directly within the Vim editor. It enables on-the-fly syntax checking and highlighting for various programming languages, helping developers identify errors, warnings, and potential issues in their code as they write it.

- Key features of Syntastic include:
  - Syntax Checking: Syntastic uses external syntax checkers and linters (such as Flake8, Pylint, ESLint, etc.) to analyze the code in real-time. It checks for syntax errors, style violations, and other code issues.
  - Error Highlighting: When syntax errors or issues are detected, Syntastic highlights the problematic lines in the Vim editor, making it easy to locate and address the problems.
  - Status Line Indicators: Syntastic provides status line indicators that display the status of the current file's syntax checking. It shows error and warning counts, allowing you to quickly identify the severity of issues in your code.
  - Quickfix List: Syntastic populates the Vim quickfix list with detected errors, making it easy to navigate between them and quickly jump to the problematic lines.
  - Language Support: Syntastic supports a wide range of programming languages, including Python, JavaScript, Ruby, C/C++, Java, and many others.
  - Customizable: Users can configure the syntax checkers and linters to use, customize the error format, and adjust various settings according to their preferences.
- Syntastic enhances the development experience for Vim users by providing immediate feedback on code correctness and style. It helps catch errors early in the coding process and encourages adherence to coding standards and best practices.
- To use Syntastic, you typically need to install external syntax checkers and linters for the programming languages you are working with. Once configured, Syntastic will automatically start checking your code as you edit, providing helpful feedback and improving the overall coding experience in Vim.

### Syntastic and pyflake8

- Syntastic is a framework for Vim that provides a unified interface to integrate with various external syntax checkers and linters. When you receive messages or feedback from PyFlake8 through Syntastic, it means that PyFlake8 is indeed running outside of Syntastic.

- Syntastic itself does not perform the syntax checking or linting directly. Instead, it acts as a bridge between Vim and external tools like PyFlake8, allowing Vim to display the results of the syntax check and highlight any issues detected.

- Here's how the process typically works:
1. You write code in a Vim buffer and save the file.
2. Syntastic triggers the external syntax checker (e.g., PyFlake8) based on the file's type (determined by the file extension or other configurations).
3. The external syntax checker (PyFlake8) runs as a separate process outside of Vim and analyzes the code for syntax errors and other issues.
4. Once PyFlake8 completes its analysis, it returns the results to Syntastic.
5. Syntastic then processes the results and displays them in Vim, highlighting the problematic lines and showing any error messages or warnings in the status line or the quickfix list.
