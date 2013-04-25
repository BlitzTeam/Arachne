import math
import pydyn.dynamixel as dyn
import pydyn
import thread
from Config import *
import time
from constants import *

class Spider:
	walkSpeed = 100.0 / 9.89
	rotationSpeed = 180.0 / 13.3

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
		
	def initLegsPosition(self, angle, gait, turnAngle = 0.0, incremental = False): #init the legs according to the chosen gait
		if gait == Gait.Tripod:
			Leg.liftTime = 0.3
			Leg.forwardTime = 0.3
			Leg.pullTime = 0.7
 
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 2 == 0 else 0.5, turnAngle=turnAngle)
		elif gait == Gait.Wave:
			Leg.liftTime = 0.3
			Leg.forwardTime = 0.3
			Leg.pullTime = 3.6
			
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, float(i) / float(len(self.legs)), turnAngle=turnAngle)
		elif gait == Gait.Ripple:
			Leg.liftTime = 0.3
			Leg.forwardTime = 0.3
			Leg.pullTime = 1.8
			
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 3 == 0 else 1/3 if i % 3 == 1 else 2/3, turnAngle=turnAngle)
		tmpLegs = (self.legs[1], self.legs[4], self.legs[0], self.legs[2], self.legs[3], self.legs[5])
		for l in self.legs:
			l.move()
			time.sleep(0.01)
		time.sleep(1.0)
		for l in self.legs:
			l.getCurrentMove().start()

	def move(self, angle = 0.0, gait = Gait.Tripod, startNow = True, turnAngle = 0.0, distance = None, duration = None): # problems between -60 and 180 degrees
			self.currentDirection = angle
			self.turnAngle = turnAngle
			
			timer = None
			if distance != None:
				duration = Spider.distanceToTime(distance)
			if duration != None:
				timer = Timer()
							
			if startNow:
				self.moving = True
			else:
				while not self.moving:
					time.sleep(0.2)
			
			self.initLegsPosition(self.currentDirection, gait, turnAngle = self.turnAngle)
			
			if timer != None:
				timer.start()

			while self.moving and (timer == None or timer.elapsedTime() < duration):
				for l in self.legs:
					l.move()
					if not l.hasScheduledMove():
						l.moveToward(self.currentDirection, turnAngle = self.turnAngle)
					time.sleep(0.01)

	def rotate(self, gait = Gait.Tripod, angle = None, duration = None):
		rotationAngle = 90.0
		timer = None
		if angle != None:
			duration = Spider.angleToTime(angle)
		if duration != None:
			timer = Timer()
		self.initLegsPosition(rotationAngle, gait, incremental = True)
		
		if timer != None:
			timer.start()
		# walk
		while timer == None or timer.elapsedTime() < duration:
			for i, l in enumerate(self.legs):
				if not l.hasScheduledMove():
					l.moveToward(rotationAngle + i * 360 / 6)
				l.move()
				time.sleep(0.01)
				
	@staticmethod
	def distanceToTime(distance):
		return distance / Spider.walkSpeed
	
	@staticmethod
	def angleToTime(angle):
		return angle / Spider.rotationSpeed
				

if __name__ == "__main__":
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	legs = configLegs(ctrl.motors, simulator = False)
	for i in range(-180, 180, 45):
		print('Angle ' + str(i)) 
		for l in legs:
			print(l.orientation, l.preferredDirection, l.getRelativeDirection2(i))
			l.setRealAngle(l.getRelativeDirection2(i)[0], 0, 0)
		raw_input()
