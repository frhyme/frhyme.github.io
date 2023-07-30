---
title: selenium - change readOnly element
category:
tags:
---

## selenium - change readOnly element

- When attempting to scrape a web page, you might encounter an error message like the one below:

```log
selenium.common.exceptions.InvalidElementStateException: Message: Element is read-only: <input id="" name="" type="text">
```

- This error occurs when the element in the target HTML page is designed to be read-only, preventing direct modifications. In such cases, you can still change the element's value using JavaScript execution.

- By utilizing the `execute_script` method in Selenium, you can run custom JavaScript code directly within the browser. This allows you to bypass the read-only restriction and modify the elements as required.

- Below is a Python code example that demonstrates how to open a new Chrome browser session, navigate to a webpage, and use JavaScript execution to set the values of elements with ids "sDate" and "eDate" to "20230701" and "20230730," respectively. The modified HTML source is then retrieved and printed before closing the browser session:

```python
from selenium import webdriver

# Start a new Chrome browser session
driver = webdriver.Chrome()

# Open the web page with the form you want to interact with
url = "https://example.com/your-webpage"  # Replace this with the actual URL
driver.get(url)

# Execute JavaScript to set the values for sDate and eDate fields
start_date = "20230701"
end_date = "20230730"
script = f"document.getElementById('sDate').value = '{start_date}';"
script += f"document.getElementById('eDate').value = '{end_date}';"
driver.execute_script(script)

# Now you can trigger the button click to perform any further actions (if needed)

# Get the modified HTML source after changing the elements
modified_html_source = driver.page_source

# Close the browser session
driver.quit()

# Print the modified HTML source
print(modified_html_source)
```

- With this approach, you can effectively interact with elements that would otherwise be read-only, facilitating the successful execution of your web scraping or automation tasks.
