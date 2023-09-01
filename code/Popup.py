import tkinter


class Popup:

    def __init__(self):
        self.root: tkinter.Tk
        self.status: str = "inactive"

    def configure_window(self):

        self.root.title("Work Break Reminder")
        self.root.geometry("400x150")
        self.root.attributes("-topmost", True)

        label1 = tkinter.Label(self.root, text="Time to take a break!")
        label1.pack(pady=20)

        button_frame = tkinter.Frame(self.root)
        button_frame.pack(side=tkinter.TOP, pady=20)

        dismiss_button = tkinter.Button(
            button_frame,
            text="Dismiss until next break",
            command=self.dismiss
        )
        dismiss_button.pack(
            side=tkinter.LEFT,
            padx=10
        )

        postpone_button = tkinter.Button(
            button_frame,
            text="Postpone for 3 minutes",
            command=self.postpone
        )
        postpone_button.pack(
            side=tkinter.LEFT,
            padx=10
        )
        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)

    def dismiss(self):
        self.root.destroy()
        self.status = "major wait"

    def postpone(self):
        self.root.destroy()
        self.status = "minor wait"

    def do_nothing(self):
        pass

    def show(self) -> str:
        self.root: tkinter.Tk = tkinter.Tk()
        self.configure_window()
        self.root.mainloop()
        return self.status
