import cv2
import os
from PyQt5.QtWidgets import QMessageBox
# from time import sleep
# from threading import Timer
from datetime import datetime
# request
import requests
# url semilla apiRest
urlApi = 'http://control-personal.test/api/'

class CustomMessageBox(QMessageBox):
    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.timeout = 0
        self.autoclose = False
        self.currentTime = 0

    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        self.currentTime += 1
        if self.currentTime >= self.timeout:
            self.done(0)

    @staticmethod
    def showWithTimeout(timeoutSeconds, message, title, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = CustomMessageBox()
        w.autoclose = True
        w.timeout = timeoutSeconds
        w.setText(message)
        w.setWindowTitle(title)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()

def mainRecognition(dataPath):
    imagePaths = os.listdir(dataPath)
    print('imagePaths=',imagePaths)

    #face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Leyendo el modelo
    #face_recognizer.read('modeloEigenFace.xml')
    #face_recognizer.read('modeloFisherFace.xml')
    face_recognizer.read('modeloLBPHFace.xml')

    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # cap = cv2.VideoCapture('Gaby.mp4')
    cap = cv2.VideoCapture(0)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            '''
            # EigenFaces
            if result[1] < 5700:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
            # FisherFace
            if result[1] < 500:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            '''
            # LBPHFace
            if result[1] < 70:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                
                # send code to api
                # sleep(15)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                form = {
                    'cod_empleado': imagePaths[result[0]],
                    'hora': current_time
                }
                # envios de datos a la ApiRest
                x = requests.post(urlApi+'asistencia-empleado', data = form)
                if x.status_code == 400:
                    CustomMessageBox.showWithTimeout(5, "Error con los tipos de datos, por favor revisa los datos nuevamente.", "Error", icon=QMessageBox.Warning)
                if x.status_code == 500:
                    CustomMessageBox.showWithTimeout(5, "Problemas con el servidor, por favor vuelva a intentarlo mas tarde.", "Error", icon=QMessageBox.Warning)
                if x.status_code == 200:
                    CustomMessageBox.showWithTimeout(4, "Empleado registrado con éxito.", "Bien hecho", icon=QMessageBox.NoIcon)
                if x.status_code == 422:
                    CustomMessageBox.showWithTimeout(4, "Usted ya registro su asistencia.", "Error", icon=QMessageBox.Information)
                if x.status_code == 102:
                    CustomMessageBox.showWithTimeout(5, "El empleado no se encuentra en nuestro sistema.", "Error", icon=QMessageBox.Information)
                if x.status_code == 103:
                    CustomMessageBox.showWithTimeout(5, "No cuenta con ningún horario para registrar en este día.", "Error", icon=QMessageBox.Information)
                if x.status_code == 104:
                    CustomMessageBox.showWithTimeout(5, "Registro fuera de hora.", "Error", icon=QMessageBox.Information)

                # sleep(15)
                # end send
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
        if cv2.getWindowProperty('frame',cv2.WND_PROP_VISIBLE) < 1:    
            break

    cap.release()
    cv2.destroyAllWindows()

# mainRecognition('Data')