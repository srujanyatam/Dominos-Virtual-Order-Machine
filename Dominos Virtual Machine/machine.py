import os
from cvzone.HandTrackingModule import HandDetector
import cv2


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imbackground=cv2.imread("Resources/backgroung img.png")

folderpathmodes=("Resources/modes")
listimagemodepath=(os.listdir(folderpathmodes))
listimagemode=[]
for imgmodepath in listimagemodepath:
    listimagemode.append(cv2.imread(os.path.join(folderpathmodes,imgmodepath)))
print(listimagemode)

modetype=0 #changing selection mode
selection=-1
counter=0
selectionspeed = 7

detector=HandDetector(detectionCon=0.8,maxHands=1)
modepositions=[(948,104),(1176,166),(948,394),(1176,505)]
counterpause=0

while True:
    success,img=cap.read()
    #find the hands and its land marks
    hands,img = detector.findHands(img)

    #overlaying the webcam
    imbackground[125:125+480,15:15+640]=img
    imbackground[0:720,847:1280]=listimagemode[modetype]

    if hands and counterpause==0 and modetype<4:
        hand1=hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        if fingers1==[0,1,0,0,0]:
            if selection != 1:
                counter = 1
            selection=1
        elif fingers1==[0,1,1,0,0]:
            if selection != 2:
                counter = 1
            selection=2
        elif fingers1==[0,1,1,1,0]:
            if selection != 3:
                counter = 1
            selection=3
        elif fingers1==[0,1,1,1,1]:
            if selection != 4:
                counter = 1
            selection=4
        else:
            selection = -1
            counter = 0
        if counter>0:
            counter+=1
            print(counter)

            cv2.ellipse(imbackground,modepositions[selection-1],(103,103),0,0,counter*selectionspeed,(0,255,0),10)
            if counter*selectionspeed>360:
                modetype +=1
                counter=0
                selection=-1
                counterpause=1

    if counterpause>0:
        counterpause +=1
        if counterpause>60:
            counterpause=0

    # displaying
    #cv2.imshow("image",img)
    cv2.imshow("backgroung img",imbackground)
    cv2.waitKey(1)
    
    
    
    