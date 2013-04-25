import math
import pydyn.dynamixel as dyn
import pydyn
import thread
from Config import *
import time
from constants import *
from Spider import *

def testRelativeDirection():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	for i in range(-180, 180, 90):
		print('Angle ' + str(i)) 
		for l in legs:
			print(l.orientation, l.preferredDirection, l.getRelativeDirection2(i))
			l.setRealAngle(l.getRelativeDirection2(i)[0], 0, 0)
		raw_input()
		
def testLeg():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	legs[4].setRealAngle(100,0,0)
	time.sleep(1.0)	
	
	
def testWalk():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.move(10, turnAngle = 10.0)	

def testLegWalk():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	leg = legs[4]
	while(True):
		if not leg.hasScheduledMove():
			leg.moveToward(0.0, turnAngle = 10.0)
		leg.move()
		

def testInit():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.init()
	time.sleep(1.0)

if __name__ == '__main__':
	testLeg()
	#testRelativeDirection()
	#testWalk()
	#testLegWalk()
	#testInit()
