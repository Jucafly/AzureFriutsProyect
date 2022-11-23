import time
import cv2
import os
import time 
from unittest import result
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from Config import *
from tkinter import *


#Inicamos Captura de WebCAM
cap = cv2.VideoCapture(0)
##Validadores de Azure##
preditionCredentials = ApiKeyCredentials(in_headers={"Prediction-key": preditionKey})
predictor = CustomVisionPredictionClient(endPoint, preditionCredentials)

###################
##---Funciones---##
###################
def AzureConnection (image2Send):
  try:
    with open(image2Send, mode="rb") as test_data:
      results = predictor.detect_image(projectID,publishIterationName,test_data)
  except:
    print("AZURE no Responde")
    time.sleep(2)
    raise SystemExit
   
  for prediction in results.predictions:
    if(prediction.probability * 100 >= 80):
        print("\t" + prediction.tag_name + """": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f},
        bbox.width = {3:.2f}, bbox.height = {4:.2f}""".format(prediction.probability * 100, prediction.bounding_box.left,
        prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))

window = Tk()
window.title("Imagen para Azure")
window.geometry("900x900")


####-----MAIN-----####
while (cap.isOpened()):
  ret,frame = cap.read()
  cv2.imshow('Capture Imagen',frame)
  if(cv2.waitKey(1) == ord('s')):

    imgtempath = 'D:\jucav\Documents\Proyectos\ProyectoIMTC\Img\AzFotos\Azfoto.png'
    time.sleep(3)
    ret, frame = cap.read() 
    cv2.imwrite(imgtempath,frame)
    time.sleep(3)
    
    break

  



AzureConnection(imgtempath)

uimg = 'D:\jucav\Documents\Proyectos\ProyectoIMTC\Img\AzFotos\Azfoto.png'
img = PhotoImage(name="ImagenTest",file=uimg)

label = Label(window,image=img,bd=5,relief=SUNKEN)
label.pack(padx=10,pady=10)

etiqueta = Label(window, text = "Cosas",bg = "blue")
etiqueta.pack(padx=10, pady=10)




window.mainloop()
cap.release()
cv2.destroyAllWindows()



