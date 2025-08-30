__all__ = ("find_shortest_longest_word",)

import string
from types import new_class


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    words = [i.strip().strip(string.punctuation) for i in text.split()]
    return (None, None) if not words else (min(words, key=len), max(words, key=len))

