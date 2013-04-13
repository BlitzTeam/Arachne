from Timer import *
import time
import math

class ServoMotion(object):
	def __init__(self, amplitude, period, center, offset = 0.0):
		self.amplitude = float(amplitude)
		self.period = float(period)
		self.center = float(center)
		self.offset = float(offset)
		self.motionTimer = Timer()

	def start(self):
		self.motionTimer.start()

	def currentPosition(self):
		return math.sin((self.motionTimer.elapsedTime() * 2 * math.pi + self.offset * self.period) / self.period) * (self.amplitude / 2) + self.center

class LegMotion(object):
	def __init(self, startValues, endValues, time = 1.0):
		self.startValues = startValues
		self.endValues = endValues
		self.time
		self.motionTimer = Timer()
	
	def start(self):
		self.motionTimer.start()
		
	def currentValues(self):
		currentTime = self.motionTimer.elapsedTime()
		return (extrapolate(self.startValues[0], self.endValues[0], currentTime, self.time),
				extrapolate(self.startValues[1], self.endValues[1], currentTime, self.time),
				extrapolate(self.startValues[2], self.endValues[2], currentTime, self.time))
	
	def isDone(self):
		return self.motionTimer.elapsedTime() > time
		
	@staticmethod
	def extrapolate(startValue, endValue, currentTime, totalTime):
		if currentTime > totalTime:
			return endValue
		return startValue + (endValue - startValue) * (currentTime / totalTime) 

if __name__ == '__main__':
	s = ServoMotion(20,5,10,0.25)
	s.start()
	while(True):
		print(s.currentPosition())
		time.sleep(0.1)
	
