import numpy
import sys, time
import pydyn.dynamixel as dyn
import math

class Leg:
	a1 = 4.9
	a2 = -1.4
	b = 5.0
	c = 7.0

	def __init__(self, orientation = 1, x = 0, y = 0, servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x # top down view
		self.y = y # top down view
		self.motors = (servo_up, servo_middle, servo_down)

	def moveToward(self, direction):
		"""
		Moves the leg toward direction. Waits until the move is done.
		"""
		# move up
		# move toward
		#]move down
		pass

	#def getAngle(self, id_motor):
		#return self.motors[id_motor].position - self.origins[id_motor]
		
	@staticmethod
	def angleToPosition(alpha, beta, gamma, relative = True):
		if relative == True:
			return (numpy.cos(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								numpy.sin(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								Leg.a2 + Leg.b * numpy.sin(beta) +  Leg.c * numpy.cos(beta + gamma))
		else:
			rel = angleToPosition(alpha, beta, gamma, True)
			return () # TODO: Implementation
			
	@staticmethod
	def positionToAngle(self, x, y, z):
		 #u = a1 + b * numpy.cos(beta) + c * numpy.cos(beta+gamma)
		 
		#calcul de alpha
		u = math.sqrt(x**2+y**2)
		if (u != 0):
			if(u < 0):
				signe = -1
			else:
				signe = 1
			alpha = signe * 2 * numpy.arctan(y/(x+u**2))
		else:
			raise AssertionError("error, alpha equals 0")
			
		#calcul de gamma
		tmpGamma = ((u - self.a1)**2 + (z + self.a2)**2 - self.b**2 - self.c**2) / 2 * self.b * self.c
		if (((u - self.a1)**2 + (z - self.a2)**2) <= ((self.b + self.c)**2) and ((((u - self.a1)**2) + (z - self.a2)**2) >= ((self.b + self.c)**2))):
			gamma = numpy.arccos(tmpGamma)
		else:
			raise AssertionError("error, gamma not between -1 & 1")
		
		#calcul de beta
			sinBeta = ((z - self.a2) * (self.b + self.c * numpy.cos(gamma)) - (u - self.a1) * self.c * numpy.sin(gamma)) / ((u - self.a1)**2 + (z - self.a2)**2)
			cosBeta = ((u - self.a1) * (self.b + self.c * numpy.cos(gamma)) - (z - self.a2) * self.c * numpy.sin(gamma)) / ((u - self.a1)**2 + (z - self.a2)**2)
		
		print "alpha : %f" % (alpha, )
		print "cosBeta : " + cosBeta
		print "sinBeta : %f" % (cosBeta, )
		print "gamma : " + gamma
		return [alpha, cosBeta, gamma]
			
"""
if __name__ == "__main__":
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	a_motors = ctrl.motors[0]
	b_motors = ctrl.motors[1]
	c_motors = ctrl.motors[2]
	
	leg = Leg(a_motors , b_motors , c_motors, 147, 149, 245)
	
	alfa = a_motors.position - Leg.moto
	beta
	gamma
	
	print(leg.angleToPosition(a_motors.position,b_motors.position,c_motors.position))

	print (a_motors.position,b_motors.position,c_motors.position)
	
"""
