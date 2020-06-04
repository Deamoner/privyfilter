#from "../src/privy" import Privy
import sys
sys.path.append('../src/')
from privyfilter.privyfilter import Privyfilter as pf

faces2, img = pf.processFile("../TestPics/1Person-Close.jpg")
print(faces2)
print(img)
