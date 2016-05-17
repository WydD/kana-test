from verbs.verb import BaseForms
import romkan


class Plain:
    def __init__(self, verb):
        self.verb = verb

    def present(self):
        return self.verb.base(BaseForms.PLAIN)

    def past(self):
        # TE form with an a
        hepburn = romkan.to_hepburn(self.verb.base(BaseForms.TE))
        hepburn[-1] = 'a'
        return romkan.to_hiragana(hepburn)

    def teiru(self):
        return self.verb.base(BaseForms.TE)+"いる"

    def te(self):
        return self.verb.base(BaseForms.TE)

    def tai(self):
        return self.verb.base(BaseForms.MASU)+"たい"

    def passive(self):
        return self.verb.base(BaseForms.NEGATIVE) + "れる"

    def causative(self):
        return self.verb.base()