from Leg import *
from Servo import *
import math

def configLegs(motors, simulator = True):
	if simulator:
		return (	Leg(math.pi / 6, 0, 0, Servo(motors[0]), Servo(motors[1]), Servo(motors[2])), 
					Leg(3 * math.pi / 6, 0, 0, Servo(motors[15]), Servo(motors[16]), Servo(motors[17])), 
					Leg(5 * math.pi / 6, 0, 0, Servo(motors[12]), Servo(motors[13]), Servo(motors[14])), 
					Leg(7 * math.pi / 6, 0, 0, Servo(motors[9]), Servo(motors[10]), Servo(motors[11])),
					Leg(9 * math.pi / 6, 0, 0, Servo(motors[6]), Servo(motors[7]), Servo(motors[8])),
					Leg(11 * math.pi / 6, 0, 0, Servo(motors[3]), Servo(motors[4]), Servo(motors[5])))
	
	return configLegs(motors, True) #TODO: Implement this case

