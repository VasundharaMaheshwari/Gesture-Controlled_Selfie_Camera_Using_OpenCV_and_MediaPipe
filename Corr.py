import cv2
import mediapipe as mp
import random
def coordinate_lock(id, h, w, takepic):
    if takepic==0:
         cx, cy = int(lm.x*w), int(lm.y*h)
         cv2.circle(img, (int(cx), int(cy)), 5, (255,255,255), cv2.FILLED)
         return cy
    else:
        return 0
Framewidth=640
Frameheight=480
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Cap=cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
Cap.set(3,Framewidth)
Cap.set(4,Frameheight)
Cap.set(10,150)
handsup=0
thumbup=0
fingerdown=0
takepic=0
cywhisk=0
cymiddle=0
cythumb=0
cythumb2=0
cyf1lower=0
cyf1upper=0
cyf2lower=0
cyf2upper=0
cyf3lower=0
cyf3upper=0
cyf4lower=0
cyf4upper=0
while True:
     success , img = Cap.read()
     Grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
     results = hands.process(imgRGB)
     Face = faceCascade.detectMultiScale(img,6,0)
     if takepic==0:
        for ( x ,y ,w ,h ) in Face:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 2)
            cv2.putText(img, 'Face Captured', (x,y-10), cv2.FONT_HERSHEY_PLAIN, 2.0, (255,0,255), 2)
     h,w,c = img.shape
     if results.multi_hand_landmarks:
         for handLms in results.multi_hand_landmarks:
             for id, lm in enumerate(handLms.landmark):
                 if (id==0):
                     cywhisk = coordinate_lock(0,h,w,takepic)
                 if (id==10):
                     cymiddle = coordinate_lock(10,h,w,takepic)
                 if (id==2):
                     cythumb = coordinate_lock(2,h,w,takepic)
                 if (id==3):
                     cythumb2 = coordinate_lock(3,h,w,takepic)
                 if (id==5):
                     cyf1lower = coordinate_lock(5,h,w,takepic)
                 if (id==9):
                     cyf2lower = coordinate_lock(9,h,w,takepic)
                 if (id==13):
                     cyf3lower = coordinate_lock(13,h,w,takepic)
                 if (id==17):
                     cyf4lower = coordinate_lock(17,h,w,takepic)
                 if (id==8):
                     cyf1upper = coordinate_lock(8,h,w,takepic)
                 if (id==12):
                     cyf2upper = coordinate_lock(12,h,w,takepic)
                 if (id==16):
                     cyf3upper = coordinate_lock(16,h,w,takepic)
                 if (id==20):
                     cyf4upper = coordinate_lock(20,h,w,takepic)
                 if cythumb2<cythumb:
                     thumbup=1
                 else:
                     thumbup=0
                 if cymiddle<cywhisk:
                     handsup=1
                 else:
                     handsup=0
                 if cyf1lower<cyf1upper and cyf2lower<cyf2upper and cyf3lower<cyf3upper and cyf4lower<cyf4upper:
                     fingerdown=1
                 else:
                     fingerdown=0
                 if fingerdown==1 and handsup==1 and takepic==0 and thumbup==1:
                     takepic=120
     if takepic>1:
         if takepic>=90:
             cv2.putText(img, '3', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 3)
         elif takepic>=60:
             cv2.putText(img, '2', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 3)
         elif takepic>=30:
             cv2.putText(img, '1', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 3)
         takepic= takepic-1
     elif takepic==1:
         meow = random.randint(0,1000)
         cv2.imwrite('Picture' + str(meow) + '.jpg', img)
         fingerdown=0
         takepic=0
         thumbup=0
         handsup=0
     cv2.imshow('result',img)
     if cv2.waitKey(1) & 0xFF == 27:
         break
Cap.release()
cv2.destroyAllWindows()