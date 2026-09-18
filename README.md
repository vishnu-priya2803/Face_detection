Face Recognition and Emotion Detection

📌 Project Overview

This project uses **Python, OpenCV, and DeepFace** to detect a person's face through a webcam and identify their facial emotion in real time.

The system captures video from the webcam, detects the face, and analyzes the facial expression to display the detected emotion.

🎯 Objectives

 Detect faces using a webcam.
 Detect facial emotions in real time.
 Display a box around the detected face.
 Display the detected emotion on the screen.
 Provide a simple and easy-to-use computer vision application.

 🛠️ Technologies Used

Python 3.11
OpenCV
DeepFace
TensorFlow
NumPy
😊 Emotions Detected

The system can detect emotions such as:
 Happy
Sad
Angry
 Fear
 Surprise
 Disgust
 Neutral
 ⚙️ How It Works

text
Webcam
   ↓
Capture Video
   ↓
Face Detection
   ↓
Extract Face
   ↓
DeepFace Emotion Analysis
   ↓
Display Emotion
 📂 Project Structure
text
Face-Emotion-Detection/
│
├── 5.py
└── README.md

💻 Installation

Make sure **Python 3.11** is installed.

Open Command Prompt and install the required packages:

bash
py -3.11 -m pip install opencv-python
py -3.11 -m pip install deepface
py -3.11 -m pip install tf-keras

 ▶️ How to Run

Open Command Prompt in the project folder and run:

bash
py -3.11 5.py


The webcam will open automatically.

The application will show:

* A rectangle around the detected face.
* The detected emotion above the face.

### ⏹️ Stop the Camera

Press:

```text
Q
```

to close the camera window.

## 📸 Example

When a face is detected, the application displays:

```text
+----------------+
|                |
|    FACE        |
|   DETECTED     |
|                |
+----------------+

Emotion: Happy
```

## ✨ Features

* Real-time webcam detection
* Face detection
* Emotion recognition
* No database required
* No face image folder required
* Simple Python implementation

## 🚀 Future Improvements

* Add person identification/face recognition.
* Add a graphical user interface.
* Detect multiple faces at the same time.
* Store emotion results.
* Display emotion statistics using graphs.
* Improve detection speed and accuracy.

## 👩‍💻 Author

**Vishnu Priya**

B.Tech – Computer Science and Engineering (Data Science)

## 📄 License

This project is created for educational and project purposes.
