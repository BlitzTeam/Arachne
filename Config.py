from Leg import *
from Servo import *
from constants import *
import math

def configLegs(connexion):
	Leg.a = 72
	Leg.b = 100
	Leg.a1 = 0
	Leg.a2 = 0
	Leg.ab0 = 0
	Leg.ab1 = 0
	Leg.ab2 = 0
	
	motors = []
	
	return 	(	
				Leg((Servo(connexion, 0), Servo(connexion, 0), Servo(connexion, 0)), LegType.FRONT), 
				Leg((Servo(connexion, 0), Servo(connexion, 0), Servo(connexion, 0)), LegType.FRONT), 
				Leg((Servo(connexion, 0), Servo(connexion, 0), Servo(connexion, 0)), LegType.BACK),
				Leg((Servo(connexion, 0), Servo(connexion, 0), Servo(connexion, 0)), LegType.BACK)
			)
