from enum import Enum


class BaseForms(Enum):
    NEGATIVE = "a"
    CONDITIONAL = "e"
    TE = "te"
    MASU = "i"
    PLAIN = "u"
    VOLITIONAL = "o"
    POTENTIAL = "rare"
    IMPERATIVE = "ro"


class Verb:
    _base_table = None

    def __init__(self, plain_form):
        self._plain_form = plain_form
        self._stem = plain_form[0:-1]

    def base(self, base_form):
        if base_form == BaseForms.PLAIN:
            return self._plain_form
        return self._stem + self._base_table[base_form.value]


class RUVerb(Verb):
    def __init__(self, plain_form):
        super().__init__(plain_form)
        self._base_table = {
            "a": "",
            "i": "",
            "e": "れ",
            "te": "て",
            "o": "よう",
            "rare": "られ",
            "ro": "ろ",
        }
