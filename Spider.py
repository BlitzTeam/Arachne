import math
import pydyn.dynamixel as dyn
import pydyn
from Config import *
import time
from constants import *

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
		
	def initLegsPosition(self, angle, gait, incremental = False): #init the legs according to the chosen gait
		if gait == Gait.Tripod:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 2 == 0 else 0.5)
		elif gait == Gait.Wave:		
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, float(i) / float(len(self.legs)))
		elif gait == Gait.Ripple:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 3 == 0 else 1/3 if i % 3 == 1 else 2/3)
		
		for l in legs:
			l.move()
		time.sleep(1.0)
		for l in legs:
			l.getCurrentMove().start()


	def move(self, angle = 0.0, gait = Gait.Wave): # problems between -60 and 180 degrees
		self.initLegsPosition(angle, gait)
		
		# walk
		while True:
			for l in self.legs:
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(angle)
										
	def rotate(self, gait = Gait.Wave):
		rotationAngle = 90.0
		self.initLegsPosition(rotationAngle, gait, True)
		
		# walk
		while True:
			for i, l in enumerate(self.legs):
				l.move()
				if not l.hasScheduledMove():
					l.moveToward(rotationAngle + i * 360 / 6)

if __name__ == "__main__":
	pydyn.enable_vrep()
	ctrl = dyn.create_controller(verbose = False, motor_range = [0, 18])
	ctrl.start_sim()
	
	legs = configLegs(ctrl.motors)
	s = Spider(legs)
	s.move(30.0, Gait.Tripod)
