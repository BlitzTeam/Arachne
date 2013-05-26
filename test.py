import math
import thread
from Config import *
import time
from constants import *
from Spider import *
from Connexion import *

def testWalk():
	legs = configLegs(connexion = Connexion())
	spider = Spider(legs)
	spider.move()

if __name__ == '__main__':
	testWalk()

