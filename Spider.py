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
		
	def initLegsPosition(self, angle): #init the legs according to the chosen gait
		if gait == Gait.Tripod:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle, 0.0 if i % 2 == 0 else 0.5))
		elif gait == Gait.Wave:		
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle, float(i) / float(len(self.legs)))
		elif gait == Gait.Ripple:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle, 0.0 if i % 3 == 0 else 1/3 if i % 3 == 1 else 2/3)


	def move(self, angle = 0.0, gait = Gait.Wave):
		self.initLegsPosition(gait)				
		#wait until th
		
		# walk
		while True:
			for l in self.legs:
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(angle)
					
	def rotate(self, gait = Gait.Wave):
		rotationAngle = 30.0 # Check this value
		self.initLegsPosition(gait)
		
		
		# walk
		while True:
			for l in self.legs:
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(angle, 0.0, True)



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
