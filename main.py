from kivy.app import App # type: ignore
from kivy.uix.image import Image # type: ignore
from kivy.clock import Clock # type: ignore
from kivy.graphics.texture import Texture # type: ignore
import cv2

class FaceDetectorApp(App):
    def build(self):
        # This widget will display the camera feed
        self.img = Image()
        # Connect to the webcam (0 is usually the default laptop cam)
        self.capture = cv2.VideoCapture(0)
        # Load the pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Schedule the 'update' function to run 30 times per second
        Clock.schedule_interval(self.update, 1.0/30.0)
        return self.img

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert to grayscale for detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Convert the OpenCV frame (BGR) to Kivy texture (RGB)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = texture

if __name__ == '__main__':
    FaceDetectorApp().run()