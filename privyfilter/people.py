#pip install thisapidoesnotexist
from thisapidoesnotexist import get_person
from deepface import DeepFace
import cv2
import numpy as np
import requests
from privyfilter.peoplemod.face_detection import select_face
from privyfilter.peoplemod.face_swap import face_swap

class Holder(object):
    pass

class People(object):
    @staticmethod
    def findFacesDetail(img1, demographics = False):
        #TODO: Compartmentalize the faces functions into the people object
        if os.path.isfile(img1) != True:
            exit("File does not exist.")
        ##TODO: find faces
        src_points, src_shape, src_face = select_face(img1)
        demography = People.getDemographics(dst[0])
        return src_points, src_shape, src_face, demography

    def getDemographics(img1, actions = ['age','gender', 'race']):
        # TODO: process the cv2 objects - save to temp file I guess?
        #Error checking:
        if os.path.isfile(img1) != True:
            exit("File does not exist.")
        demography = DeepFace.analyze(dst[0], actions)
        return demography

    @staticmethod
    def getRandomFakeFace():
        #TODO: return cv2 object instead of saving
        person = get_person()
        person.save_image()
        return person

    #swap img1 face onto img2
    @staticmethod
    def faceSwap(img1, img2):
        # TODO: Compartmentalize the faces functions into the people object
        #assume both cv2 images are passed to us
        src_points, src_shape, src_face = select_face(img1)
        dst_points, dst_shape, dst_face = select_face(img2)
        # sets some args
        args = Holder()
        args.correct_color = True
        args.warp_2d = False
        #cv2 object return
        output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, img2, args)
        return output

