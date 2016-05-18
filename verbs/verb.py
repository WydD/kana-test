from enum import Enum


class BaseForms(Enum):
    A = "a"
    E = "e"
    TE = "te"
    I = "i"
    U = "u"
    O = "o"
    POTENTIAL = "rare"
    IMPERATIVE = "ro"
    CAUSATIVE = "sa"


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
            "o": "よう",
            "rare": "られ",
            "ro": "ろ",
            "sa": "さ",
        }
