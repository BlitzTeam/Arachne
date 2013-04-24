import math
#import pydyn.dynamixel as dyn
#import pydyn
import thread
from Config import *
import time
from constants import *

class Spider:	
	def __init__(self, legs):
		#legs = array of Leg
		self.legs = legs
		self.currentDirection = 0.0
		self.moving = False
		self.turnAngle = 0.0
		
	def init(self):
		for l in self.legs:
			l.setPosition(40, 0, Config.groundHeight)
				
	def getLegs(self):
		return self.legs
	
	def getLeg(self, id):
		return self.legs[id]
		
	def initLegsPosition(self, angle, gait, turnAngle = 0.0, incremental = False): #init the legs according to the chosen gait
		if gait == Gait.Tripod:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 2 == 0 else 0.5, turnAngle=turnAngle)
		elif gait == Gait.Wave:		
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, float(i) / float(len(self.legs)), turnAngle=turnAngle)
		elif gait == Gait.Ripple:
			for i in range(len(self.legs)):
				self.legs[i].moveToward(angle if not incremental else angle + 360 / 6 * i, 0.0 if i % 3 == 0 else 1/3 if i % 3 == 1 else 2/3, turnAngle=turnAngle)
		
		for l in self.legs:
			l.move()
			time.sleep(0.01)
		time.sleep(1.0)
		for l in self.legs:
			l.getCurrentMove().start()
			time.sleep(0.01)

	def move(self, angle = 0.0, gait = Gait.Tripod, startNow = True, turnAngle = 0.0): # problems between -60 and 180 degrees
			self.currentDirection = angle
			self.turnAngle = turnAngle
			if startNow:
				self.moving = True
			else:
				while not self.moving:
					time.sleep(0.1)
			
			self.initLegsPosition(self.currentDirection, gait, turnAngle = self.turnAngle)
			# walk
			#currentTime = 0
			while self.moving:
				#print("update", time.time() - currentTime)
				#currentTime = time.time()
				for l in self.legs:
					l.move()
					if not l.hasScheduledMove():
						l.moveToward(self.currentDirection, turnAngle = self.turnAngle)
					time.sleep(0.01)

	def rotate(self, gait = Gait.Wave):
		rotationAngle = 90.0
		self.initLegsPosition(rotationAngle, gait, True)
		
		# walk
		while True:
			for i, l in enumerate(self.legs):
				if not l.hasScheduledMove():
					l.moveToward(rotationAngle + i * 360 / 6)
				l.move()
				time.sleep(0.01)
				

if __name__ == "__main__":
	#ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	motors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	
	legs = configLegs(motors, simulator = False)
	for i in range(-180, 180, 45):
		print('Angle ' + str(i)) 
		for l in legs:
			print(l.orientation, l.preferredDirection, l.getRelativeDirection2(i))

