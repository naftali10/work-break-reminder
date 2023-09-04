import tkinter


class Popup:

    def __init__(self, debug: bool = False):
        self.debug: bool = debug
        self.root: tkinter.Tk
        self.status: str = "inactive"
        self.repop_timeout_ms: int = (10 if debug else 60) * 1000

    def configure_pre_break_window(self):
        self.basic_configuration(label="Time to take a break!")
        self.add_button(text="Start break", command=self.start_break)
        self.add_button(text="Postpone for 3 minutes", command=self.postpone)
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop_pre)

    def configure_post_break_window(self):
        self.basic_configuration(label="Did you take a break?")
        self.add_button(text="Yes", command=self.dismiss)
        self.add_button(text="No", command=self.loop_to_pre)
        if self.debug:
            self.add_button(text="Kill", command=self.kill)
        self.root.after(ms=self.repop_timeout_ms, func=self.repop_post)

    def basic_configuration(self, label: str):
        self.root.title("Work Break Reminder")
        self.root.geometry("400x150")
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)

        label1 = tkinter.Label(self.root, text=label)
        label1.pack(pady=20)

        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(side=tkinter.TOP, pady=20)

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
        raise SystemExit("Killed on purpose")

    def start_break(self):
        self.root.destroy()
        self.status = "break wait"

    def loop_to_pre(self):
        self.root.destroy()
        self.show_pre_break()

    def show_pre_break(self) -> str:
        self.root: tkinter.Tk = tkinter.Tk()
        self.configure_pre_break_window()
        self.root.mainloop()
        return self.status

    def show_post_break(self) -> str:
        self.root: tkinter.Tk = tkinter.Tk()
        self.configure_post_break_window()
        self.root.mainloop()
        print("post break mainloop finished")
        return self.status

    def repop_pre(self):
        self.root.destroy()
        self.show_pre_break()

    def repop_post(self):
        self.root.destroy()
        self.show_post_break()
