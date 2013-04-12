import math

class Spider:
	groundHeight = -60.0
	
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
			for i in range(1, 6, 2):
				self.legs[i].moveToward(angle)
			#wait for move completion
			for i in range(0, 6, 2):
				self.legs[i].moveToward(angle)
			#wait for move completion



