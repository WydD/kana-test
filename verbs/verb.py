from enum import Enum


class BaseForms(Enum):
    A = "a"
    E = "e"
    TE = "te"
    I = "i"
    U = "u"
    O = "o"


class Verb:
    _base_table = None
    is_ru = False

    def __init__(self, plain_form):
        self._plain_form = plain_form
        self._stem = plain_form[0:-1]

    def base(self, base_form):
        if base_form == BaseForms.U:
            return self._plain_form
        return self._stem + self._base_table[base_form.value]

    def stem(self):
        return self._stem


class RUVerb(Verb):
    def __init__(self, plain_form):
        super().__init__(plain_form)
        self.is_ru = True
        self._base_table = {
            "a": "",
            "i": "",
            "e": "れ",
            "te": "て",
            "o": "よう"
        }

uverb_base_table = {
    "く": {
        "a": "か",
        "i": "き",
        "e": "け",
        "o": "こう",
        "te": "いて"
    },
    "ぐ": {
        "a": "が",
        "i": "ぎ",
        "e": "げ",
        "o": "ごう",
        "te": "いで"
    },
    "す": {
        "a": "さ",
        "i": "し",
        "e": "せ",
        "o": "そう",
        "te": "して"
    },
    "む": {
        "a": "ま",
        "i": "み",
        "e": "め",
        "o": "もう",
        "te": "んで"
    },
    "ぬ": {
        "a": "な",
        "i": "に",
        "e": "ね",
        "o": "のう",
        "te": "んで"
    },
    "う": {
        "a": "わ",
        "i": "い",
        "e": "え",
        "o": "おう",
        "te": "って"
    },
    "つ": {
        "a": "た",
        "i": "ち",
        "e": "て",
        "o": "とう",
        "te": "って"
    },
    "る": {
        "a": "ら",
        "i": "り",
        "e": "れ",
        "o": "ろ",
        "te": "って"
    }
}


class UVerb(Verb):
    def __init__(self, plain_form):
        super().__init__(plain_form)
        self.is_ru = False
        self._base_table = uverb_base_table[plain_form[-1]]
