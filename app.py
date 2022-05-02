from datetime import date
import os
from cv2 import *
import cv2 as cv
import cv2
import face_recognition
class Attendance:
    def __init__(self):
        try:
            os.mkdir('attendance_data')
        except:
            pass
        today = date.today()
        today = today.strftime("%b-%d-%Y")
        cam_port = 0
        cam = cv.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
 
            cv.imshow(today, image)
 
            cv.imwrite("attendance_data/{}.png".format(today), image)
            img = image#cv2.imread("attendance_data/{}.png".format(today))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), 
                            (0, 0, 255), 2)
                
                faces = img[y:y + h, x:x + w]
            
                cv2.imwrite(f'img/face{x}.jpg', faces)
                cv.waitKey(1)
            cv.destroyWindow("GeeksForGeeks")

        else:
            print("No image detected. Please! try again")
        box ={}
        tt =[]
        datainfo = []
        students= ['biden','teddy','wren']
        for a in os.listdir('data'):
            datainfo.append(a)
            
        datainfo.sort()
        
        for todayimg in os.listdir('img'):
            for dataimg,stu in zip(datainfo,students):
                today_image = face_recognition.load_image_file('img/{}'.format(todayimg))
                data_image = face_recognition.load_image_file('data/{}'.format(dataimg))
                today_encoding = face_recognition.face_encodings(today_image)[0]
                data_encoding = face_recognition.face_encodings(data_image)[0]
                if face_recognition.compare_faces([today_encoding], data_encoding)[0]==True:
                    tt.append(stu)
        print(tt)
    def compare_faces(face1,face2):
        pass
Attendance()