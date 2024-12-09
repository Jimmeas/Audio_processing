import librosa
import numpy as np
import scipy.signal as signal
from pydub import AudioSegment


# Function to convert mp3 or aac to wav
def convert_to_wav(input_file):
    if input_file.endswith(('.mp3', '.aac')):
        audio = AudioSegment.from_file(input_file)
        wav_file = input_file.rsplit('.', 1)[0] + ".wav"
        audio.export(wav_file, format="wav")
        return wav_file
    return input_file


# Function to remove metadata
def remove_metadata(audio_file):
    audio = AudioSegment.from_file(audio_file)
    audio.export(audio_file, format="wav")  # Save without metadata
    return audio_file


# Function to load audio file
def load_audio(file_path):
    if file_path.endswith(('.mp3', '.aac')):
        file_path = convert_to_wav(file_path)
    file_path = remove_metadata(file_path)
    y, sr = librosa.load(file_path, sr=None, mono=True)  # Load as mono
    return y, sr


# Function to compute the decay of the filtered signal
def compute_decay(filtered_signal):
    decay = np.abs(filtered_signal)  # Absolute value of the signal
    decay = decay / np.max(decay)  # Normalize to the max value for better comparison
    return decay


# Function to compute RT60 for a given frequency band (Low, Mid, High)
def calculate_decay_for_band(y, sr, low_freq, high_freq):
    # Bandpass filter to isolate a frequency band
    nyquist = 0.5 * sr
    low = low_freq / nyquist
    high = high_freq / nyquist
    b, a = signal.butter(4, [low, high], btype='band')
    filtered_signal = signal.filtfilt(b, a, y)

    # Compute the decay of the filtered signal
    decay = compute_decay(filtered_signal)

    return decay
