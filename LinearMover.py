import pydyn.dynamixel as dyn
from LegNames import *

class LinearMover(object):
	baudrate = 1000000

	def __init__(self, motors, motions):
		self.motors = motors
		self.motions = motions		


	def run(self):
		for m in self.motors:
			m.compliant = True

		while(True):
			for i in range(len(self.motors)):
				self.motors[i].position = self.motions[i].currentPosition()


if __name__ == '__main__':
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20], start = False, baudrate = baudrate)
	ctrl.start()

	# TODO:
	# -make sure motors are sorted according to LegNames
	# -retrieve motion values

	motions = []

	lm = LinearMover(ctrl.motors, motions)
	lm.run()