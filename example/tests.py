from unittest import TestCase
from example.exmath import exsum


class ExTestCase(TestCase):
    def test_exsum(self):
        self.assertEqual(exsum(3,2), 5)
