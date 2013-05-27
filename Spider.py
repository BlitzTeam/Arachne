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

		for i in range(len(self.legs)):
			self.legs[i].moveToward()

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
			
			currentTime = 0
			while self.moving:
				print(time.time() - currentTime)
				currentTime = time.time()
				time.sleep(0.5)
				for l in self.legs:
					if not l.hasScheduledMove():
						l.moveToward(0, turnAngle = self.turnAngle)
					l.move()

