import numpy
import sys, time
import pydyn.dynamixel as dyn
import math

class Leg:
	a1 = 49
	a2 = -14
	b = 50
	c = 70
	
	alpha0 = math.radians(150)
	beta0 = math.radians(175)
	gamma0 = math.radians(90)

	def __init__(self, orientation, x , y , servo_up, servo_middle, servo_down):
		self.orientation = orientation
		self.x = x # top down view
		self.y = y # top down view
		self.motors = (servo_up, servo_middle, servo_down)

	def getMotor(self, id):
		return self.motors[id]

	def initStartPosition(self):
		for m in self.motors:
			m.initStartPosition()

	def goToStartPosition(self):
		for m in self.motors:
			m.goToStartPosition()

	def makeCompliant(self, compliant = True):
		for m in self.motors:
			m.makeCompliant(compliant)

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
		
	#@staticmethod
	def angleToPosition(self, alpha, beta, gamma, relative = True):
		if relative == True:
			return (numpy.cos(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								numpy.sin(alpha) * (Leg.a1 + Leg.b * numpy.cos(beta) + Leg.c * numpy.cos(beta + gamma)),
								Leg.a2 + Leg.b * numpy.sin(beta) +  Leg.c * numpy.cos(beta + gamma))
		else:
			rel = self.angleToPosition(alpha, beta, gamma, True)
			return () # TODO: Implementation
			

		#Place le bout de patte a la position [x,y,z] passee en parametres en fonction du debut de la patte
		#(Modele inverse)

	def setPositionPatte(self,x,y,z):
		mot = self.getAngle(x, y, z)
		if(mot == None):
			print("ERROR : Position impossible")
			return
		for i in range(3): 
			if mot[i] % 360 > 300:
				mot[i] = 300
				self.setMotor(i,mot[i] % 360)
		#Recupere les angles [alpha,beta,gamma] en degres des moteurs a appliquer pour deplacer le bout de la patte a la position [x,y,z] passee en parametres
		#(Calcul du modele inverse)

	def getAngle(self,x, y, z):
		u = math.sqrt(x * x + y * y)
		if(u == 0):
			#alpha = math.radians(150 - self.alpha0) # valeur arbitraire car infinite de possibilite
			alpha = math.atan(x/y)
		else:
			alpha = math.atan(y / x)
		if( abs((alpha % math.pi) - (math.pi / 2)) < 0.00001):
			u = y / math.sin(alpha)
		else:
			u = x / math.cos(alpha)
		#print u

		up = u - self.a1
		zp = z - self.a2

		if(up**2 + zp**2 <= (self.b + self.c)**2 and up**2 + zp**2 >= (self.b - self.c)**2):
			cosGamma = (up**2 + zp**2 - self.b**2 - self.c**2) / (2*self.b*self.c)
			absGamma = math.acos(cosGamma)
			#print absGamma
		else:
			return None

		gamma = -absGamma
		sinGamma = -math.sqrt(1 - cosGamma ** 2)
		#absBeta = math.acos(((u - self.a1) * (self.b + self.c * cosGamma) + (z - self.a2) * self.c * sinGamma) / ((u - self.a1)**2 + (z - self.a2)**2))
		sinBeta = ((z - self.a2) * (self.b + self.c * cosGamma) - (u - self.a1) * self.c * sinGamma) / ((u - self.a1)**2 + (z - self.a2)**2)
		cosBeta = ((u - self.a1) * (self.b + self.c * cosGamma) + ((z - self.a2) * self.c * sinGamma)) / ((u - self.a1)**2 + (z - self.a2)**2)
		beta = math.atan2(sinBeta, cosBeta)

		#print beta

		# signe de beta
		"""if sinBeta < 0:
		beta = -absBeta
		else:
		beta = absBeta
		##"""

		# signe de gamma

		gamma = -gamma

		return [math.degrees(alpha + self.alpha0),
		math.degrees(beta + self.beta0),
		math.degrees(gamma + self.gamma0)]
                	
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
	

	'''
		 #u = a1 + b * numpy.cos(beta) + c * numpy.cos(beta+gamma)
		 
		#calcul de alpha
		u = math.sqrt(x**2 + y**2)
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
		'''
"""
