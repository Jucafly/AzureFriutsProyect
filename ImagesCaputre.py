import cv2
import os
import time 

#Damos los Data Paths
dataPath = "D:\jucav\Documents\Proyectos\ProyectoIMTC\Img"
fotosPath = dataPath + '\Captures'
cicles = 0

#Comprobacion de Carpeta
if not os.path.exists(fotosPath):
    print("Creando Carpeta en ",fotosPath)
    os.makedirs(fotosPath)
else:
    print("Si existe la carpeta")

#Inicamos Captura de WebCAM
cap = cv2.VideoCapture(0)
##
while (cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('Imagen',frame)

    if(cv2.waitKey(1) == ord('f')):
        while cicles < 10:
            imgtempath = 'D:\jucav\Documents\Proyectos\ProyectoIMTC\Img\Captures\imgs {}.jpg'.format(cicles)
            print(imgtempath)
            time.sleep(1)
            ret, frame = cap.read()
            cv2.imwrite(imgtempath,frame)
            cicles = cicles+1    
    
    if(cv2.waitKey(1) == ord('s')):
        print("SALIMOS")
        break 
    

cap.release()
cv2.destroyAllWindows()








    



