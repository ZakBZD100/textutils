## Description

It would be useful to have a function that returns a dictionary of word frequencies in a text.

## Expected behavior

```python
from textutils import word_frequency

word_frequency("hello world hello")
# {"hello": 2, "world": 1}
```

## Context

This would help users analyze text without having to write their own counting logic.
