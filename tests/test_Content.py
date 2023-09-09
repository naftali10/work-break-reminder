import unittest
from Content import  Content


class TestContent(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Content()

    def test_randomize_tip(self):
        self.assertTrue(self.under_test.randomize_tip() in self.under_test.tips)

    def test_randomize_motivation(self):
        self.assertTrue(self.under_test.randomize_motivation() in self.under_test.motivations)
