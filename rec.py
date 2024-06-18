import cv2, sys, numpy, os
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def adduser(name):

    datasets = 'datasets'
    sub_data = name

    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)

    (width, height) = (130, 100)
    count = 1
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for(x,y,w,h) in faces:
            face_cropped = img[y:y + h, x:x + w]
            return face_cropped

    try:
        cap = cv2.VideoCapture(0)
        img_id = 0
        id = 3
        while True:
            ret, my_frame = cap.read()
            if face_cropped(my_frame) is not None:
                img_id += 1
                face_resize = cv2.resize(face_cropped(my_frame), (500, 500))
                face = cv2.resize(face_cropped(my_frame), (500, 500))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                fontScale = 1
                thickness = 2
                color = (178, 190, 181)
                cv2.imwrite('% s/% s.png' % (path, count),face_resize)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow("Cropped Face",face)
                count+=1
            if cv2.waitKey(1) == 13 or int(img_id) == 100:
                break;

        cap.release()
        cv2.destroyAllWindows()
        print("Completed")
    except Exception as es:
        print(str(es))
