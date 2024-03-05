import tkinter
import tkinter.font as tkFont

class Popup:

    def __init__(self, size: str = "400x150", debug: bool = False):
        self.size: str = size
        self.debug: bool = debug
        self.root: tkinter.Tk = None
        self.status: str = "inactive"
        self.repop_timeout_ms: int = (10 if debug else 60) * 1000
        self.labels: [(str, str, str, str, int)] = \
            [("Test", "center", 'n', "normal", 9)] if debug \
            else [("Take a break!", "center", 'n', "normal", 9)]

    def configure_window(self):
        self.basic_configuration()
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop)

    def basic_configuration(self):
        self.root.title("Wellness Time Reminder")
        self.root.geometry(self.size)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)

        for (text, justify, align, weight, size) in self.labels:
            label = tkinter.Label(
                master=self.root,
                text=text,
                justify=justify,
                wraplength=600,
                font=tkFont.Font(family="Segoe UI", size=size, weight=weight))
            label.pack(anchor=align, padx=20, pady=5)

        self.button_frame = tkinter.Frame(master=self.root)
        self.button_frame.pack(pady=20)

    def add_button(self, text: str, command: {}):
        button = tkinter.Button(
            master=self.button_frame,
            text=text,
            command=command
        )
        button.pack(
            side=tkinter.LEFT,
            padx=20
        )

    def kill(self):
        self.root.destroy()
        raise SystemExit("Killed on purpose")

    def do_nothing(self):
        pass

    def repop(self):
        self.root.destroy()
        self.status = "repop"
        self.show()

    def show(self) -> str:
        self.root: tkinter.Tk = tkinter.Tk()
        self.configure_window()
        self.root.mainloop()
        return self.status
