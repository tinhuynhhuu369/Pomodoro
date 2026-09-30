# Đồng hồ Pomodoro

Ứng dụng desktop Windows đếm giờ Pomodoro đơn giản: 25 phút làm việc, 5 phút nghỉ, hiện thông báo khi hết giờ.

## Tính năng

- Đếm ngược 25 phút cho phiên làm việc, 5 phút cho phiên nghỉ
- Tự động chuyển giữa phiên làm việc và phiên nghỉ
- Thông báo khi hết giờ: popup + âm thanh báo hiệu, cửa sổ tự nổi lên trên cùng
- Các nút Bắt đầu / Tạm dừng / Đặt lại
- Hiển thị số phiên Pomodoro đã hoàn thành trong ngày

## Yêu cầu

- Windows
- Python 3.8+ (chỉ dùng thư viện chuẩn: `tkinter`, `winsound` — không cần cài thêm package nào)

## Cách chạy

```
python main.py
```

## Đóng gói thành .exe (chạy không cần cài Python)

```
pip install pyinstaller
pyinstaller --onefile --windowed --name PomodoroClock main.py
```

File `.exe` sẽ nằm trong thư mục `dist/`.

## Công nghệ

Python thuần + `tkinter` (GUI có sẵn trong Python, không cần cài đặt) + `winsound` (âm báo có sẵn trên Windows).

## Cấu trúc dự án

```
Pomodoro/
├── main.py         # Toàn bộ app: giao diện + logic đếm giờ + thông báo
└── README.md
```

## Roadmap (có thể làm sau)

- Lưu số phiên đã hoàn thành qua ngày (file JSON trong `%APPDATA%`)
- Tùy chỉnh thời gian làm việc/nghỉ qua giao diện
- Icon khay hệ thống (system tray) để chạy ẩn nền
