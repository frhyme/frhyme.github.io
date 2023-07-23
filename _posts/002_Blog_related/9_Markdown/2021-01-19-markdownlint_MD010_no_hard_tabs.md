---
title: MarkdownLint - MD010 - no hard tabs
category: MarkdownLint
tags: markdown markdownlint tab
---

## MarkdownLint - MD010 - no hard tabs

- MD010은 다음을 의미합니다. 해석하면, "들여쓰기(Indentaion)을 할때, space 대신 hard tab을 사용하게 되면, 발생하는 rule입니다. 해결하려면, hard tab을 space로 변환하세요". 

> This rule is triggered by any lines that contain hard tab characters instead of using spaces for indentation. To fix this, replace any hard tab characters with spaces instead.

## Hard Tab and Soft Tab

- hard tab은 키보드에서 보통 tab키를 눌러서, `\t`가 입력되는 경우를 말합니다. 
- soft tab은 tab키를 누르는 것이 아니라, 스페이스 2번, 스페이스 4번 등으로 tab처럼 보여지게 하는 것이죠.
- 다만 보통 IDE에서는 hard tab을 눌러서 soft tab으로 자동변환되도록 해주는 설정들이 되어 있곤 합니다.
- 하드 탭을 쓰지 말라는 이유는, 언어에 따라서 스페이스2 스페이스4가 다른데, 그냥 tab으로 처리해버리면 변환 과정에서 문제가 생기는 일이 있기 때문이죠. 그래서 보통 하드 탭은 넣지 않고 변환 할때 스페이스로 변환해서 처리하곤 합니다.

## Solution

- 보통 직접 IDE에서 타이핑하는 경우보다는, 다른 사람의 코드를 복사해서 가져온 경우 발생합니다. 직접 타이핑하는 경우에는 hard tab을 알아서 soft tab으로 변환주는데, 복사하는 경우에는 그 코드에 숨겨져 있는 `\t`가 그대로 넘어오게 되니까요.
- 그냥, 찾아서 바꿔주면 해결됩니다.

## Reference

- [markdownlint - MD010](https://github.com/updownpress/markdown-lint/blob/master/rules/010-no-hard-tabs.md)
- [stackoverflow - what are hard and soft tabls](https://stackoverflow.com/questions/26350689/what-are-hard-and-soft-tabs)
