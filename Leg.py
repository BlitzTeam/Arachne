import time
import math
from Config import *
from Motion import *
from constants import *

class Leg:
	groundHeight = 120.0
	liftHeight = 100.0

	def __init__(self, servos, legType = LegType.BACK):
		self.motors = servos
		self.moves = []
		self.legType = legType
		
	def initAtGroundHeight(self):
		self.setPosition(100.0, 0, Leg.groundHeight)

	def getMotors(self):
		return self.motors

	def getMotor(self, id):
		return self.motors[id]
		
	def getAngle(self):
		return (self.motors[0].getAngle(), self.motors[1].getAngle(), self.motors[2].getAngle())

	def setRealAngle(self, a, b, c): # set theorical angles
		realAngles = Leg.computeServoAngles(a,b,c)
		self.setAngle(realAngles[0], realAngles[1], realAngles[2])
		 
	def setAngle(self, angles):
		self.motors[0].setAngle(angles[0])
		self.motors[1].setAngle(angles[1])
		if LegType.FRONT:
			self.motors[2].setAngle(angles[2])

	def setPosition(self, x, y, z):
		angles = self.locationToAngle(x, y, z)
		self.setAngle(angles)

	def locationToAngle(self, x, y, z):
		if (self.legType == LegType.FRONT):
			p = math.sqrt(x**2 + y**2)
			alpha = math.atan2(y, x)
			l = math.sqrt(z**2 + p**2)
			gamma = math.acos((Leg.a**2 + Leg.b**2 - l**2) / (2 * Leg.a * Leg.b))
			beta = math.acos((Leg.a**2 + l**2 - Leg.b**2) / (2 * Leg.a * l))
			return (math.degrees(alpha), math.degrees(beta), math.degrees(gamma))
		
		elif (self.legType == LegType.BACK):
			p = x
			l = math.sqrt(z**2 + p**2)
			o1 = math.acos(z / l)
			gamma = math.acos((Leg.a**2 + Leg.b**2 - l**2) / (2 * Leg.a * Leg.b))
			beta = math.acos((Leg.a**2 + l**2 - Leg.b**2) / (2 * Leg.a * l)) - (math.pi / 2) + o1
			return (math.degrees(beta), math.degrees(gamma))
		
		return ()
		
	def getCurrentMove(self):
		if len(self.moves) > 0:
			return self.moves[0]
		return None
		
	def scheduleMove(self, startPosition, endPosition, time):
		self.moves.append(LegMotion(endPosition, startPosition, time))
	
	def moveToward(self, completionRatio = 0.0, turnAngle = 0.0):		
		if (self.legType == LegType.BACK):
			posA = (120, 0, Leg.groundHeight)
			posB = (50, 0, Leg.groundHeight)
			posC = (90, 0, Leg.liftHeight)
			self.scheduleMove(posA, posB, Leg.pullTime)
			self.scheduleMove(posB, posC, Leg.liftTime)
			self.scheduleMove(posC, posA, Leg.forwardTime)
		elif (self.legType == LegType.FRONT):
			posA = (0, 50, 100)
			posB = (100, 50, 100)
			posC = (100, 50, 50)
			self.scheduleMove(posA, posB, Leg.pullTime)
			self.scheduleMove(posB, posC, Leg.liftTime)
			self.scheduleMove(posC, posA, Leg.forwardTime)
			
	@staticmethod
	def computeXY(alpha, p):
		f = math.tan(math.radians(alpha))
		x = math.sqrt(p**2 / (1 + f**2))
		x = -x if abs(alpha) > 90 else x
		y = x * f
		return (x, y)
		
	@staticmethod
	def computeServoAngles(alpha, beta, gamma): #compute the real values given to the servos
		return (alpha, beta, gamma)
	
	def move(self, dt = 0.0): # move the leg according to the current self.move[0], does nothing if len(self.move) == 0
		if len(self.moves) != 0:
			currentMove = self.moves[0]
			if currentMove.isDone():
				self.moves.pop(0)
				if len(self.moves) != 0:
					currentMove = self.moves[0]
					currentMove.start()
					print("New Move")
					
			currentValues = currentMove.currentValues(dt)
			self.setPosition(currentValues[0], currentValues[1], currentValues[2])
		
	def hasScheduledMove(self):
		return len(self.moves) != 0
	
	def clearScheduledMoves(self):
		self.moves = []

