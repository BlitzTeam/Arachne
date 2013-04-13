import math

class Spider:
	groundHeight = 70.0
	liftHeight = 40.0
	
	def __init__(self, legs):
		#legs = array of Leg
		self.legs = legs
		
	def init(self):
		for l in self.legs:
			for s in l.getMotors():
				s.init()
				
	def getLegs(self):
		return self.legs
	
	def getLeg(self, id):
		return self.legs[id]

	def move(self, angle):
		while True:
			for l in self.legs:
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(angle)

