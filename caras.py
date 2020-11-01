import sys
import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)
clasificador = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

while(True):
    retval, frame = camara.read()

    #& 0xFF filtra el resultado de waitKey de 32 a 8 bits, codigo ASCII.
    if(cv.waitKey(1) == ord('q')):
        camara.release()
        cv.destroyAllWindows()
        sys.exit(0)

    caras = clasificador.detectMultiScale(frame)

    for(x, y, w, h) in caras:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255,255,255), 2)

    cv.imshow('Webcam', frame)