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
	
def testServo():
	legs = configLegs(connexion = Connexion())
	leg = legs[0]
	leg.setPosition(0,0,100)
	leg.setPosition(120,0,120)

def testLeg():
	legs = configLegs(connexion = Connexion())
	leg = legs[0]
	while(True):
		if (not leg.hasScheduledMove()):
			leg.moveToward()
		leg.move()		
		
if __name__ == '__main__':
	#testWalk()
	#testServo()
	testLeg()
