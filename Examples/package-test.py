from privyfilter.privyfilter import Privyfilter as pf

faces, imger = pf.faceScrub("../TestPics/10.jpg")
print(faces)
img = pf.RemoveMetaData("../TestPics/10.jpg")
print(img)

#Synthetic face replacement ( Simple Deepfake)
#get random sythetic face
fakeface = pf.getFakeFace()
fakeface.save_image("fakeface.jpg")
faces, imger = pf.faceScrub("fakeface.jpg")
print(faces)
#Swap faces
faceswap = pf.swapFaces("fakeface.jpg", "../TestPics/9.jpg")
print(fakeface)
quit()