import tkinter
from Popup import Popup


class PopupPostBreak(Popup):

    def configure_window(self):
        self.basic_configuration(content=[tkinter.Label(text="Did you take a break?")])
        self.add_button(text="Yes", command=self.dismiss)
        self.add_button(text="No", command=self.loop_to_pre)
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
        self.show()
