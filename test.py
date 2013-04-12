import sys, time
import pydyn
import pydyn.dynamixel as dyn
#from Config import *
#from Spider import *
#from Motion import *
#from Servo import *
#from LegNames import *

pydyn.enable_vrep()

ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
ctrl.start_sim()

#legs = configLegs(ctrl.motors, True)

#spider = Spider(legs)

#l = configLegs(ctrl.motors);
#s = Spider(l)
#print("position " ,s.getLeg(1).getPosition())

for m in ctrl.motors:
	m.compliant = False
	print m.present_position_raw
	m.position = 125


#s.getLeg(1).goToAngle(100,100,100)
#print("appuyez apres le mouvement pour avoir la position . . .")
raw_input()

for m in ctrl.motors:
	m.compliant = False
	print m.present_position_raw
	m.position = 110

raw_input()

for m in ctrl.motors:
	m.compliant = False
	print m.present_position
	m.position = 150

raw_input()

#print("position " ,s.getLeg(1).getPosition())
for m in ctrl.motors:
	print m.position_raw

