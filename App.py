import tkinter as tk
import time

def start_pomodoro():
    """Start the Pomodoro timer."""
    work_time = 25 * 60  # 25 minutes
    short_break_time = 5 * 60  # 5 minutes
    long_break_time = 15 * 60  # 15 minutes
    cycles = int(entry_cycles.get())
    for _ in range(cycles):
        countdown(work_time, "Work")
        countdown(short_break_time, "Short Break")
    countdown(long_break_time, "Long Break")

def countdown(time_in_seconds, label):
    """Countdown function for the Pomodoro timer."""
    for _ in range(time_in_seconds):
        minutes, seconds = divmod(time_in_seconds, 60)
        label_result.config(text=f"{label}: {minutes:02}:{seconds:02}")
        root.update()
        time.sleep(1)
        time_in_seconds -= 1

# Create the main window
root = tk.Tk()
root.title("Pomodoro Timer")

# Create and place widgets
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_cycles = tk.Label(frame_input, text="Enter number of cycles:")
label_cycles.pack()

entry_cycles = tk.Entry(frame_input)
entry_cycles.pack()

button_start = tk.Button(frame_input, text="Start Pomodoro", command=start_pomodoro)
button_start.pack(pady=5)

label_result = tk.Label(frame_input, text="Timer will appear here")
label_result.pack()

# Start the main loop
root.mainloop()
