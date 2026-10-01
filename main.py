import tkinter as tk
import winsound
from tkinter import messagebox

WORK_MINUTES = 25
BREAK_MINUTES = 5

MODE_LABELS = {"work": "Làm việc", "break": "Nghỉ"}
MODE_COLORS = {"work": "#f6d6d0", "break": "#d4ecd9"}  # đỏ nhạt = tập trung, xanh lá nhạt = thư giãn

mode = "work"
time_left = WORK_MINUTES * 60
is_running = False
sessions_completed = 0
after_id = None  # id của lần gọi root.after đang chờ, để hủy khi tạm dừng/đặt lại


def format_time(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def mode_duration(current_mode):
    minutes = WORK_MINUTES if current_mode == "work" else BREAK_MINUTES
    return minutes * 60


def update_time_label():
    time_label.config(text=format_time(time_left))


def cancel_pending_tick():
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None


def tick():
    global time_left, after_id
    after_id = None
    if not is_running:
        return
    if time_left > 0:
        time_left -= 1
        update_time_label()
    if time_left == 0:
        on_session_end()
    else:
        after_id = root.after(1000, tick)


def apply_mode_style():
    status_label.config(text=MODE_LABELS[mode])
    color = MODE_COLORS[mode]
    # Label và Frame không tự lấy màu nền của cửa sổ nên phải đổi từng cái
    for widget in (root, status_label, time_label, button_frame, sessions_label):
        widget.config(bg=color)


def on_session_end():
    global mode, time_left, sessions_completed, after_id
    if mode == "work":
        sessions_completed += 1
        sessions_label.config(text=f"Số phiên hôm nay: {sessions_completed}")
        mode = "break"
    else:
        mode = "work"
    time_left = mode_duration(mode)
    update_time_label()
    apply_mode_style()
    notify()
    # Chỉ hẹn tick sau khi đóng popup, để popup không bị dồn nếu người dùng chưa kịp bấm OK
    after_id = root.after(1000, tick)


def notify():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    # Đưa cửa sổ lên trên cùng để không bỏ lỡ thông báo khi đang dùng app khác
    root.attributes("-topmost", True)
    root.lift()
    if mode == "break":
        message = f"Hết giờ làm việc — nghỉ {BREAK_MINUTES} phút nhé"
    else:
        message = "Hết giờ nghỉ — quay lại làm việc"
    messagebox.showinfo("Hết giờ!", message, parent=root)
    # Tắt topmost sau khi đóng popup, nếu không cửa sổ sẽ đè lên mọi app khác mãi
    root.attributes("-topmost", False)


def start():
    global is_running, after_id
    if is_running:
        return  # tránh bấm nhiều lần tạo nhiều vòng tick chạy song song
    is_running = True
    after_id = root.after(1000, tick)


def pause():
    global is_running
    is_running = False
    cancel_pending_tick()


def reset():
    global is_running, time_left
    is_running = False
    cancel_pending_tick()
    time_left = mode_duration(mode)
    update_time_label()


root = tk.Tk()
root.title("Đồng hồ Pomodoro")
root.geometry("320x260")
root.resizable(False, False)

status_label = tk.Label(root, text=MODE_LABELS[mode], font=("Helvetica", 16))
status_label.pack(pady=(20, 0))

time_label = tk.Label(root, text=format_time(time_left), font=("Helvetica", 48))
time_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Bắt đầu", width=8, command=start)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Tạm dừng", width=8, command=pause)
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Đặt lại", width=8, command=reset)
reset_button.grid(row=0, column=2, padx=5)

sessions_label = tk.Label(root, text=f"Số phiên hôm nay: {sessions_completed}", font=("Helvetica", 10))
sessions_label.pack(pady=(20, 0))

apply_mode_style()

root.mainloop()
