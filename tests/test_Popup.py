import unittest
from Popup import Popup


class TestPopup(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Popup(debug=True)

    def test_show(self):
        print("Take your time\n"
              "Click on kill")
        try:
            self.under_test.show()
        except SystemExit:
            pass

    def test_repop(self):
        print("Ignore window to verify repop.\n"
              "Afterwards, Kill.")
        try:
            self.under_test.show()
        except SystemExit:
            pass


if __name__ == '__main__':
    unittest.main()
