from Timer import *
import math

class ServoMotion(object):
	def __init__(self, amplitude, period, center):
		self.amplitude = float(amplitude)
		self.period = float(period)
		self.center = float(center)
		self.motionTimer = Timer()

	def start(self):
		self.motionTimer.start()

	def currentPosition(self):
		return math.sin(self.motionTimer.elapsedTime() * 2 * math.pi / self.period) * (self.amplitude / 2) + self.center




