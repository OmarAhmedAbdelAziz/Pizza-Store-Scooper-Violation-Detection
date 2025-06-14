# Importing Libraries
import cv2
from ultralytics import YOLO

# Loading Model
model = YOLO("/content/best.pt")

# Loading Video
video_path = "/content/wrong.mp4"
cap = cv2.VideoCapture(video_path)

# Getting Video Properties
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

# Output Video Specs
output_path = "ViolationDetection.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Making the ROIs of Contatiners
container_rois = [
        [300, 630, 350, 700],  # Container 1
        [320, 575, 360, 630],  # Container 2
        [330, 520, 375, 575],  # Container 3
        [335, 475, 385, 520],  # Container 4
        [340, 425, 395, 475],  # Container 5
        [350, 380, 420, 425],  # Container 6
        [380, 335, 435, 380],  # Container 7
        [390, 305, 440, 335],  # Container 8
        [400, 260, 450, 305],  # Container 9
]

# Checking Bounding Box Overlap
def is_overlap(boxA, boxB):
    ax1, ay1, ax2, ay2 = boxA
    bx1, by1, bx2, by2 = boxB
    return not (min(ax2, bx2) < max(ax1, bx1) or min(ay2, by2) < max(ay1, by1))

# Violation Counter
violation_count = 0
roi_violation_states = [False] * len(container_rois)

# Start
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.25, verbose=False)[0]

    hands = []
    scoopers = []

    for box in results.boxes:
        cls = int(box.cls)
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = results.names[cls]
        if label == "hand":
            hands.append((x1, y1, x2, y2))
        elif label == "scooper":
            scoopers.append((x1, y1, x2, y2))


    for idx, roi in enumerate(container_rois):
        hand_in_roi = any(is_overlap(hand, roi) for hand in hands)
        scooper_in_roi = any(is_overlap(scooper, roi) for scooper in scoopers)

        current_violation = hand_in_roi and not scooper_in_roi


        if current_violation and not roi_violation_states[idx]:
            violation_count += 1
            roi_violation_states[idx] = True
        elif not current_violation:
            roi_violation_states[idx] = False

    # Drawing ROIs and Detection
    for roi in container_rois:
        cv2.rectangle(frame, roi[:2], roi[2:], (0, 255, 255), 2)
    for hand in hands:
        cv2.rectangle(frame, hand[:2], hand[2:], (0, 0, 255), 2)
    for scooper in scoopers:
        cv2.rectangle(frame, scooper[:2], scooper[2:], (0, 255, 0), 2)

    # Display violation count
    cv2.putText(frame, f"Violations: {violation_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    out.write(frame)


cap.release()
out.release()
