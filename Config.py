from Leg import *
from Servo import *
import math

def configLegs(motors, simulator = True):
	if simulator:
		Leg.a = 50.0
		Leg.b = 70.0
		Leg.c = 0.0
		return (	Leg(0.0, 0, 0, Servo(motors[0], offset = 30), Servo(motors[1]), Servo(motors[2], offset = 90)), 
					Leg(90.0, 0, 0, Servo(motors[15]), Servo(motors[16]), Servo(motors[17], offset = 90)), 
					Leg(180.0, 0, 0, Servo(motors[12], offset = -30), Servo(motors[13]), Servo(motors[14], offset = 90)), 
					Leg(180.0, 0, 0, Servo(motors[9], offset = 30), Servo(motors[10]), Servo(motors[11], offset = 90)),
					Leg(270.0, 0, 0, Servo(motors[6]), Servo(motors[7]), Servo(motors[8], offset = 90)),
					Leg(0.0, 0, 0, Servo(motors[3], offset = -30), Servo(motors[4]), Servo(motors[5], offset = 90)))
	
	Leg.a = 60
	Leg.b = 93
	Leg.c = 24
	
	return (		Leg(0.0, 2.6, 3.3, Servo(motors[12]), Servo(motors[1]), Servo(motors[17])), 
					Leg(90.0, 4.2, 0, Servo(motors[5], offset = 40), Servo(motors[4]), Servo(motors[0])), 
					Leg(180.0, 2.6, -3.3, Servo(motors[16]), Servo(motors[2]), Servo(motors[13])), 
					Leg(180.0, -2.8, -3.3, Servo(motors[7]), Servo(motors[6]), Servo(motors[8])),
					Leg(270.0, -4.3, 0, Servo(motors[14]), Servo(motors[10]), Servo(motors[11])),
					Leg(0.0, -2.8, 3.3, Servo(motors[9]), Servo(motors[3]), Servo(motors[15])))

