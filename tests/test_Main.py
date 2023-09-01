import unittest
from Main import Main


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Main(debug=True)

    def test_run_keybind(self):
        print("Please play with the GUI and alt+f11 keybind")
        self.under_test.run()


if __name__ == '__main__':
    unittest.main()
