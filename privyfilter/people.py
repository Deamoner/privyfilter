#pip install thisapidoesnotexist
from thisapidoesnotexist import get_person
import cv2
import numpy as np
import requests
from privyfilter.peoplemod.face_detection import select_face
from privyfilter.peoplemod.face_swap import face_swap

class Holder(object):
    pass

class People(object):
    def getRandomFakeFace():
        person = get_person()
        person.save_image()
        return person

    #swap img1 face onto img2
    def faceSwap(img1, img2):

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
