class Servo:
	
	def __init__(self, servo_ctrl, min_value = 0, max_value = 359, offset = 0.0, orientation = 1.0, initPosition = 0):
		self.servo_ctrl = servo_ctrl
		self.min_value = min_value
		self.max_value = max_value
		self.offset = offset
		self.orientation = orientation
		self.initPosition = initPosition
		self.compliant = servo_ctrl.compliant
		self.position = servo_ctrl.position
	
	def initStartPosition(self):
		self.initPosition = self.servo_ctrl.position

	def goToStartPosition(self):
		self.setPosition(self.initPosition)

	def makeCompliant(self, compliant = True):
		print("compliant param = " , compliant)
		print("compliant motor= " , self.servo_ctrl.compliant)
		self.servo_ctrl.compliant = compliant
		print("new compliant motor = " , self.servo_ctrl.compliant)

	def setPosition(self, value):
		#Set the servo position safely
		self.servo_ctrl.position = min(self.max_value, max(self.min_value, value))

	def getPosition(self):
		#Get servo position
		return self.position

	def getStartPosition(self):
		#Get servo position
		return self.initPosition
