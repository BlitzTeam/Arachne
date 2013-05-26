import math
import thread
from Config import *
import time
from constants import *

class Spider:
	walkSpeed = 100.0 / 8.07
	rotationSpeed = 180.0 / 10.54

	def __init__(self, legs):
		self.legs = legs
		self.currentDirection = 0.0
		self.moving = False
		self.turnAngle = 0.0
		
	def init(self):
		for l in self.legs:
			l.initAtGroundHeight()
				
	def getLegs(self):
		return self.legs
	
	def getLeg(self, id):
		return self.legs[id]
		
	def initLegsPosition(self, angle, turnAngle = 0.0, incremental = False):
		for l in self.legs:
			l.clearScheduledMoves()

		Leg.liftTime = 5.0
		Leg.forwardTime = 5.0
		Leg.pullTime = 10.0
		for i in range(len(self.legs)):
			self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 2 == 0 else 0.5, turnAngle=turnAngle)

		for l in self.legs:
			l.move()
		time.sleep(0.5)
		for l in self.legs:
			l.getCurrentMove().start()

	def move(self, startNow = True, turnAngle = 0.0):
			
			self.turnAngle = turnAngle						
			if startNow:
				self.moving = True
			
			while not self.moving:
				time.sleep(0.1)
			
			self.initLegsPosition(self.currentDirection, turnAngle = self.turnAngle)
			
			while self.moving:
				for l in self.legs:
					if not l.hasScheduledMove():
						l.moveToward(0, turnAngle = self.turnAngle)
					l.move()

