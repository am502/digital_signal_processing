import sounddevice
from scipy.io.wavfile import write

fs = 44100
sec = 27
recorded = sounddevice.rec(int(sec * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("recorded.wav", fs, recorded)
