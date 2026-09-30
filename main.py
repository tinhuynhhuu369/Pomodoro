import tkinter as tk

WORK_MINUTES = 25
BREAK_MINUTES = 5

root = tk.Tk()
root.title("Đồng hồ Pomodoro")
root.geometry("320x260")
root.resizable(False, False)

status_label = tk.Label(root, text="Làm việc", font=("Helvetica", 16))
status_label.pack(pady=(20, 0))

time_label = tk.Label(root, text=f"{WORK_MINUTES:02d}:00", font=("Helvetica", 48))
time_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Bắt đầu", width=8)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Tạm dừng", width=8)
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Đặt lại", width=8)
reset_button.grid(row=0, column=2, padx=5)

root.mainloop()
