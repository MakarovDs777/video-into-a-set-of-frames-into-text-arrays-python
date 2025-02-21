import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
import os

def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем корневое окно
    file_path = filedialog.askopenfilename(title="Выберите файл видео", filetypes=[("Video files", ".mp4;.avi;.mov")])
    
    if file_path:  # Проверяем, выбран ли файл
        # Создание папки на рабочем столе для сохранения кадров
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_name = "video_frames"
        frames_folder = os.path.join(desktop_path, folder_name)
        os.makedirs(frames_folder, exist_ok=True)

        # Открытие видео
        video_capture = cv2.VideoCapture(file_path)
        frame_count = 0

        while True:
            ret, frame = video_capture.read()  # Чтение кадра
            if not ret:
                break  # Выход из цикла, если кадры кончились

            frame_count += 1
            # Преобразование цвета BGR в RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            np.set_printoptions(threshold=np.inf)  # Выводим все элементы массива
            
            # Сохранение массива в текстовый файл соответствующего кадра
            text_file_path = os.path.join(frames_folder, f"frame_{frame_count}.txt")
            np.savetxt(text_file_path, rgb_frame.reshape(-1, rgb_frame.shape[2]), fmt='%d')
            print(f"Кадр {frame_count} сохранен в {text_file_path}")

        video_capture.release()
        print(f"Обработка видео завершена. Сохранено {frame_count} кадров.")
    else:
        print("Файл не выбран.")

# Запуск диалогового окна
select_video_file()
