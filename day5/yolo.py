from ultralytics import YOLO
import cv2

# ----------------------------
# Load model
# ----------------------------
model = YOLO("yolov8n.pt")      # detection model
print("Loaded classes:", model.names)

# ----------------------------
# Open webcam
# ----------------------------
cap = cv2.VideoCapture(0)

# Fix zoom issue by setting camera size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

filter_class = None   # None = all classes, 0 = person

print("\nPRESS 1 = Detect ALL classes")
print("PRESS 2 = Detect ONLY PERSON")
print("PRESS q = Quit")

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # ----------------------------
    # PREPROCESS IMAGES
    # ----------------------------
    resized = cv2.resize(frame, (400, 300))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(resized, (15, 15), 0)

    # ----------------------------
    # YOLO DETECTION ON ORIGINAL FRAME
    # ----------------------------
    if filter_class is None:
        results = model(frame)  # all classes
    else:
        results = model(frame, classes=[filter_class])  # filtered

    annotated = results[0].plot()  # drawing boxes

    # ----------------------------
    # SHOW ALL WINDOWS
    # ----------------------------
    cv2.imshow("Original Frame (No Zoom)", frame)
    cv2.imshow("YOLO Detection", annotated)
    cv2.imshow("Resized Frame", resized)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Blur Frame", blur)

    # ----------------------------
    # KEYBOARD CONTROLS
    # ----------------------------
    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        filter_class = None
        print("Switched → Detect ALL classes")

    if key == ord('2'):
        filter_class = 0
        print("Switched → Detect PERSON only")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
