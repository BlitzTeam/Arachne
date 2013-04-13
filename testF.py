import sys, time
import pydyn
import pydyn.dynamixel as dyn
from Config import *
from Spider import *
from Motion import *
from Servo import *
from LegNames import *

#pydyn.enable_vrep()

ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])

legs = configLegs(ctrl.motors, True)

spider = Spider(legs)

#for i in ctrl.motors:
#	i.compliant = False

while(True):
	m = 0
	#pattes avant
	#Elles se levent		
	spider.legs[0].motors[1].setPosition(90)
	spider.legs[3].motors[1].setPosition(90)
	time.sleep(0.5)
	#tourne vers l'avant
	spider.legs[0].motors[0].setPosition(90)
	spider.legs[3].motors[0].setPosition(180)
	time.sleep(0.5)
	#redescendent jusqu'au sol
	spider.legs[0].motors[1].setPosition(180)
	spider.legs[3].motors[1].setPosition(180)
	time.sleep(0.5)
	#tourne vers l'arriere
	spider.legs[0].motors[0].setPosition(180)
	spider.legs[3].motors[0].setPosition(90)
	time.sleep(0.5)
	"""
	for m in (0,1):
		#pattes avant
		#Elles se levent		
		spider.legs[m].motors[1].setPosition(180)
		#tourne vers l'avant
		spider.legs[m].motors[1].setPosition(sm2.currentPosition())
		#redescendent jusqu'au sol
		spider.legs[m].motors[1].setPosition(sm2.currentPosition())
		#tourne vers l'arriere
		spider.legs[m].motors[1].setPosition(sm2.currentPosition())	
		
		#pattes milieu
		#se levent
		#tourne vers l'avant
		#descendent
		#tourne vers l'arriere
	
	
		spider.legs[m].motors[1].setPosition(sm2.currentPosition())
		spider.legs[m].motors[2].setPosition(sm.currentPosition())
		if m in (1,4):
			spider.legs[m].motors[0].setPosition(sm0.currentPosition())
	"""
		
