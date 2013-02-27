from Timer import *
import time
import math

class ServoMotion(object):
	def __init__(self, amplitude, period, center, offset = 0):
		self.amplitude = float(amplitude)
		self.period = float(period)
		self.center = float(center)
		self.offset = float(offset)
		self.motionTimer = Timer()

	def start(self):
		self.motionTimer.start()

	def currentPosition(self):
		return math.sin((self.motionTimer.elapsedTime() * 2 * math.pi + self.offset) / self.period) * (self.amplitude / 2) + self.center

class SpiderMotion(object):
	"motions = array of ServoMotion"
	def __init__(self, motions):
		self.motions = 	motions

	def start(self):
		for m in self.motions:
			m.start



if __name__ == '__main__':
	s = ServoMotion(20,5,10,0.25)
	s.start()
	while(True):
		print(s.currentPosition())
		time.sleep(0.1)
	
