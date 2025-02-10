import cv2

def draw_bounding_box(image, hand_landmarks, hand_label, total_fingers):
    """
    Draws a bounding box around the detected hand, displays the hand label, and finger count.
    """
    h, w, _ = image.shape
    x_min, y_min = w, h
    x_max, y_max = 0, 0

    # Calculate bounding box coordinates
    for lm in hand_landmarks.landmark:
        x, y = int(lm.x * w), int(lm.y * h)
        x_min, y_min = min(x_min, x), min(y_min, y)
        x_max, y_max = max(x_max, x), max(y_max, y)

    # Draw the bounding box
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Combine hand label and finger count
    text_hand = f"{hand_label} Hand"
    text_fingers = f"Fingers: {total_fingers}"

    # Determine if the bounding box is too small to fit both texts in one line
    text_width = max(cv2.getTextSize(text_hand, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0][0],
                     cv2.getTextSize(text_fingers, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0][0])
    if x_max - x_min < text_width:
        # Draw filled rectangle for the background of the text (wrapped)
        cv2.rectangle(image, (x_min - 1, y_min - 40), (x_min + text_width + 10, y_min), (0, 255, 0), cv2.FILLED)
        # Put the text on the image (wrapped)
        cv2.putText(image, text_hand, (x_min + 5, y_min - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, text_fingers, (x_min + 5, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    else:
        # Draw filled rectangle for the background of the text (single line)
        cv2.rectangle(image, (x_min - 1, y_min - 20), (x_max + 1, y_min), (0, 255, 0), cv2.FILLED)
        # Put the text on the image (single line)
        cv2.putText(image, f"{text_hand} - {text_fingers}", (x_min + 5, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
