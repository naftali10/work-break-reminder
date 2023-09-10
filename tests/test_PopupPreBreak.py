import unittest
from PopupPreBreak import PopupPreBreak


class TestPopup(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = PopupPreBreak(debug=True)

    def test_show_start_break(self):
        print("Take your time\n"
              "Click on start break")
        self.under_test.show()
        self.assertEqual("break wait", self.under_test.status)

    def test_show_postpone(self):
        print("Take your time\n"
              "Click on postpone")
        self.under_test.show()
        self.assertEqual("minor wait", self.under_test.status)

    def test_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, click Kill to continue.")
        try:
            self.under_test.show()
        except SystemExit:
            pass


if __name__ == '__main__':
    unittest.main()
