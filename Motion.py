from Timer import *
import math

class ServoMotion(object):
	def __init__(self, amplitude, period, center):
		self.amplitude = amplitude
		self.period = period
		self.center = center
		self.motionTimer = Timer()

	def start(self):
		self.motionTimer.start()

	def currentPosition(self):
		return math.sin(self.motionTimer.elapsedTime() * self.period / math.pi) * self.amplitude + self.center




