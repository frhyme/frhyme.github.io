---
title: nltk down ssl certificate failed.
category: python-libs
tags: python python-libs nltk 
---

## `nltk.download()` failed

- nltk로부터 필요한 라이브러리들을 다음처럼 다운 받을 때, 문제가 생기는 경우가 있습니다.

```python
import nltk
nltk.download("wordnet")
```

- 이유는 모르겠지만, nltk로부터 다운받는 과정에서 뭔가 문제가 발생한 것이죠. 
- 개념적으로는 `'/Users/frhyme/anaconda3/nltk_data'` 경로 안에 필요한 라이브러리들을 [이곳에서](http://www.nltk.org/nltk_data/) 다운 받아서 쓰면 되긴 하는데, 그래도 잘 안될 때가 있어요. 

- 다행히도, stackoverflow 내의 질문 [nltk-download-ssl-certificate-verify-failed](https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed)의 답변인 아래 코드를 사용하면 정상적으로 다운받을 수 있습니다. 
- 이유는 모르겠지만, 아래 코드를 사용하면, 원래 nltk 패키지를 다운받는 팝업이 뜨고, 거기서 다운받으면 됩니다 호호.

```python
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
```




## reference

- [nltk-download-ssl-certificate-verify-failed](https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed)