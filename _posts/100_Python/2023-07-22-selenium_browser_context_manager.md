---
title: selenium - browser with context
category: selenium
tags: selenium browser python
---

## selenium - browser with context

- When using Selenium for web scraping, it's common to encounter situations where the browser is not closed properly, especially if an exception occurs during the process. This can lead to lingering browser instances occupying memory in the background. Additionally, when utilizing Selenium in headless mode (where the browser operates in the background without a visible window), it becomes challenging to determine if the browser is still active or not.

- To address this issue, we can apply a similar approach used when opening Python files using the `with` statement. By implementing a context manager with Selenium, we can ensure that the browser is properly opened and closed, regardless of any exceptions that may occur.

- Using the context manager pattern, we can encapsulate the setup (browser opening) and teardown (browser closing) operations within the `__enter__()` and `__exit__()` methods of the context manager class. This allows us to ensure that the browser is closed gracefully, even if an exception is raised during the web scraping process.

- Here's an example of how a Selenium context manager might be structured:

```python
from selenium import webdriver

class SeleniumContextManager:
    def __enter__(self):
        # Open the browser (e.g., Chrome)
        self.driver = webdriver.Chrome()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the browser after the indented block of code
        self.driver.quit()

# Using the Selenium context manager with the 'with' statement
with SeleniumContextManager() as driver:
    # Perform web scraping operations using 'driver' as the WebDriver instance
    driver.get('https://www.example.com')
    # ... rest of the web scraping code ...

# The browser is automatically closed after the 'with' block.
```

- In this example, the browser is opened when the `with` statement is executed, and the `webdriver` instance is made available within the indented block. After the block completes (whether normally or due to an exception), the browser is closed automatically by the `__exit__()` method, ensuring proper cleanup.

- By using the `with` statement in this manner, we enhance the reliability of our web scraping code, ensuring that the browser resources are managed efficiently and freeing up memory when the scraping process is completed.

- Indeed, the context managing mechanism can also be achieved using the `contextlib` module in Python, specifically by utilizing the `contextmanager` decorator. This approach offers a more concise way to create lightweight context managers without needing to define a separate class with `__enter__()` and `__exit__()` methods.

- Here's how the previous Selenium context manager can be rewritten using the `contextlib` module:

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

- In this version, the `contextmanager` decorator transforms the generator function `selenium_context_manager()` into a context manager. The `yield` statement inside the function serves as a replacement for the `__enter__()` method, where the browser is opened, and the `driver` instance is made available within the indented block.

- The `try` block inside the function covers the body of the `with` statement (indented block), and the `finally` block serves as the equivalent of the `__exit__()` method, ensuring that the browser is closed after the `with` block completes execution, regardless of any exceptions that may occur.

- Both the class-based context manager and the `contextlib`-based context manager achieve the same goal of managing the browser's lifecycle during web scraping. The `contextlib` approach can be more concise and is suitable for simpler context management scenarios. However, for more complex use cases or if additional context management functionality is required, the class-based approach provides more flexibility.
