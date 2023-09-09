import tkinter


class Popup:

    def __init__(self, debug: bool = False):
        self.debug: bool = debug
        self.root: tkinter.Tk = None
        self.status: str = "inactive"
        self.repop_timeout_ms: int = (10 if debug else 60) * 1000

    def configure_window(self):
        self.basic_configuration(content=[tkinter.Label(text="Test")])
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop)

    def basic_configuration(self, content: [tkinter.Label]):
        self.root.title("Work Break Reminder")
        self.root.geometry("400x150")
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)

        for cont in self.content_made:
            cont.pack(pady=20)

        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(side=tkinter.TOP, pady=20)

    def add_button(self, text: str, command: {}):
        button = tkinter.Button(
            self.button_frame,
            text=text,
            command=command
        )
        button.pack(
            side=tkinter.LEFT,
            padx=10
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
