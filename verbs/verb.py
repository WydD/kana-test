from enum import Enum


class BaseForms(Enum):
    NEGATIVE = "a"
    IMPERATIVE = "e"
    TE = "te"
    MASU = "i"
    PLAIN = "u"


class Conjugation:
    _base_table = dict()

    def __init__(self, plain_form):
        self._plain_form = plain_form
        self._stem = plain_form[0:-1]
        self._ending = plain_form[-1]

    def _base(self, base_form):
        return self._stem + self._base_table[self._ending][base_form.value]


