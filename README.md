# textutils

A lightweight Python library for common text-processing operations.

## Features

- **Word counting** — Count the number of words in a text
- **Character counting** — Count the number of characters in a text
- **Text reversal** — Reverse a given text string
- **Word capitalization** — Capitalize the first letter of each word
- **snake_case conversion** — Convert text to snake_case
- **camelCase conversion** — Convert text to camelCase
- **Slug generation** — Generate URL-friendly slugs

## Installation

```bash
pip install textutils
```

## Usage

```python
from textutils import (
    word_count,
    character_count,
    reverse,
    capitalize_words,
    snake_case,
    camel_case,
    slugify,
)

word_count("Hello Open Source!")       # 2
character_count("Hello")               # 5
reverse("Hello")                       # "olleH"
capitalize_words("hello world")        # "Hello World"
snake_case("Hello World")              # "hello_world"
camel_case("hello world")              # "helloWorld"
slugify("Open Source Development!")    # "open-source-development"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git switch -c feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
