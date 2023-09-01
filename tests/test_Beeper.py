import unittest
from Beeper import Beeper
import time


class TestBeeper(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Beeper()

    def test_get_speaker_index(self):
        self.assertNotEqual(0, self.under_test.get_speaker_index())

    def test_beep(self):
        self.assertIsNone(self.under_test.beep())
        print("Beeped once")
        time.sleep(2)

    def test_beep_again(self):
        self.assertIsNone(self.under_test.beep())
        print("Beeped again")
        time.sleep(2)

    def test_beep_twice(self):
        self.assertIsNone(self.under_test.beep_twice())
        print("Beeped twice")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
