import math

class Spider:
	
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
	
	def initStartPosition(self):
		for l in self.legs:
			l.initStartPosition()

	def goToStartPosition(self):
		for l in self.legs:
			l.goToStartPosition()

	def makeCompliant(self, compliant = True):
		for l in self.legs:
			l.makeCompliant(compliant)

	def move(self, angle, distance):
		distanceWalked = 0
		while(distance > distanceWalked):
			for leg in self.legs:
				leg.moveToward(angle)
		
	def rotate(self, angle):
		pass
		
		

