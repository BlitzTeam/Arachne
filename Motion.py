from Timer import *
import time
import math

class LegMotion(object):
	def __init__(self, startValues, endValues, time = 5.0):
		self.startValues = startValues
		self.endValues = endValues
		self.time = time
		self.motionTimer = Timer()
		self.start()
	
	def start(self):
		self.motionTimer.start()
		
	def currentValues(self, dt):
		return LegMotion.extrapolateBatch(self.startValues, self.endValues, self.motionTimer.elapsedTime() + dt, self.time)
	
	def isDone(self):
		return self.motionTimer.elapsedTime() > self.time
		
	@staticmethod
	def extrapolate(startValue, endValue, currentTime, totalTime):
		if currentTime > totalTime:
			return endValue
		return startValue + (endValue - startValue) * (currentTime / totalTime)
	
	@staticmethod
	def extrapolateBatch(startValues, endValues, currentTime, totalTime):
		if len(startValues) != len(endValues):
			print("Error: startValues and endValues must have the same length in LegMotion.extrapolateBatch()")
		res = []
		for i in range(len(startValues)):
			res.append(LegMotion.extrapolate(startValues[i], endValues[i], currentTime, totalTime))
		return res

