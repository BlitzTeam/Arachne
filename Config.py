from Leg import *
from Servo import *
import math

def configLegs(motors, simulator = False):
	Leg.a = 60
	Leg.b = 93
	Leg.c = 24
	
	return (		Leg(0.0, 2.6, 3.3, Servo(motors[6]), Servo(motors[8]), Servo(motors[10]), preferredDirection = "right"), 
					Leg(90.0, 4.2, 0, Servo(motors[0]), Servo(motors[2]), Servo(motors[4])), 
					Leg(180.0, -2.8, -3.3, Servo(motors[13]), Servo(motors[15]), Servo(motors[17]), preferredDirection = "right"),
					Leg(270.0, -4.3, 0, Servo(motors[7]), Servo(motors[9]), Servo(motors[11])),

