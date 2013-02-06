import numpy

class Leg:
	a1 = 4.9
	a2 = -1.4
	b = 5.0
	c = 7.0

	def __init__(self, motor_a, motor_b, motor_c):
		self.motors = [motor_a, motor_b, motor_c]

	@staticmethod
	def angleToPosition(alpha, beta, gamma):
		return numpy.array([numpy.cos(alpha) * (self.a1 + self.b * numpy.cos(beta) + self.c * numpy.cos(beta + gamma)),
                            numpy.sin(alpha) * (self.a1 + self.b * numpy.cos(beta) + self.c * numpy.cos(beta + gamma)),
                            self.a2 + self.b * numpy.sin(beta) +  self.c * numpy.cos(beta + gamma)])
   
	@staticmethod
	def positionToAngle(self, x, y, z):
		pass

if __name__ == "__main__":
	leg = Leg(0,0,0)
	print(leg.angleToPosition(0,0,0))
