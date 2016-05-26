import unittest

from verbs.verb import RUVerb, UVerb
import unittest

from verbs.conjugation import Plain, Polite, Negative, PoliteNegative
from verbs.verb import BaseForms

class VerbTest(unittest.TestCase):
    def __init__(self, methodName='runTest', verb=None, table=None):
        super(VerbTest, self).__init__(methodName)
        self.table = table
        self.verb = verb
        split = [[c.strip() for c in l.split('|')] for l in self.table.split("\n")]
        self.forms = split[1]
        self.conjugation = split[3:]

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

    def test_polite_negative(self):
        self.execute(4, PoliteNegative)


suite = unittest.TestSuite()
suite.addTest(VerbTest.create(RUVerb("たべる"), open("tests/taberu.txt").read()))
suite.addTest(VerbTest.create(UVerb("かう"), open("tests/kau.txt").read()))
unittest.TextTestRunner(verbosity=2).run(suite)
