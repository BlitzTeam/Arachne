from Leg import *
from Servo import *
from constants import *
import math
from Connexion import *

def configLegs(connexion = Connexion()):
	Leg.a = 72
	Leg.b = 100
	Leg.a1 = 0
	Leg.a2 = 0
	Leg.ab0 = 0
	Leg.ab1 = 0
	Leg.ab2 = 0
	
	Leg.liftTime = 5.0
	Leg.forwardTime = 5.0
	Leg.pullTime = 5.0
	
	#define SERVO_BR1 0
	#define SERVO_BR2 1
	#define SERVO_BL1 2
	#define SERVO_BL2 3
	#define SERVO_FM1 4
	#define SERVO_FR1 5
	#define SERVO_FR2 6
	#define SERVO_FR3 7
	#define SERVO_FR4 8
	#define SERVO_FL1 9
	#define SERVO_FL2 10
	#define SERVO_FL3 11
	
	BR1 = 0
	BR2 = 1
	BL1 = 2
	BL2 = 3
	FM1 = 4
	FR1 = 5
	FR2 = 6
	FR3 = 7
	FR4 = 8
	FL1 = 9
	FL2 = 10
	FL3 = 11
	
	
	return 	(	
				Leg((Servo(connexion, BR1, offset=90), Servo(connexion, BR2, offset=-90)), LegType.BACK),
				Leg((Servo(connexion, BL1, offset=90), Servo(connexion, BL2)), LegType.BACK)
			)
	"""
	return 	(	
				Leg((Servo(connexion, 9), Servo(connexion, 10), Servo(connexion, 16)), LegType.FRONT), #FRONT LEFT LEG
				Leg((Servo(connexion, 27), Servo(connexion, 26), Servo(connexion, 25)), LegType.FRONT), #FRONT RIGHT LEG
				Leg((Servo(connexion, 5), Servo(connexion, 8)), LegType.BACK), #BACK RIGHT LEG
				Leg((Servo(connexion, 11), Servo(connexion, 3)), LegType.BACK) #BACK LEFT LEG
			)
			
	"""
