from Timer import Timer
from Beeper import Beeper
from PopupPreBreak import PopupPreBreak
from PopupPostBreak import PopupPostBreak


class Main:

    def __init__(self, debug: bool = False):
        self.timer = Timer(debug=debug)
        self.beeper = Beeper()
        self.popup_pre_break = PopupPreBreak(debug=debug)
        self.popup_post_break = PopupPostBreak(debug=debug)

        self.status: str = "start"

    def run(self):
        while True:
            self.major_reset_loop()
            self.transition_to_popup()
            while True:
                if self.status == "break wait":
                    self.wait_break_and_popup()
                    if self.status == "pre break":
                        self.status = self.popup_pre_break.show()
                    if self.status == "major wait":
                        break
                elif self.status in ["minor wait", "medium wait"]:
                    self.minor_medium_loop()
                else:
                    raise ValueError(f"Unexpected status: {self.status}")
            if self.status == "major wait":
                continue
            else:
                raise ValueError(f"Unexpected status: {self.status}")

    def major_reset_loop(self):
        while True:
            self.status = self.timer.wait_major()
            if self.status == "major reset":
                self.beeper.alert_major_reset()
            else:
                break

    def minor_medium_loop(self):
        while True:
            if self.status == "minor wait":
                self.timer.wait_minor()
            elif self.status == "medium wait":
                self.timer.wait_medium()
            self.transition_to_popup()
            if self.status not in ["minor wait", "medium wait"]:
                break

    def wait_break_and_popup(self):
        self.timer.wait_break()
        self.status = self.popup_post_break.show()

    def transition_to_popup(self):
        self.beeper.alert_upcoming_popup()
        self.timer.wait_before_popup()
        self.status = self.popup_pre_break.show()

