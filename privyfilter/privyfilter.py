"""
Privy module
Privacy filter for photos for detecting faces and private information and scrubbing it.

To do:

"""

import numpy as np
import cv2
from PIL import Image
import os.path
from .people import People

mydir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(mydir, "Configs", "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(config_path)

class Privyfilter(object):
    """
    Common methods for processing the photos.
    """

    #Method for object creation - loading all the image processing libraries
    def __init__(self):
        faces = []
        self = self

    #Method for loading the models and libraries for the object
    @staticmethod
    def faceScrub(imgPath):
        #filetest = os.path.isfile(imgPath)
        #if image no good throw error

        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        anonyimage = Privyfilter.find_and_blur(gray, img)
        return faces, anonyimage


    #Method for annoymizing the faces
    @staticmethod
    def anonymize_face(image, blocks=6):
        (h, w) = image.shape[:2]
        xSteps = np.linspace(0, w, blocks + 1, dtype='int')
        ySteps = np.linspace(0, h, blocks + 1, dtype='int')
        for i in range(1, len(ySteps)):
            for j in range(1, len(xSteps)):
                startX = xSteps[j - 1]
                startY = ySteps[i - 1]
                endX = xSteps[j]
                endY = ySteps[i]
                roi = image[startY: endY, startX:endX]
                (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
                cv2.rectangle(image, (startX, startY), (endX, endY), (B, G, R), -1)
        return image
    #Private Method for annoymizing the faces
    def find_and_blur(bw, color):
        face_cascade = cv2.CascadeClassifier(config_path)
        faces = face_cascade.detectMultiScale(bw, 1.1, 4)
        for (x, y, w, h) in faces:
            color[y:y+h, x:x+w] = Privyfilter.anonymize_face(color[y:y+h, x:x+w])
        return color

    #RemoveMetaData(imgPath)
    def RemoveMetaData(imgPath):
        image = Image.open(imgPath)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        return image_without_exif

    def getFakeFace():
        return People.getRandomFakeFace()

    def swapFaces(imgPath1, imgPath2):
        #TODO: Will need to be udpated to use in a pipeline instead of with file paths - this can be simple demo test implemtnation
        img1 = cv2.imread(imgPath1)
        img2 = cv2.imread(imgPath2)
        finalPhoto = People.faceSwap(img1, img2)
        return finalPhoto