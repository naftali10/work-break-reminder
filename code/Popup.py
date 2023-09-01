import tkinter


class Popup:

    def __init__(self, debug: bool = False):
        self.debug: bool = debug
        self.root: tkinter.Tk
        self.status: str = "inactive"
        self.repop_timeout_ms: int = (10 if debug else 60) * 1000

    def configure_window(self):

        self.root.title("Work Break Reminder")
        self.root.geometry("400x150")
        self.root.attributes("-topmost", True)

        label1 = tkinter.Label(self.root, text="Time to take a break!")
        label1.pack(pady=20)

        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(side=tkinter.TOP, pady=20)

        self.add_button(text="Dismiss until next break", command=self.dismiss)
        self.add_button(text="Postpone for 3 minutes", command=self.postpone)
        if self.debug:
            self.add_button(text="Kill", command=self.kill)

        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop)

    def add_button(self,text: str, command: {}):
        button = tkinter.Button(
            self.button_frame,
            text=text,
            command=command
        )
        button.pack(
            side=tkinter.LEFT,
            padx=10
        )

    def dismiss(self):
        self.root.destroy()
        self.status = "major wait"

    def postpone(self):
        self.root.destroy()
        self.status = "minor wait"

    def do_nothing(self):
        pass

    def kill(self):
        self.root.destroy()
        raise RuntimeError("Killed on purpose")

    def show(self) -> str:
        self.root: tkinter.Tk = tkinter.Tk()
        self.configure_window()
        self.root.mainloop()
        return self.status

    def repop(self):
        self.root.destroy()
        self.show()
