---
title: json - ensure ascii
category: json
tags: json python
---

## JSON - Preserving Non-ASCII Characters

- When using the `json` module in Python to handle JSON data containing non-ASCII characters, you may encounter a situation where the characters appear broken when opening the JSON file. However, this is not a result of data corruption but rather a display of UTF-8 encoded characters. Understanding the reason behind this behavior can lead to better practices in dealing with JSON data.

### Historical Context and Default Encoding

- JSON was originally designed to facilitate data transmission between different computer systems and programming languages. To ensure smooth interaction and interpretation of messages on both ends, a default encoding method was required to be understood by both computers. ASCII encoding, being a simple and widely supported character encoding, was chosen as the default. Thus, by default, the `json.dump` method sets `ensure_ascii=True`, resulting in ASCII-encoded output when writing JSON to a file.

### Preserving Non-ASCII Characters

- To save JSON data with raw non-ASCII characters, such as Korean characters, it is essential to preserve the original encoding when writing the JSON file. Setting `ensure_ascii=False` explicitly instructs the `json.dump` method to preserve non-ASCII characters without escaping them into UTF-8 encoded representations. This ensures that the actual Korean characters, not their encoded versions, are stored in the JSON file.

### Saving JSON with Non-ASCII Characters

- To save JSON files with non-ASCII characters correctly, follow this approach:

```python
import json

data = {
    "name": "한국어",
    "age": 30,
    "location": "Seoul"
}

# Open a file in write mode and set ensure_ascii to False
with open('output.json', 'w', encoding='UTF-8') as f:
    json.dump(data, f, ensure_ascii=False)
```

- By explicitly specifying `'UTF-8'` as the encoding and setting `ensure_ascii=False`, you ensure that non-ASCII characters, like the Korean text in this example, are saved correctly as intended, preserving the true character representation in the JSON file. This practice aligns with modern standards and allows seamless handling of multilingual data across different systems and applications.
