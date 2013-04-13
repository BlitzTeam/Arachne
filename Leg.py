import numpy
import sys, time
import pydyn.dynamixel as dyn
import math
import pydyn
from Config import *
from Spider import *
from Motion import *

class Leg:
	a1 = 49
	a2 = -14
	b = 50
	c = 70
	
	alpha0 = 150
	beta0 = 175
	gamma0 = 90

	def __init__(self, orientation, x , y , servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x # top down view
		self.y = y # top down view
		self.motors = (servo_up, servo_middle, servo_down)
		self.moves = []

	def getMotors(self):
		return self.motors

	def getMotor(self, id):
		return self.motors[id]
		
	def getAngle(self):
		return (self.motors[0].getAngle(), self.motors[1].getAngle(), self.motors[2].getAngle())

	def setAngle(self, a, b, c):
		self.motors[0].setAngle(a)
		self.motors[1].setAngle(b)
		self.motors[2].setAngle(c)
				
	def angleToPosition(self, alpha, beta, gamma, relative = True):
		if relative == True:
			return (numpy.cos(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								numpy.sin(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								Leg.a2 + Leg.b * numpy.sin(beta) +  Leg.c * numpy.cos(beta + gamma))
		else:
			rel = self.angleToPosition(alpha, beta, gamma, True)
		return() # TODO: Implementation

	def setPosition(self, x, y, z):
		angles = Leg.locationToAngle(x, y, z, Leg.b, Leg.c)
		print(angles)
		self.setAngle(angles[0], angles[1], angles[2])

	@staticmethod            	
	def locationToAngle(x, y, z, a, b):
		alpha = 150 + (90 - math.degrees(math.atan2(x, y)))
	
		p = math.sqrt(x**2 + y**2)
		l = math.sqrt(p**2 + z**2)
		if (l > a + b):
			print("Warning: You requested an impossible location for a leg")
			return None

		gamma = math.degrees(math.acos((-l**2 + a**2 + b**2) / (2 * a * b)))

		o3 = math.degrees(math.acos(z/l))
		o4 = math.degrees(math.acos((-b**2 + a**2 + l**2) / (2 * a * l)))
		beta = 90 - (o3 + o4)	

		return (alpha, beta + 150, 180 - gamma + 60)
		
	def moveToward(self, direction):
		relativeDirection = self.orientation - direction
		reversedDirection = False
		if (relativeDirection > 90 or relativeDirection < -90): #if impossible direction for alpha, reverse it
			reversedDirection = True
			relativeDirection = relativeDirection + 180.0
		
		z = Spider.groundHeight
		maxGamma = 160
		minGamma = 40
		alpha = relativeDirection
		
		#self.moves.append(LegMotion(self.getAngle(), (alpha, beta, gamma))) # Schedule the lifting motion
		
		gamma = minGamma if reversedDirection else maxGamma
		beta = Leg.computeBeta(alpha, gamma, z)
		newValues = Leg.computeServoAngles(alpha, beta, gamma)
		print(self.getAngle())
		self.moves.append(LegMotion(self.getAngle(), newValues)) # Schedule the forward motion

		gamma = maxGamma if reversedDirection else minGamma		
		beta = Leg.computeBeta(alpha, gamma, z)
		self.moves.append(LegMotion(newValues, Leg.computeServoAngles(alpha, beta, gamma))) # Schedule the backward motion
		
	@staticmethod
	def computeBeta(alpha, gamma, z): #compute the beta angle according to alpha, gamma and z. This function works with theorical values
		l = math.sqrt(Leg.b**2 + Leg.c**2 - 2 * Leg.b * Leg.c * math.cos(gamma))
		print(l, z)
		p = math.sqrt(l**2 - z**2)
		o3 = math.degrees(math.acos((z**2 + l**2 - p**2) / (2 * z * l)))
		o4 = math.degrees(math.acos((Leg.b**2 + l**2 - Leg.c**2) / (2 * Leg.b * l)))
		return 90 - (o3 + o4)
		
	@staticmethod
	def computeServoAngles(alpha, beta, gamma): #compute the real values given to the servos
		return (alpha + 150, beta + 150, 180 - gamma + 60)
	
	def move(self): # move the leg according to the current self.move[0], does nothing if len(self.move) == 0
		if len(self.moves) != 0:
			currentMove = self.moves[0]
			if currentMove.isDone():
				self.moves.pop(0)
				print("Move done")
				if len(self.moves) != 0:
					currentMove = self.moves[0]
					currentMove.start()
					print("New move loaded")
					
			currentValues = currentMove.currentValues()
			self.setAngle(currentValues[0], currentValues[1], currentValues[2])
		
	def hasScheduledMove(self):
		return len(self.moves) != 0
		
if __name__ == '__main__':
	pydyn.enable_vrep()
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	ctrl.start_sim()
	
	l = configLegs(ctrl.motors)
	s = Spider(l)
	s.init()
	leg = s.getLeg(1)
	m = leg.getMotor(2)
	m.servo_ctrl.position = 230
	time.sleep(2.0)
	print (m.servo_ctrl.position)
