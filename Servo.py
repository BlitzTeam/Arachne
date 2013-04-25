class Servo:
	def __init__(self, servo_ctrl, min_value = 0, max_value = 299.9, offset = 0.0, orientation = 1.0, initPosition = 150.0):
		self.servo_ctrl = servo_ctrl
		self.min_value = min_value
		self.max_value = max_value
		self.offset = offset
		self.orientation = orientation
		self.initPosition = initPosition
			
	def init(self):
		self.setAngle(self.initPosition)

	def setAngle(self, value): #Set the servo position safely
		#print(value)
		self.servo_ctrl.compliant = False		
		self.servo_ctrl.position = min(self.max_value, max(self.min_value, value + self.offset))

	def getAngle(self): #Get the current servo position
		return self.servo_ctrl.position - self.offset

	def printId(self):
		print(self.servo_ctrl.id)
