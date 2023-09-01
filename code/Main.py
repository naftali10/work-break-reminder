from Timer import Timer
from Beeper import Beeper
from Popup import Popup


class Main:

    def __init__(self, debug: bool = False):
        self.timer = Timer(debug=debug)
        self.beeper = Beeper()
        self.popup = Popup(debug=debug)

        self.status: str = "start"

    def run(self):
        while True:
            self.major_loop()
            self.transition_to_popup()
            if self.status == "major wait":
                continue
            elif self.status == "minor wait":
                self.minor_loop()
            else:
                raise RuntimeError(f"Unexpected status: {self.status}")

    def major_loop(self):
        while True:
            self.status = self.timer.wait_major()
            if self.status == "major reset":
                self.beeper.alert_major_reset()
            else:
                break

    def minor_loop(self):
        while True:
            self.timer.wait_minor()
            self.transition_to_popup()
            if self.status != "minor wait":
                break

    def transition_to_popup(self):
        self.beeper.alert_upcoming_popup()
        self.timer.wait_before_popup()
        self.status = self.popup.show()
