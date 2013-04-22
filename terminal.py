import math
from Spider import *
from Config import *


if __name__ == "__main__":
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])	
	spider = Spider(configLegs(ctrl.motors, simulator = False))
	line = ""
	while line != "quit":
		line = raw_input(">> ")
		if line == "help":
			print("help: print the available commands")
		elif line == "joystick":
			print("Joystick mode ON")
		elif line.startsWith("goto"):
			args = line.split(" ")
			if len(args) == 3:
				x = float(args[1])
				y = float(args[2])
				spider.currentDirection = math.degrees(math.atan2(y, x))
			else:
				print("Invalid usage.")
		elif line.startsWith("move"):
			args = line.split(" ")
			if len(args == 2):
				spider.currentDirection = float(args[1])
			else:
				print("Invalid Usage.")
		elif line == "quit":
			pass
		else:
			print("Unknown command")
