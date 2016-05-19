import unittest

from verbs.verb import RUVerb, UVerb
import unittest

from verbs.conjugation import Plain, Polite, Negative
from verbs.verb import BaseForms

class VerbTest(unittest.TestCase):
    def __init__(self, methodName='runTest', verb=None, table=None):
        super(VerbTest, self).__init__(methodName)
        self.table = table
        self.verb = verb
        split = [[c.strip() for c in l.split('|')] for l in self.table.split("\n")]
        self.forms = split[2]
        self.conjugation = split[4:]

    def __str__(self):
        return "%s (%s)" % (self.verb._plain_form, self._testMethodName)

    @staticmethod
    def create(verb=None, table=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(VerbTest)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(VerbTest(name, verb=verb, table=table))
        return suite

    def test_forms(self):
        self.assertEqual(self.forms[0], self.verb.base(BaseForms.A))
        self.assertEqual(self.forms[1], self.verb.base(BaseForms.I))
        self.assertEqual(self.forms[2], self.verb.base(BaseForms.U))
        self.assertEqual(self.forms[3], self.verb.base(BaseForms.E))
        self.assertEqual(self.forms[4], self.verb.base(BaseForms.O))
        self.assertEqual(self.forms[5], self.verb.base(BaseForms.TE))

    def execute(self, index, conjugation):
        plain = conjugation(self.verb)
        self.assertEqual(self.conjugation[0][index], plain.present())
        self.assertEqual(self.conjugation[1][index], plain.past())
        self.assertEqual(self.conjugation[2][index], plain.imperative())
        self.assertEqual(self.conjugation[3][index], plain.volitional())
        self.assertEqual(self.conjugation[4][index], plain.conditional())
        self.assertEqual(self.conjugation[5][index], plain.conditional_past())
        self.assertEqual(self.conjugation[6][index], plain.passive())
        self.assertEqual(self.conjugation[7][index], plain.potential())
        self.assertEqual(self.conjugation[8][index], plain.causative())
        self.assertEqual(self.conjugation[9][index], plain.causative_passive())

    def test_plain(self):
        self.execute(1, Plain)

    def test_polite(self):
        self.execute(2, Polite)

    def test_negative(self):
        self.execute(3, Negative)


suite = unittest.TestSuite()
suite.addTest(VerbTest.create(RUVerb("たべる"), """
Forms (A, I, U, E, O, TE)
たべ | たべ | たべる | たべれ | たべよう | たべて
Conjugation (Plain, Polite, Negative, Negative Polite)
Present				| たべる			|	たべます			|	たべない
Past				| たべた			|	たべました		|	たべなかった
Imperative			| たべろ			|	たべて ください	|	たべるな
Volitional			| たべよう		|	たべましょう		|	たべまい
Conditional			| たべれば		|	たべますれば		|	たべなければ
Conditional past	| たべたら		|	たべましたら		|	たべなかったら
Passive				| たべられる		|	たべられます		|	たべられない
Potential			| たべられる		|	たべられます		|	たべられない
Causative			| たべさせる		|	たべさせます		|	たべさせない
Causative passive	| たべさせられる	|	たべさせられます	|	たべさせられない
"""))
suite.addTest(VerbTest.create(UVerb("かう"), """
Forms (A, I, U, E, O, TE)
かわ | かい | かう |　かえ　| かおう | かって
Conjugation (Plain, Polite, Negative, Negative Polite)
Present				| かう			|	かいます			|	かわない
Past				| かった			|	かいました		|	かわなかった
Imperative			| かえ			|	かって ください	|	かうな
Volitional			| かおう			|	かいましょう		|	かうまい
Conditional			| かえば			|	かいますれば		|	かわなければ
Conditional past	| かったら		|	かいましたら		|	かわなかったら
Passive				| かわれる		|	かわれます		|	かわれない
Potential			| かえる			|	かえます			|	かえない
Causative			| かわせる		|	かわせます		|	かわせない
Causative passive	| かわせられる	|	かわせられます	|	かわせられない
"""))
unittest.TextTestRunner(verbosity=2).run(suite)
