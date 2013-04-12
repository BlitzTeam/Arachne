import numpy
import sys, time
import pydyn.dynamixel as dyn
import math
from inverseKinematics import *
import pydyn
from Config import *
from Spider import *

class Leg:
	a1 = 49
	a2 = -14
	b = 50
	c = 70
	
	alpha0 = 150
	beta0 = 175
	gamma0 = 90

	def __init__(self, orientation, x , y , servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x # top down view
		self.y = y # top down view
		self.motors = (servo_up, servo_middle, servo_down)

	def getMotors(self):
		return self.motors

	def getMotor(self, id):
		return self.motors[id]

	def setAngleMotor(self, id, angle):
		self.motors[id].setPosition(angle)

	def makeCompliant(self, compliant = True):
		for m in self.motors:
			m.makeCompliant(compliant)

	def setAngle(self, a, b, c):
		self.setAngleMotor(0, a)
		self.setAngleMotor(1, b)
		self.setAngleMotor(2, c)
				
	def angleToPosition(self, alpha, beta, gamma, relative = True):
		if relative == True:
			return (numpy.cos(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								numpy.sin(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								Leg.a2 + Leg.b * numpy.sin(beta) +  Leg.c * numpy.cos(beta + gamma))
		else:
			rel = self.angleToPosition(alpha, beta, gamma, True)
		return() # TODO: Implementation

	def setPosition(self, x, y, z):
		angles = Leg.locationToAngle(x, y, z, Leg.b, Leg.c)
		print(angles)
		self.setAngle(angles[0], angles[1], angles[2])

	@staticmethod            	
	def locationToAngle(x, y, z, a, b):
		print(a, b)
		alpha = 150 + (90 - math.degrees(math.atan2(x, y)))
	
		p = math.sqrt(x**2 + y**2)
		l = math.sqrt(p**2 + z**2)
		if (l > a + b):
			return None

		print(p, l, (-l**2 + a**2 + b**2) / (2 * a * b))
	
		gamma = math.degrees(math.acos((-l**2 + a**2 + b**2) / (2 * a * b)))

		o3 = math.degrees(math.acos(z/l))
		o4 = math.degrees(math.acos((-b**2 + a**2 + l**2) / (2 * a * l)))
		print(o3, o4)
		beta = 90 - (o3 + o4)	

		print(alpha, beta, gamma)
		return (alpha, beta + 150, 180 - gamma + 60)
		
if __name__ == '__main__':
	pydyn.enable_vrep()
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])
	ctrl.start_sim()
	
	l = configLegs(ctrl.motors)
	s = Spider(l)
	s.init()
	
	leg = s.getLeg(1)
	leg.setPosition(50, 0, 0)
	raw_input()
	leg.setPosition(70, 0, 0)
	raw_input()
	leg.setPosition(90, 0, 0)
	raw_input()
	
