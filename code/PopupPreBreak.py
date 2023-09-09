import tkinter
from Popup import Popup
from Content import Content


class PopupPreBreak(Popup):

    def __init__(self, debug: bool = False):
        super().__init__(debug)
        self.content = Content()

    def configure_window(self):
        self.basic_configuration(content=self.content_made)
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
        if self.status != "repop":
            self.make_content()
        super().show()

    def make_content(self):
        tip = self.content.randomize_tip()
        motivation = self.content.randomize_motivation()
        self.content_made = [
            tkinter.Label(text=motivation, justify="center"),
            tkinter.Label(text=tip, justify="left", wraplength=350)
        ]
