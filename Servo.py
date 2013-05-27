class Servo:
	def __init__(self, servo_ctrl, servo_id, offset = 0):
		self.servo_ctrl = servo_ctrl
		self.id = servo_id
		self.offset = offset
			
	def init(self):
		self.setAngle(self.initPosition)

	def setAngle(self, value):
		self.servo_ctrl.setAngle(self.id, value + self.offset)

