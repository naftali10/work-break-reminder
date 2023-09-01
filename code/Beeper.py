import time
import pyaudio
import numpy as np


class Beeper:

    def __init__(self):
        self.frequency: int = 1500
        self.single_beep_duration: float = 0.75
        self.audio = pyaudio.PyAudio()

    def beep(self) -> None:
        wave = self.make_sine_wave()
        try:
            stream = self.audio.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=48000,
                output=True,
                output_device_index=self.get_speaker_index()
            )
            stream.write(wave)
            stream.close()
        except RuntimeError as e:
            raise RuntimeError(f"Beeper Error: {e}")

    def make_sine_wave(self) -> np:
        t = np.linspace(0, self.single_beep_duration, int(self.single_beep_duration * 48000), False)
        wave = np.sin(self.frequency * t * 2 * np.pi).astype(np.float32)
        return wave

    def get_speaker_index(self) -> int:
        device_name = "Speakers (Realtek(R) Audio)"
        for i in range(self.audio.get_device_count()):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info["name"] == device_name:
                device_index = i
                return device_index
        raise RuntimeError(f"Failed to find audio device '{device_name}'")

    def beep_twice(self):
        self.beep()
        self.beep()

    def alert_major_reset(self):
        self.beep()
        time.sleep(1)

    def alert_upcoming_popup(self):
        self.beep_twice()
