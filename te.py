import numpy as np
import cv2

def play_thermal_video(file_path):
    # 1. Load dữ liệu từ file .npy
    try:
        data = np.load(file_path)
        print(f"Dữ liệu đã tải: {data.shape}") # In ra shape để kiểm tra
    except FileNotFoundError:
        print("Không tìm thấy file. Vui lòng kiểm tra lại đường dẫn.")
        return

    # 2. Vòng lặp qua từng khung hình
    for i, frame in enumerate(data):
        # Chuẩn hóa dữ liệu để hiển thị (vì dữ liệu nhiệt thường có range giá trị lạ)
        # Chuyển về dạng 8-bit (0-255)
        frame_norm = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
        frame_8bit = frame_norm.astype(np.uint8)

        # Áp dụng màu nhiệt (Color Map) để dễ quan sát hơn
        # Bạn có thể thử COLORMAP_JET, COLORMAP_HOT hoặc COLORMAP_MAGMA
        color_frame = cv2.applyColorMap(frame_8bit, cv2.COLORMAP_JET)

        # Hiển thị
        cv2.imshow('Thermal Video', color_frame)

        # Nhấn 'q' để thoát hoặc dừng 30ms giữa các frame
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

# Sử dụng hàm
play_thermal_video('thermal_video.npy')