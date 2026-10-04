# textutils

petite librairie python pour manipuler du texte

## Features

- compter les mots
- compter les caracteres
- inverser le texte
- mettre en majuscule
- snake_case
- camelCase
- faire des slugs pour les urls
- compter la frequence des mots

## Installation

```bash
pip install textutils
```

## Usage

```python
from textutils import word_count, snake_case, slugify, word_frequency

word_count("Hello World") # 2
snake_case("Hello World") # hello_world
slugify("Hello World!") # hello-world
word_frequency("hello world hello") # {"hello": 2, "world": 1}
```

## Contributing

Feel free to make a PR if you want to contribute

## License

MIT
