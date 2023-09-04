import time
import unittest
from Popup import Popup


class TestPopup(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Popup(debug=True)

    def test_show_pre_dismiss(self):
        print("Take your time\n"
              "Click on start break")
        self.under_test.show_pre_break()
        self.assertEqual("break wait", self.under_test.status)

    def test_show_pre_postpone(self):
        print("Take your time\n"
              "Click on postpone")
        self.under_test.show_pre_break()
        self.assertEqual("minor wait", self.under_test.status)

    def test_pre_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, click any button to continue.")
        try:
            self.under_test.show_pre_break()
        except SystemExit:
            pass

    def test_post_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, click any button to continue.")
        try:
            self.under_test.show_post_break()
        except SystemExit:
            pass

    def test_show_post_dismiss(self):
        print("Take your time\n"
              "Click on Yes.")
        self.under_test.show_post_break()
        self.assertEqual("major wait", self.under_test.status)

    def test_show_post_loop_to_pre(self):
        print("Take your time\n"
              "Click on No, verify pre-break loop, then kill.")
        with self.assertRaises(SystemExit):
            self.under_test.show_post_break()
        self.assertEqual("inactive", self.under_test.status)


if __name__ == '__main__':
    unittest.main()
