import numpy as np
import librosa
import matplotlib.pyplot as plt
from audio_processing import calculate_decay_for_band

# Function to generate visualizations (six graphs)
def plot_all_graphs(y, sr):
    # Calculate decay values for different frequency bands
    decay_low = calculate_decay_for_band(y, sr, 20, 200)  # Low frequency range (20-200 Hz)
    decay_mid = calculate_decay_for_band(y, sr, 200, 2000)  # Mid frequency range (200-2000 Hz)
    decay_high = calculate_decay_for_band(y, sr, 2000, 20000)  # High frequency range (2000-20000 Hz)

    # Create the figure with subplots (3 rows, 2 columns)
    fig, axs = plt.subplots(3, 2, figsize=(10, 10))  # Reduced size from (12, 12) to (10, 10)

    # Plot 1: Waveform of the audio
    axs[0, 0].plot(np.linspace(0, len(y) / sr, num=len(y)), y)
    axs[0, 0].set_title("Waveform", fontsize=10)
    axs[0, 0].set_xlabel("Time [s]", fontsize=8)
    axs[0, 0].set_ylabel("Amplitude", fontsize=8)
    axs[0, 0].grid(True)

    # Plot 2: Decay for Low frequency (Line graph)
    axs[0, 1].plot(np.linspace(0, len(y) / sr, num=len(decay_low)), decay_low, color='blue')
    axs[0, 1].set_title("Decay - Low Frequency", fontsize=10)
    axs[0, 1].set_xlabel("Time [s]", fontsize=8)
    axs[0, 1].set_ylabel("Decay", fontsize=8)
    axs[0, 1].grid(True)

    # Plot 3: Decay for Mid frequency (Line graph)
    axs[1, 0].plot(np.linspace(0, len(y) / sr, num=len(decay_mid)), decay_mid, color='orange')
    axs[1, 0].set_title("Decay - Mid Frequency", fontsize=10)
    axs[1, 0].set_xlabel("Time [s]", fontsize=8)
    axs[1, 0].set_ylabel("Decay", fontsize=8)
    axs[1, 0].grid(True)

    # Plot 4: Decay for High frequency (Line graph)
    axs[1, 1].plot(np.linspace(0, len(y) / sr, num=len(decay_high)), decay_high, color='green')
    axs[1, 1].set_title("Decay - High Frequency", fontsize=10)
    axs[1, 1].set_xlabel("Time [s]", fontsize=8)
    axs[1, 1].set_ylabel("Decay", fontsize=8)
    axs[1, 1].grid(True)

    # Plot 5: Frequency Response of the audio signal (in dB)
    D = np.abs(librosa.stft(y))
    freqs = librosa.fft_frequencies(sr=sr)
    magnitude = np.mean(D, axis=1)
    magnitude_db = 20 * np.log10(magnitude)  # Convert to dB

    axs[2, 0].semilogx(freqs, magnitude_db, color='purple')
    axs[2, 0].set_title("Frequency Response (in dB)", fontsize=10)
    axs[2, 0].set_xlabel("Frequency [Hz]", fontsize=8)
    axs[2, 0].set_ylabel("Magnitude [dB]", fontsize=8)
    axs[2, 0].grid(True)

    # Plot 6: Combined RT60 Comparison (Line graph with decay trends for each frequency)
    axs[2, 1].plot(np.linspace(0, len(y) / sr, num=len(decay_low)), decay_low, color='blue', label="Low")
    axs[2, 1].plot(np.linspace(0, len(y) / sr, num=len(decay_mid)), decay_mid, color='orange', label="Mid")
    axs[2, 1].plot(np.linspace(0, len(y) / sr, num=len(decay_high)), decay_high, color='green', label="High")
    axs[2, 1].set_title("Decay Comparison (Low, Mid, High Frequencies)", fontsize=10)
    axs[2, 1].set_xlabel("Time [s]", fontsize=8)
    axs[2, 1].set_ylabel("Decay", fontsize=8)
    axs[2, 1].legend()
    axs[2, 1].grid(True)

    # Adjust layout for better readability
    plt.tight_layout(pad=1.0)  # Increase the padding for better spacing
    plt.show()
