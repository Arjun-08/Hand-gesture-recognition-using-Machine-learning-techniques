# import library
import mediapipe as mp #hand detecting class- pre-trained
import cv2 #to process image and video

# class to initialize values and functions
class handDetector: # pretrained class in mediapipe to detect hands

    # constructor
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils


    # check for hands and draw them and return the image with drawn one
    def find_hands(self, img, draw=True): #checks for the hands in the input image and adds landmarks
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert image into RGB form
        self.result = self.hands.process(imgRgb) #run the handDectector model on the processed image
        if self.result.multi_hand_landmarks: #if hand detected move to next line
            for handlms in self.result.multi_hand_landmarks: #adds adn saves the hadn landmarks on loop adn assigns to handlms
                if draw: #if draw is true
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS) #draws landmarks on the image using...
        return img

    # returns list of position of all the points
    def find_position(self, img, handno=0, draw=True):
        lst = []

        if self.result.multi_hand_landmarks: #if hand detected move to next line
            myhand = self.result.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                l, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * l)
                lst.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED) #fill the positions in the list and return
        return lst
