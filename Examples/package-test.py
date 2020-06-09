from privyfilter.privyfilter import Privyfilter as pf

faces, imger = pf.faceScrub("../TestPics/1Person-Close.jpg")
print(faces)
img = pf.RemoveMetaData("../TestPics/1Person-Close.jpg")
print(img)
quit()