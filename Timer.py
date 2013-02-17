import time

class Timer(object):
	def __init__(self):
		self.startTime = 0
		self.pauseTime = False

	def start(self):
		self.startTime = time.time()

	def elapsedTime(self):
		if (self.pauseTime == False):
			return time.time() - self.startTime
		return self.pauseTime - self.startTime

	def pause(self):
		self.pauseTime = time.time()

	def resume(self):
		if (self.pauseTime != False):
			self.startTime += time.time() - self.pauseTime
			self.pauseTime = False