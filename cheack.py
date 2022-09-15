from uzwords import words
from difflib import get_close_matches

from tranlater import to_latin

def cheack(word, words=words):
    word = word.lower()
    words = to_latin(words)
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = f"{word}"
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    return {"available":available, "matches":matches}