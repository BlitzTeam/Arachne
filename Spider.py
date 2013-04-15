import math
import pydyn.dynamixel as dyn
import pydyn
from Config import *
import time

class Spider:
	groundHeight = 70.0
	liftHeight = 50.0
	
	def __init__(self, legs):
		#legs = array of Leg
		self.legs = legs
		
	def init(self):
		for l in self.legs:
			l.setPosition(40, 0, Spider.groundHeight)
				
	def getLegs(self):
		return self.legs
	
	def getLeg(self, id):
		return self.legs[id]

	def move(self, angle):
		#init the legs
		for i in range(len(self.legs)):
			self.legs[i].moveToward(angle, float(i) / float(len(self.legs)))
			print(float(i) / float(len(self.legs)))

		# walk
		while True:
			for l in self.legs:
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(angle)



if __name__ == "__main__":
	pydyn.enable_vrep()
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	ctrl.start_sim()
	
	legs = configLegs(ctrl.motors)
	s = Spider(legs)
	s.init()
	time.sleep(1.0)
	
	"""
	for leg in s.legs:
		leg.moveToward(30.0)
		while leg.hasScheduledMove():
			leg.move()
	"""
	
	s.move(0.0)
