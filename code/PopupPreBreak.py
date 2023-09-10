import tkinter
from Popup import Popup
from Content import Content


class PopupPreBreak(Popup):

    def __init__(self, debug: bool = False):
        super().__init__(size="400x180", debug=debug)
        self.content = Content()

    def configure_window(self):
        self.basic_configuration()
        self.add_button(text="Start break", command=self.start_break)
        self.add_button(text="Postpone for 3 minutes", command=self.postpone)
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop)

    def postpone(self):
        self.root.destroy()
        self.status = "minor wait"

    def start_break(self):
        self.root.destroy()
        self.status = "break wait"

    def show(self):
        if not self.status in ["repop", "minor wait"]:
            self.new_labels()
        return super().show()

    def new_labels(self):
        motivation = self.content.randomize_motivation()
        tip = "Activity suggestion:\n" + self.content.randomize_tip()
        self.labels = [
            (motivation, "center", 'n'),
            (tip, "left", 'w')
        ]
