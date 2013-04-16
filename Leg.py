import numpy
import sys, time
import pydyn.dynamixel as dyn
import math
import pydyn
from Config import *
from Spider import *
from Motion import *
from constants import *

class Leg:
	#a1 = 49
	#a2 = -14
	b = 50
	c = 70
	
	liftTime = 0.5
	forwardTime = 0.5
	pullTime = 2.0

	def __init__(self, orientation, x , y , servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x # top down view
		self.y = y # top down view
		self.motors = (servo_up, servo_middle, servo_down)
		self.moves = []
		
	def initAtGroundHeight(self):
		self.setPosition(50.0, 0, Spider.groundHeight)

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

	"""				
	def angleToPosition(self, alpha, beta, gamma, relative = True):
		if relative == True:
			return (numpy.cos(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								numpy.sin(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								Leg.a2 + Leg.b * numpy.sin(beta) +  Leg.c * numpy.cos(beta + gamma))
		else:
			rel = self.angleToPosition(alpha, beta, gamma, True)
		return() # TODO: Implementation
	"""

	def setPosition(self, x, y, z):
		angles = Leg.locationToAngle(x, y, z, Leg.b, Leg.c)
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
		
	def getCurrentMove(self):
		if len(self.moves) > 0:
			return self.moves[0]
		return None
		
	def moveToward(self, direction, completionRatio = 0.0):
		relativeDirection = self.orientation - direction
		relativeDirection = (relativeDirection + 180) % 360 - 180 # direction between -180 and +180 degrees
		reversedDirection = False
				
		if relativeDirection > 90 or (relativeDirection == 90 and self.motors[0].offset > 0):
			reversedDirection = True
			relativeDirection = relativeDirection - 180.0
		elif relativeDirection < -90 or (relativeDirection == -90.0 and self.motors[0].offset < 0):
			reversedDirection = True
			relativeDirection = relativeDirection + 180.0
		
		totalTime = Leg.liftTime + Leg.forwardTime + Leg.pullTime
		currentTime = completionRatio * totalTime
		
		maxGamma = 160.0
		minGamma = 70.0
		aveGamma = minGamma + (maxGamma - minGamma) * 0.5
		alpha = relativeDirection
		
		gamma = maxGamma if reversedDirection else minGamma
		oldValues = Leg.computeServoAngles(alpha, Leg.computeBeta(alpha, gamma, Spider.groundHeight), gamma) # cannot read current position because of vrep
		
		gamma = aveGamma
		beta = Leg.computeBeta(alpha, gamma, Spider.liftHeight)
		newValues = Leg.computeServoAngles(alpha, beta, gamma)
		oldValues = LegMotion.extrapolateBatch(oldValues, newValues, currentTime, Leg.liftTime)
		if currentTime < Leg.liftTime:
			self.moves.append(LegMotion(oldValues, newValues, Leg.liftTime - currentTime)) # Schedule the lifting motion
			currentTime = 0.0
		else:
			currentTime -= Leg.liftTime
		
		gamma = minGamma if reversedDirection else maxGamma
		beta = Leg.computeBeta(alpha, gamma, Spider.groundHeight)
		oldValues = newValues
		newValues = Leg.computeServoAngles(alpha, beta, gamma)
		oldValues = LegMotion.extrapolateBatch(oldValues, newValues, currentTime, Leg.forwardTime)
		if currentTime < Leg.forwardTime:
			self.moves.append(LegMotion(oldValues, newValues, Leg.forwardTime - currentTime)) # Schedule the forward motion
			currentTime = 0.0
		else:
			currentTime -= Leg.forwardTime

		gamma = maxGamma if reversedDirection else minGamma		
		beta = Leg.computeBeta(alpha, gamma, Spider.groundHeight)
		oldValues = newValues
		newValues = Leg.computeServoAngles(alpha, beta, gamma)
		oldValues = LegMotion.extrapolateBatch(oldValues, newValues, currentTime, Leg.pullTime)
		if currentTime < Leg.pullTime:
			self.moves.append(LegMotion(oldValues, newValues, Leg.pullTime - currentTime)) # Schedule the backward motion

	@staticmethod
	def computeBeta(alpha, gamma, z): #compute the beta angle according to alpha, gamma and z. This function works with theorical values
		l = math.sqrt(Leg.b**2 + Leg.c**2 - 2 * Leg.b * Leg.c * math.cos(math.radians(gamma)))		
		o3 = math.degrees(math.acos(z / l))
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
				if len(self.moves) != 0:
					currentMove = self.moves[0]
					currentMove.start()
					
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
	time.sleep(1.0)
	leg = s.getLeg(4)

	leg.moveToward(-30.0)

	while leg.hasScheduledMove():
		leg.move()
