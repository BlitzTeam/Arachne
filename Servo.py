class Servo():
	def __init__(self, servo_ctrl, min_value = 0, max_value = 359, offset = 0.0, orientation = 1.0):
		self.servo_ctrl = servo_ctrl
		self.min_value = min_value
		self.max_value = max_value
		self.offset = offset
		self.orientation = orientation

	def setPosition(self, value):
		"Set the servo position safely"
		self.servo_ctrl.position = min(self.max_value, max(self.min_value, value))

