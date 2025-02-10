import cv2
import time
from hand_tracking import process_frame, fingersUp
from bounding_box import draw_bounding_box
import mediapipe as mp

# Initialize the camera
cap = cv2.VideoCapture(0)

prev_time = 0  # For FPS calculation
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_hands_styles = mp.solutions.drawing_styles

def process_and_draw(frame):
    """Process the frame, detect hands, draw landmarks, and count fingers."""
    results = process_frame(frame)  # Detect hands first

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = hand_info.classification[0].label  # 'Left' or 'Right'

            # Count fingers
            fingers = fingersUp(hand_landmarks, hand_label)  
            totalFingers = fingers.count(1)

            # Draw bounding box with finger count and hand label
            draw_bounding_box(frame, hand_landmarks, hand_label, totalFingers)

        # Draw landmarks LAST to maintain original colours
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_hands_styles.get_default_hand_landmarks_style(),
                mp_hands_styles.get_default_hand_connections_style()
            )

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for a mirrored view
    h, w, _ = frame.shape  # Get frame dimensions

    # Process the frame and draw landmarks and bounding boxes
    process_and_draw(frame)

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Display FPS on the top-left corner
    cv2.putText(frame, f'FPS: {fps:.2f}', (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Hand Recognition - Azfar Danish', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
