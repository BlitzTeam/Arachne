import numpy
import sys, time
import pydyn.dynamixel as dyn


class Leg:
	a1 = 4.9
	a2 = -1.4
	b = 5.0
	c = 7.0

	def __init__(self, orientation, x, y, servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x
		self.y = y
		self.motors = (servo_up, servo_middle, servo_down)

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
			return ()
			
	@staticmethod
	def positionToAngle(self, x, y, z):
		pass

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
