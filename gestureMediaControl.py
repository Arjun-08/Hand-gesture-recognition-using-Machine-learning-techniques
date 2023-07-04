import cv2
import math
# self made module for hand detection using mediapipe
import handDetectorModule as hd
import pyautogui as pg #allows mouse and keyboard control
import numpy as np

# pycaw library and declarations for audio control
from ctypes import cast, POINTER #allows python to access the existing lib from other languages 
                                 #foreign function lib
from comtypes import CLSCTX_ALL #access com(component object analysis) components and interfaces
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #audio windows library

#use pycaw(pyaudio) lib to get the audio output device and create the pointer to the audio endpoint volume object
devices = AudioUtilities.GetSpeakers() #get list of all the audio output devices on the system
                            #GetSpeakers gives the default audio output device
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None) #allows us to control the volume level of the device
volume = cast(interface, POINTER(IAudioEndpointVolume)) #a pointer to access the volume control at ease

# fn to get range of volume (-65.5 to 0)
volRange = volume.GetVolumeRange()

# taking min and max volume in variables
min = volRange[0]
max = volRange[1]


# fn for volume control
# a4-> thumb finger tip coordinates a8->index finger tip coordinates
# 4-> thumb finger tip  8->index finger tip
def volume_control(frame, a4, a8):
    # circles the tip of the thumb
    cv2.circle(frame, (a4[1], a4[2]), 15, (255, 0, 255), cv2.FILLED)

    # circles the tip of index finger
    cv2.circle(frame, (a8[1], a8[2]), 15, (255, 0, 255), cv2.FILLED)

    # x and y coordinates of 4th and 8th pt
    x1 = a4[1]
    x2 = a8[1]
    y1 = a4[2]
    y2 = a8[2]

    # draw line b/w 4th and 8th pt
    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3) #3 implies thinckness of the line

    # find mid of line and draw circle on it
    midx, midy = (x2 + x1) // 2, (y2 + y1) // 2
    cv2.circle(frame, (midx, midy), 15, (255, 0, 0), cv2.FILLED)

    # find length of line using Pythagoras thm
    length = math.hypot(x2 - x1, y2 - y1)

    # map length to volume
    vol = np.interp(length, [25, 140], [min, max])

    # set volume using pycaw library fn
    volume.SetMasterVolumeLevel(vol, None)

    # draw a rectangle to display volume change and put percentage by mapping volume with 0-100
    '''cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
    bar = np.interp(length, [25, 140], [400, 150])
    cv2.rectangle(frame, (50, int(bar)), (85, 400), (0, 255, 0), cv2.FILLED)
    percent = np.interp(vol, [min, max], [0, 100])
    cv2.putText(frame, f'{int(percent)}%', (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)'''

    return frame


# capture object
cap = cv2.VideoCapture(0)

# create detector object
detector = hd.handDetector()

while True:

    # read image ,flip it and draw the hands
    isTrue, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.find_hands(img)

    # this return list of all 21 points wit index, x and y coordinates from top
    lst = detector.find_position(img, draw=False)
    # print(lst)

    # tips of all fingers except thumb
    finger = [8, 12, 16, 20]

    # check if list is not empty
    if len(lst) > 9:

        # if thumb folded no volume control
        if lst[4][1] < lst[8][1]:
            img = volume_control(img, lst[4], lst[8])

        else:
            # find no. of fingers raised
            m = []
            for i in finger:
                if lst[i][2] > lst[i - 2][2]:
                    m.append(1)
                else:
                    m.append(0)
            # print("sum:",sum(m))

            # if thumb folded and all fingers folded then play/pause
            if lst[4][1] > lst[8][1] and sum(m) >= 4:
                pg.press('playpause')
                # print("pause")

            # if thumb folded and all fingers folded except little finger forward
            elif lst[4][1] > lst[8][1] and sum(m) == 3 and lst[20][2] < lst[18][2]:
                pg.press('right')
                # print("right")

            # if thumb folded and all fingers folded except little finger backward
            elif lst[4][1] > lst[8][1] and sum(m) == 3 and lst[8][2] < lst[6][2]:
                pg.press('left')
                # print("left")
    # display image
    cv2.imshow("image", img)

    # if the q key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
