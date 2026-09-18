import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not working")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Cannot read camera")
        break

    try:
        result = DeepFace.analyze(
            img_path=frame,
            actions=["emotion"],
            detector_backend="opencv",
            enforce_detection=True,
            silent=True
        )

        if isinstance(result, list):
            result = result[0]

        emotion = result["dominant_emotion"]
        region = result["region"]

        x = region["x"]
        y = region["y"]
        w = region["w"]
        h = region["h"]

        # Face box
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Emotion
        cv2.putText(
            frame,
            "Emotion: " + emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    except Exception:
        cv2.putText(
            frame,
            "No face detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    cv2.imshow("Face + Emotion Detection", frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
