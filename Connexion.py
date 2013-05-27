import serial

class Connexion:
	def __init__(self):
		self.connexion = serial.Serial('/dev/ttyACM0', 115200)
	def setAngle(self, motorID, value):
		cmd = str(motorID) + ':' + str(value) + '|'
		self.connexion.write(cmd)
