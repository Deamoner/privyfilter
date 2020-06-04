from privyfilter.privyfilter import Privyfilter as pf

faces, img = pf.faceScrub("../TestPics/1Person-Close.jpg")
print(faces)
