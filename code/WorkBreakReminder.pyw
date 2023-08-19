import pyaudio
import numpy as np
import keyboard
from datetime import datetime, timedelta
import tkinter as tk
import time


duration = timedelta(minutes=60)
postpone = timedelta(minutes=3)
notification_time = timedelta(seconds=20)
reset_key = 'alt+f12'


def get_speaker_index(p):
    device_name = "Speakers (Realtek(R) Audio)"
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info["name"] == device_name:
            device_index = i
    return device_index


def make_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(duration * 48000), False)
    wave = np.sin(frequency * t * 2 * np.pi).astype(np.float32)
    return wave


def beep(frequency, duration):
    p = pyaudio.PyAudio()
    wave = make_sine_wave(frequency, duration)
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=48000,
                output=True,
                output_device_index=get_speaker_index(p))
    stream.write(wave)
    stream.close()
    p.terminate()


def show_notification():
    root = tk.Tk()
    root.title("Work Break Reminder")
    root.geometry("400x150")
    root.attributes("-topmost", True)

    label1 = tk.Label(root, text="Time to take a break!")
    label1.pack(pady=20)

    def on_close():
        root.destroy()
        timer()

    def postpone_break():
        root.destroy()
        timer(datetime.now() + postpone)

    def do_nothing():
        pass

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, pady=20)

    button1 = tk.Button(button_frame, text="Dismiss until next break", command=on_close)
    button1.pack(side=tk.LEFT, padx=10)

    postpone_button = tk.Button(button_frame, text=f"Postpone for {int(postpone.total_seconds() / 60)} minutes", command=lambda: postpone_break())
    postpone_button.pack(side=tk.LEFT, padx=10)

    root.protocol("WM_DELETE_WINDOW", do_nothing)
    root.mainloop()


def timer(end_time = None):
    if end_time is None:
        end_time = datetime.now() + duration
    did_beep = False
    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()

        if remaining_time <= notification_time and not did_beep:
            beep(1500, 0.75)
            beep(1500, 0.75)
            did_beep = True

        if keyboard.is_pressed(reset_key):
            beep(1000, 0.75)
            time.sleep(1)
            timer()

        time.sleep(0.5)

    show_notification()

timer()
