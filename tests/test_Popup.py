import unittest
from Popup import Popup


class TestPopup(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Popup()

    def test_show_dismiss(self):
        print("Click on dismiss")
        self.under_test.show()
        self.assertEqual("major wait", self.under_test.status)

    def test_show_postpone(self):
        print("Click on postpone")
        self.under_test.show()
        self.assertEqual("minor wait", self.under_test.status)


if __name__ == '__main__':
    unittest.main()
