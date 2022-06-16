# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)
from datetime import date
import os
from cv2 import *
import cv2 as cv
import cv2
import shutil
import face_recognition
class Omark:
    def __init__(self,students,data):
        try:
            os.mkdir('attendance_data')
        except:
            pass 
        
           
        try:
            box =[]
            for iaa in open(students, 'r').readlines():
                for a in range(100):
                    iaa = iaa.strip(' '*a)
                    iaa = iaa.strip('\n'*a)
                box.append(iaa)
            self.total_students = students
            self.students= students
        except FileNotFoundError as e:
            print(e)
        
        try:
            os.mkdir('attendance_data')
        except:
            pass
        today = date.today()
        today = today.strftime("%b-%d-%Y")
        cam_port = 0
        cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)
        result, image = cam.read()
        if result:
 
            cv.imshow(today, image)
 
            cv.imwrite("attendance_data/{}.png".format(today), image)
            img = image 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), 
                            (0, 0, 255), 2)
                
                faces = img[y:y + h, x:x + w]
            
                cv2.imwrite(f'img/face{x}.jpg', faces)
                cv.waitKey(1)
           

        else:
            print("No image detected. Please! try again")
        box ={}
        tt =[]
        datainfo = []
        students= self.students
        for a in os.listdir(data):
            datainfo.append(a)
            
        datainfo.sort()
        
        for todayimg in os.listdir('img'):
            for dataimg,stu in zip(datainfo,students):
                today_image = face_recognition.load_image_file('img/{}'.format(todayimg))
                data_image = face_recognition.load_image_file('{}/{}'.format(data,dataimg))
                today_encoding = face_recognition.face_encodings(today_image)[0]
                data_encoding = face_recognition.face_encodings(data_image)[0]
                if face_recognition.compare_faces([today_encoding], data_encoding)[0]==True:
                    tt.append(stu)
        print(tt)
        shutil.rmtree('img')
        self.present = tt
        for iki in tt:
            students.remove(iki)
        self.absent= students
        cv2.destroyAllWindows()
        
    def register(self):
        for k,l in zip(self.present,self.absent):
            print('{} Number of students in class'.format((len(self.total_students))))
            print('{} students presents and {} students absent'.format(len(self.present)),len(self.present))
            print('{} | Present'.format(self.present))
            print('{} | Absent'.format(self.absent))
        pass
    def cluster(dir):
        box = []
        main = []

            
        for kk in range(len(os.listdir(dir))):
            bc = []
            bc.append(os.listdir(dir)[kk])
            for jj in range(len(os.listdir(dir))):
                if kk != jj:
                    file1 = '{}/{}'.format(dir,os.listdir(dir)[kk])
                    file2 = '{}/{}'.format(dir,os.listdir(dir)[jj])
                    known_image = face_recognition.load_image_file(file1)
                    unknown_image = face_recognition.load_image_file(file2)

                    biden_encoding = face_recognition.face_encodings(known_image)[0]
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                    if results[0] == True:
                    
                        #box[str(kk)]=([os.listdir(dir)[kk]])
                        
                        #box[str(kk)].append(os.listdir(dir)[kk])
                        bc.append(os.listdir(dir)[jj])
                        
            box.append(bc)
            

                
        
        
        new_arr = []
        arr = box
        for i in range(len(arr)):

            for j in range(i+1, len(arr)):

                if set(arr[i]).intersection(set(arr[j])):

                    new_arr.append(list(set(arr[i]).union(set(arr[j]))))
                    
        res = []
        for ic in new_arr:
            ic.sort()
            if ic not in res:
                res.append(ic)
        return res