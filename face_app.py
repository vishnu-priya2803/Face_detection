import cv2
import tkinter as tk
from tkinter import messagebox
import winsound
import face_recognition
import os
import time

# 📂 Database folder path
DB_PATH = r"C:\Users\vishn\face_detection_app\face_db"

known_encodings = []
known_names = []

print("📂 Loading face database...")

# Load all images from database folder
for file in os.listdir(DB_PATH):
    if file.lower().endswith((".jpg", ".png")):
        image_path = os.path.join(DB_PATH, file)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(file)   # filename used as name
            print("✅ Loaded:", file)
        else:
            print("❌ No face found in:", file)

print("Total faces loaded:", len(known_encodings))

if len(known_encodings) == 0:
    print("❌ No valid faces in database!")
    exit()

camera = None
running = False
last_beep_time = 0


def play_sound():
    global last_beep_time
    if time.time() - last_beep_time > 2:
        winsound.Beep(1000, 200)
        last_beep_time = time.time()


def start_camera():
    global camera, running
    camera = cv2.VideoCapture(0)
    running = True
    detect_faces()


def stop_camera():
    global camera, running
    running = False
    if camera:
        camera.release()
    cv2.destroyAllWindows()


def detect_faces():
    if not running:
        return

    ret, frame = camera.read()
    if not ret:
        messagebox.showerror("Error", "Camera not working")
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        distances = face_recognition.face_distance(
            known_encodings,
            face_encoding
        )

        min_distance = min(distances)
        best_match_index = distances.tolist().index(min_distance)

        THRESHOLD = 0.72   # tuned for your images

        if min_distance < THRESHOLD:
            label = "Vishnu Priya"     # 👈 Your name here
            color = (0, 255, 0)
        else:
            label = "Unknown"
            color = (0, 0, 255)
            play_sound()

        print("Min distance:", round(min_distance, 3), "|", label)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, label, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Face Database App", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_camera()
        return

    root.after(10, detect_faces)


# 🖥️ GUI Window
root = tk.Tk()
root.title("Face Database App")
root.geometry("300x200")
root.resizable(False, False)

title = tk.Label(root, text="Face Database App",
                 font=("Arial", 16, "bold"))
title.pack(pady=20)

start_btn = tk.Button(root, text="Start Camera",
                      font=("Arial", 12),
                      bg="green", fg="white",
                      command=start_camera)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Camera",
                     font=("Arial", 12),
                     bg="red", fg="white",
                     command=stop_camera)
stop_btn.pack(pady=10)

root.mainloop()
