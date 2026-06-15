from ultralytics import YOLO
import cv2

model = YOLO("/Users/rishi/gitnew/Object-Detector-Pen-/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.55,verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("Pen Detector", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
