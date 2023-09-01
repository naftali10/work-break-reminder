import time
import unittest
from Popup import Popup


class TestPopup(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Popup(debug=True)

    def test_show_dismiss(self):
        print("Click on dismiss")
        self.under_test.show()
        self.assertEqual("major wait", self.under_test.status)

    def test_show_postpone(self):
        print("Click on postpone")
        self.under_test.show()
        self.assertEqual("minor wait", self.under_test.status)

    def test_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, click any button to continue.")
        self.under_test.show()


if __name__ == '__main__':
    unittest.main()
