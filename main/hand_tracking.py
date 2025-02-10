import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Define finger tip indices
FINGER_TIPS = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
FINGER_BASES = [2, 6, 10, 14, 18]  # Lower joint of each finger

def process_frame(frame):
    """Processes the frame and detects hand landmarks."""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    return results

def fingersUp(hand_landmarks, hand_label):
    """Determines which fingers are up accurately with a margin for stability."""
    fingers = []
    
    # Thumb Detection (Checks horizontal spread from wrist)
    thumb_tip = hand_landmarks.landmark[FINGER_TIPS[0]]
    thumb_ip = hand_landmarks.landmark[FINGER_BASES[0]]  # Thumb lower joint (IP)
    wrist = hand_landmarks.landmark[0]

    # Thumb is extended if it is far from the palm center
    thumb_extended = abs(thumb_tip.x - wrist.x) > abs(thumb_ip.x - wrist.x)
    fingers.append(1 if thumb_extended else 0)

    # Safety margin for other fingers
    MARGIN = 0.02  # Adjust this for better stability

    for i in range(1, 5):  # Index, Middle, Ring, Pinky
        tip = hand_landmarks.landmark[FINGER_TIPS[i]]
        base = hand_landmarks.landmark[FINGER_BASES[i]]

        # Finger is up if tip is **clearly above** the base (with margin)
        fingers.append(1 if tip.y < base.y - MARGIN else 0)

    return fingers
