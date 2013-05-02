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
			print(l.orientation, l.preferredDirection, l.getRelativeDirection(i))
			l.setRealAngle(l.getRelativeDirection(i)[0], 0, 0)
		raw_input()
		
def testLeg():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20], timeout = 0.1)
	legs = configLegs(ctrl.motors)
	for m in ctrl.motors:
		m.compliant = False
		m.position = 150
		m.max_torque = 100
		
		
	#ctrl.motors[14].position = 200
	legs[4].setRealAngle(90,0,0)
	time.sleep(1.0)	
	
def testRotate():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20], timeout =  0.1)
	for m in ctrl.motors:
		m.max_torque = 100
		m.moving_speed = 100
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.rotate(gait=Gait.Tripod, angle = 180.0)
	
def testMove():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20], timeout =  0.1)
	for m in ctrl.motors:
		m.max_torque = 100
		m.moving_speed = 100
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.move(gait=Gait.Tripod, distance = 100.0)
	#spider.rotate(gait=Gait.Tripod, angle = 90.0)
	#spider.move(gait=Gait.Tripod, distance = 100.0)


def testLegWalk():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	leg = legs[0]
	while(True):
		if not leg.hasScheduledMove():
			leg.moveToward(90.0, turnAngle = 0.0)
		leg.move()

def testGoto():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	for m in ctrl.motors:
		m.max_torque = 50.0
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.init()
	time.sleep(1.0)
	spider.goto(100, 0, mode = MoveMode.Basic)		

def testInit():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.init()
	time.sleep(1.0)
	
def testWalk():
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20], timeout =  0.1)
	for m in ctrl.motors:
		m.max_torque = 100
		m.moving_speed = 100
	legs = configLegs(ctrl.motors, simulator = False)
	spider = Spider(legs)
	spider.move(0.0, turnAngle = 0.0)

if __name__ == '__main__':
	#testLeg()
	#testRelativeDirection()
	#testWalk()
	testMove()
	#testGoto()
	#testLegWalk()
	#testInit()
