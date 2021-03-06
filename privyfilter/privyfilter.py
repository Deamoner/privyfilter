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
        #TODO: Change if to have option of sending cv2 object
        #filetest = os.path.isfile(imgPath)
        #if image no good throw error
        if os.path.isfile(imgPath) != True:
            #no file present
            if isinstance(imgPath, cv2):
                img = imgPath
            else:
                exit("No file or cv2 Object Present.")
        else:
            img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        anonyimage = Privyfilter.find_and_blur(gray, img)
        return faces, anonyimage

    # Method for return face box coordinates boxes
    @staticmethod
    def findFaces(imgPath):
        if os.path.isfile(imgPath1) != True:
            #no file present
            if isinstance(imgPath, cv2):
                img = imgPath
            else:
                exit("No file or cv2 Object Present.")
        else:
            img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        return faces

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
    @staticmethod
    def find_and_blur(bw, color):
        face_cascade = cv2.CascadeClassifier(config_path)
        faces = face_cascade.detectMultiScale(bw, 1.1, 4)
        for (x, y, w, h) in faces:
            color[y:y+h, x:x+w] = Privyfilter.anonymize_face(color[y:y+h, x:x+w])
        return color

    #RemoveMetaData(imgPath)
    @staticmethod
    def RemoveMetaData(imgPath):
        #error checking
        if os.path.isfile(imgPath) != True:
            exit("File does not exist.")
        image = Image.open(imgPath)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        return image_without_exif

    @staticmethod
    def getFakeFace():
        return People.getRandomFakeFace()

    #swap faces between only two iamges
    @staticmethod
    def swapFaces(imgPath1, imgPath2):

        if os.path.isfile(imgPath1) != True:
            #no file present
            if isinstance(imgPath1, cv2):
                img1 = imgPath1
            else:
                exit("No file or cv2 Object Present.")
        else:
            img1 = cv2.imread(imgPath1)
        if os.path.isfile(imgPath2) != True:
            # no file present
            if isinstance(imgPath2, cv2):
                img2 = imgPath2
            else:
                exit("No file or cv2 Object Present.")
        else:
            img2 = cv2.imread(imgPath2)
        finalPhoto = People.faceSwap(img1, img2)
        return finalPhoto

    #function to utilize
    @staticmethod
    def replaceFacesFake(self, imgPath1):
        #TODO: findallfaces, genfakefaces, segment faces, swapFace, return phot
        #find all faces and segmetn
        faces = self.findFaces(imgPath1)
        print(faces)
        return 1

