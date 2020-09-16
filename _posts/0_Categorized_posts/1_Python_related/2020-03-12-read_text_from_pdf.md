---
title: python에서 pdfminer를 이용해서 pdf로부터 text 읽기.
category: python-libs
tags: python python-libs string pdf pdfminer
---

## pdfminer is better than others

- 가끔 pdf로부터 text data를 읽어야 할때가 있습니다. 처음에는 pypdf2, pdftotext를 사용하려고 했습니다만, pypdf2의 경우는 text에서 띄워쓰기가 날아가서 tokenize를 할 수 없는 경우가 있고, pdftotext의 경우는 다른 라이브러리들과 의존성이 해결되지 않아서, 결국 포기했습니다. 
- 그래서 그냥 [pdfminersix - documentation](https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html)를 사용했습니다. 

## extract text from pdf

- [pdfminersix - documentation](https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html)에 작성되어 있는 코드는 다음과 같습니다. 다음 코드를 사용해서 `pdf_file_path`만 그대로 넘겨주면 text를 그대로 읽어서 넘겨줍니다. 
- 물론 어느 정도의 후처리는 필요하긴 하지만, 이정도가 어딘가요. pypdf2에서 발생한 띄워쓰기 문제도 없습니다.

```python
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def read_pdf_PDFMINER(pdf_file_path):
    """
    pdf_file_path: 'dir/aaa.pdf'로 구성된 path로부터 
    내부의 text 파일을 모두 읽어서 스트링을 리턴함.
    https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
    """
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())
```

## wrap-up

- 다만, [pdfminersix](https://pdfminersix.readthedocs.io/en/latest/tutorials/highlevel.html)를 보면, pdfminer와 차이가 있고, 또한, high-level로 더 간단하게 할 수 있는 함수가 있는 것 같은데, 이상하게 잘 안되네요. 이 부분은 나중에 보완해보도록 하겠습니다.

## reference

- [pdfminersix - documentation](https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html)
