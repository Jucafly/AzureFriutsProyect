import time
from unittest import result
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from Config import *


imgSource = "D:/jucav/Documents/Proyectos/ProyectoIMTC/Img/DataSets/17.jpg"

##Validadores de Azure##
preditionCredentials = ApiKeyCredentials(in_headers={"Prediction-key": preditionKey})
predictor = CustomVisionPredictionClient(endPoint, preditionCredentials)

##Try Predictio##
try:
  with open(imgSource, mode="rb") as test_data:
        results = predictor.detect_image(projectID,publishIterationName,test_data)
except:
  print("AZURE no Responde")
  time.sleep(2)
  raise SystemExit
  
##Imprimir Prediccion 
for prediction in results.predictions:
  if(prediction.probability * 100 >= 40):
      print("\t" + prediction.tag_name + """": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f},
      bbox.width = {3:.2f}, bbox.height = {4:.2f}""".format(prediction.probability * 100, prediction.bounding_box.left,
      prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))

