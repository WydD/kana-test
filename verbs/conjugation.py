from verbs.verb import BaseForms
import romkan


class Plain:
    def __init__(self, verb):
        self.verb = verb
        self.is_ru = verb.is_ru

    def present(self):
        return self.verb.base(BaseForms.U)

    def past(self):
        # TE form with an a
        return romkan.to_hiragana(romkan.to_hepburn(self.verb.base(BaseForms.TE))[:-1]+"a")

    def te(self):
        return self.verb.base(BaseForms.TE)

    def i(self):
        return self.verb.base(BaseForms.I)

    def passive(self):
        if self.is_ru:
            return self.verb.stem() + "られる"
        return self.verb.base(BaseForms.A) + "れる"

    def causative(self):
        if self.is_ru:
            return self.verb.stem() + "させる"
        return self.verb.base(BaseForms.A) + "せる"

    def causative_passive(self):
        # Short for interpreting the causative form as a RU verb
        # Equivalent to Plain(RUVerb(self.causative())).passive()
        return Plain.causative(self)[0:-1] + "られる"

    def volitional(self):
        return self.verb.base(BaseForms.O)

    def imperative(self):
        if self.is_ru:
            return self.verb.stem() + "ろ"
        return self.verb.base(BaseForms.E)

    def conditional(self):
        return self.verb.base(BaseForms.E) + "ば"

    def conditional_past(self):
        return self.past() + "ら"

    def potential(self):
        if self.is_ru:
            return self.verb.stem() + "られる"
        return self.verb.base(BaseForms.E) + "る"


class Polite(Plain):
    def __init__(self, verb):
        super().__init__(verb)
        self.polite_suffix = "ます"
        self.masu_base = self.i()

    def present(self):
        return self.masu_base + self.polite_suffix

    def past(self):
        return self.masu_base + "ました"

    def volitional(self):
        return self.masu_base + "ましょう"

    def conditional(self):
        return self.present() + "れば"  # alternative: ませば / is it ますなれば?

    def conditional_past(self):
        # Same as plain
        return self.past() + "ら"

    def imperative(self):
        return self.te() + "ください"

    def passive(self):
        # Re conjugation as the present of the passive (ru form)
        return Plain.passive(self)[0:-1] + self.polite_suffix

    def causative(self):
        # Re conjugation as the present of the causative (ru form)
        return Plain.causative(self)[0:-1] + self.polite_suffix

    def causative_passive(self):
        # Re conjugation as the present of the causative (ru form)
        return Plain.causative_passive(self)[0:-1] + self.polite_suffix

    def potential(self):
        # Re conjugation as the present of the potential (ru form)
        return Plain.potential(self)[0:-1] + self.polite_suffix


class Negative(Plain):
    def __init__(self, verb):
        super().__init__(verb)
        self.negative_base = self.verb.base(BaseForms.A)

    def present(self):
        return self.negative_base + "ない"

    def past(self):
        return self.negative_base + "なかった"

    def volitional(self):
        return (self.verb.stem() if self.is_ru else self.verb.base(BaseForms.U)) + "まい"

    def conditional(self):
        return self.negative_base + "なければ"

    def conditional_past(self):
        # Same as plain
        return self.past() + "ら"

    def imperative(self):
        return self.verb.base(BaseForms.U) + "な"

    def passive(self):
        # Re conjugation as the present of the passive (ru form)
        return Plain.passive(self)[0:-1] + "ない"

    def causative(self):
        # Re conjugation as the present of the causative (ru form)
        return Plain.causative(self)[0:-1] + "ない"

    def causative_passive(self):
        # Re conjugation as the present of the causative (ru form)
        return Plain.causative_passive(self)[0:-1] + "ない"

    def potential(self):
        # Re conjugation as the present of the potential (ru form)
        return Plain.potential(self)[0:-1] + "ない"


class PoliteNegative(Polite, Negative):
    def __init__(self, verb):
        Polite.__init__(self, verb)
        Negative.__init__(self, verb)

        self.polite_suffix = "ません"

    def past(self):
        return self.present() + "でした"

    def conditional(self):
        return self.present() + "なら"

    def conditional_past(self):
        return self.present() + "でしたら"

    def volitional(self):
        return Negative.present(self) + "でしょう"

    def imperative(self):
        return Negative.present(self) + "でください"
