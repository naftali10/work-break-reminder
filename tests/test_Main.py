import unittest
from Main import Main


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.under_test = Main(debug=True)

    def test_run(self):
        print("Please play with the GUI and alt+f11 keybind\n"
              "Times to expect:\n"
              "\tMajor wait = 5 seconds\n"
              "\tMinor wait = 2 seconds\n"
              "\tBeeps to popup interval = 2 seconds\n"
              "\tRepop interval = 10 seconds\n"
              "Click Kill when you're done")
        with self.assertRaises(RuntimeError):
            self.under_test.run()


if __name__ == '__main__':
    unittest.main()
