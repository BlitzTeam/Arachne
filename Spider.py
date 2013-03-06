import math

class Spider:
	def __init__(self, legs):
		"legs = array of Leg"
		self.legs = legs
		
	def move(self, angle, distance):
		distanceWalked = 0
		while(distance > distanceWalked):
			for leg in self.legs:
				leg.moveToward(angle)
		
	def rotate(self, angle):
		pass
		

