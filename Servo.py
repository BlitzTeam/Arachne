class Servo:
	
	def __init__(self, servo_ctrl, min_value = 0, max_value = 299.9, offset = 0.0, orientation = 1.0, initPosition = 150):
		self.servo_ctrl = servo_ctrl
		self.min_value = min_value
		self.max_value = max_value
		self.offset = offset
		self.orientation = orientation
		self.initPosition = initPosition
	
	def initStartPosition(self):
		self.initPosition = self.servo_ctrl.position
		
	def init(self):
		self.setPosition(self.initPosition)

	def goToStartPosition(self):
		self.setPosition(self.initPosition)

	def makeCompliant(self, compliant = True):
		print("compliant param = " , compliant)
		print("compliant motor= " , self.servo_ctrl.compliant)
		self.servo_ctrl.compliant = compliant
		print("new compliant motor = " , self.servo_ctrl.compliant)

	def setPosition(self, value): #Set the servo position safely
		self.servo_ctrl.compliant = False		
		self.servo_ctrl.position = min(self.max_value, max(self.min_value, value + self.offset))

	def getPosition(self):
		#Get servo position
		return self.servo_ctrl.position

	def getStartPosition(self):
		#Get servo position
		return self.initPosition

	def printId(self):
		print(self.servo_ctrl.id)
