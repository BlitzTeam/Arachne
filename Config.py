from Leg import *
from Servo import *

def configLegs(motors, simulator = True):
	if simulator:
		return (	Leg(Servo(motors[0]), Servo(motors[1]), Servo(motors[2])), 
					Leg(Servo(motors[15]), Servo(motors[16]), Servo(motors[17])), 
					Leg(Servo(motors[12]), Servo(motors[13]), Servo(motors[14])), 
					Leg(Servo(motors[9]), Servo(motors[10]), Servo(motors[11])),
					Leg(Servo(motors[6]), Servo(motors[7]), Servo(motors[8])),
					Leg(Servo(motors[3]), Servo(motors[4]), Servo(motors[5])))
	
	return configLegs(motors, True)