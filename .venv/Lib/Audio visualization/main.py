import tkinter as tk
from tkinter import filedialog, messagebox
from audio_processing import load_audio
from visualization import plot_all_graphs

# Function to display output in the GUI
def display_results():
    result_text.set("Decay plots for Low, Mid, and High frequencies displayed!")

# Main Application (GUI setup)
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.aac *.wav")])
    if file_path:
        try:
            y, sr = load_audio(file_path)
            display_results()
            plot_all_graphs(y, sr)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the Tkinter window
window = tk.Tk()
window.title("RT60 Analysis")

# Create a button to load the audio file
load_button = tk.Button(window, text="Load Audio File", command=load_file)
load_button.pack(pady=20)

# Label to display results
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=10)

# Start the GUI
window.mainloop()
