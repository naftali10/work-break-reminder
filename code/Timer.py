import time
import keyboard
from datetime import datetime, timedelta


class Timer:

    def __init__(self, debug: bool = False):
        self.major_timeout: timedelta = timedelta(seconds=5) if debug else timedelta(minutes=60)
        self.minor_timeout: timedelta = timedelta(seconds=2) if debug else timedelta(minutes=3)
        self.popup_timeout: timedelta = timedelta(seconds=9) if debug else timedelta(seconds=20)
        self.break_timeout: timedelta = timedelta(seconds=2) if debug else timedelta(minutes=3)

        self.remaining_time: timedelta = timedelta(seconds=0)
        self.finish_hour: datetime = datetime.now()
        self.sleep_interval: float = 0.5
        self.reset_key = "alt+f11" if debug else "alt+f12"

        self.status: str = "inactive"

    def update_finish_hour(self, timeout: timedelta) -> None:
        self.finish_hour = datetime.now() + timeout

    def update_remaining_time(self) -> None:
        self.remaining_time = self.finish_hour - datetime.now()

    def wait_major(self) -> str:
        self.update_finish_hour(self.major_timeout)
        while datetime.now() < self.finish_hour:
            self.update_remaining_time()
            if keyboard.is_pressed(self.reset_key):
                self.update_finish_hour(self.major_timeout)
                self.update_remaining_time()
                return "major reset"
            time.sleep(self.sleep_interval)
        return "major done"

    def wait_minor(self) -> str:
        self.update_finish_hour(self.minor_timeout)
        while datetime.now() < self.finish_hour:
            self.update_remaining_time()
            time.sleep(self.sleep_interval)
        return "minor done"

    def wait_before_popup(self) -> str:
        self.update_finish_hour(self.popup_timeout)
        while datetime.now() < self.finish_hour:
            self.update_remaining_time()
            if keyboard.is_pressed(self.reset_key):
                return "major wait"
            time.sleep(self.sleep_interval)
        return "popup done"

    def wait_break(self):
        self.update_finish_hour(self.break_timeout)
        while datetime.now() < self.finish_hour:
            self.update_remaining_time()
            time.sleep(self.sleep_interval)
        return "break done"
