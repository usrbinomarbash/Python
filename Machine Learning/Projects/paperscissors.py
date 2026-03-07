import cv2
import random
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("RPS AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


choices = ["Rock", "Paper", "Scissors"]
ai_choice = random.choice(choices)
