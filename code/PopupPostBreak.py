import tkinter
from Popup import Popup


class PopupPostBreak(Popup):

    def __init__(self, debug: bool = False):
        super().__init__(size="450x100" if debug else "400x100", debug=debug)

    def configure_window(self):
        self.labels = [("Did you take a break?", "center", 'n')]
        self.basic_configuration()
        self.add_button(text="Yes, I took a break", command=self.dismiss)
        self.add_button(text="Not really", command=self.loop_to_pre)
        self.add_button(text="I took a non-related break", command=self.dismiss)
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop)

    def dismiss(self):
        self.root.destroy()
        self.status = "major wait"

    def start_break(self):
        self.root.destroy()
        self.status = "break wait"

    def loop_to_pre(self):
        self.root.destroy()
        self.status = "pre break"
