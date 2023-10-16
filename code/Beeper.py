import time
import sounddevice
import numpy as np


class Beeper:

    def __init__(self):
        self.frequency: int = 1500
        self.single_beep_duration: float = 0.4
        self.wave = self.make_sine_wave()

    def beep(self) -> None:
        try:
            sounddevice.play(data=self.wave, samplerate=48000, device=self.get_speaker_index(),blocking=True)
        except RuntimeError as e:
            raise RuntimeError(f"Beeper Error: {e}")

    def make_sine_wave(self) -> np:
        t = np.linspace(0, self.single_beep_duration, int(self.single_beep_duration * 48000), False)
        wave = np.sin(self.frequency * t * 2 * np.pi).astype(np.float32)
        return wave

    def get_speaker_index(self) -> int:
        device_name = "Speakers (Realtek(R) Audio)"
        device_list = sounddevice.query_devices()
        for device in device_list:
            if device["name"] == device_name:
                return device["index"]
        raise RuntimeError(f"Failed to find audio device '{device_name}'")

    def beep_twice(self):
        self.beep()
        self.beep()

    def alert_major_reset(self):
        self.beep()
        time.sleep(1)

    def alert_upcoming_popup(self):
        self.beep_twice()
