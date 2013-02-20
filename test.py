import sys, time
import pydyn
import pydyn.dynamixel as dyn
from Config import *
from Spider import *
from Motion import *
from Servo import *
from LegNames import *

pydyn.enable_vrep()

ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])

legs = configLegs(ctrl.motors, True)

spider = Spider(legs)


sm = ServoMotion(80,1,250)
sm.start()

for i in ctrl.motors:
	i.compliant = False

while(True):
	for m in range(6):
		spider.legs[m].motors[2].setPosition(sm.currentPosition())

