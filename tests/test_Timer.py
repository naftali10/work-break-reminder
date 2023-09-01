import time
import unittest
from Timer import Timer
from datetime import datetime, timedelta


class TestTimer(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Timer(debug=True)

    def test_wait_major(self):
        print("Do not press combination")
        time.sleep(1)
        self.under_test.wait_major()
        self.assertEqual("major done", self.under_test.status)

    def test_wait_major_keybind(self):
        print("Please long press alt+f11")
        self.under_test.wait_major()
        self.assertEqual("major wait", self.under_test.status)

    def test_update_finish_hour(self):
        now = datetime.now()
        self.under_test.update_finish_hour(timedelta(minutes=5))
        self.assertEqual(now + timedelta(minutes=5), self.under_test.finish_hour)

    def test_update_remaining_time(self):
        self.under_test.update_remaining_time()
        self.assertEqual(timedelta(seconds=0), self.under_test.remaining_time)

    def test_wait_before_popup_keybind(self):
        print("Please long press alt+f11")
        self.under_test.wait_before_popup()
        self.assertEqual("major wait", self.under_test.status)


if __name__ == '__main__':
    unittest.main()
