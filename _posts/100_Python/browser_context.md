---
title: selenium - browser with context
category: selenium
tags: selenium browser python
---

## selenium - browser with context

when we use selenium to crawl web page, we might not close the browser especially when browser was opened and some exception occurred, that browser was not clsoed and still use memory in the background. Especially, if you use tha selenium browser by headless browser(it means that it works on the background), you can't catch if it was still alive or not.
For solving this problem, we can open the browser like the way of python file openings with `with` statemetns.






```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from contextlib import contextmanager


@contextmanager
def browser_context():
    # Start the browser session
    browser = webdriver.Firefox()

    try:
        # The driver instance is returned as the context manager value
        yield browser
    finally:
        # Close the browser session in the 'finally' block to ensure it's always closed
        browser.quit()


if __name__ == "__main__":
    target_url = 'http://naver.com'
    with browser_context() as browser:
        browser.get(target_url)
    print("== complete")
```

