import unittest
from PopupPostBreak import PopupPostBreak


class TestPopupPreBreak(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = PopupPostBreak(debug=True)

    def test_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, click Kill to continue.")
        try:
            self.under_test.show()
        except SystemExit:
            pass

    def test_show_dismiss(self):
        print("Take your time\n"
              "Click on Yes.")
        self.under_test.show()
        self.assertEqual("major wait", self.under_test.status)

    def test_show_loop_to_pre(self):
        print("Take your time\n"
              "Click on No.")
        self.under_test.show()
        self.assertEqual("pre break", self.under_test.status)


if __name__ == '__main__':
    unittest.main()
