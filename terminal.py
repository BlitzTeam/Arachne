import time
import math
#from Spider import *
#from Config import *
import threading
from pypad import *

class GamepadHandler(threading.Thread):
	gamepad = None
	xAxis = 1
	yAxis = 0

	def __init__(self, spider):
		threading.Thread.__init__(self)
		self.spider = spider
		
	def run(self):	
		x, y = 0.0, 0.0	
		while True:
			if GamepadHandler.gamepad != None:
				event = GamepadHandler.gamepad.getEvent()
				if event.eventType == 'axis' and (event.index == GamepadHandler.xAxis or event.index == GamepadHandler.yAxis) :
					if event.index == GamepadHandler.xAxis:
						x = -event.value
					elif event.index == GamepadHandler.yAxis:
						y = event.value
					
					direction = math.degrees(math.atan2(y, x))
					#self.spider.currentDirection = direction

if __name__ == "__main__":	
	#ctrl = dyn.create_controller(verbose = False, motor_range = [0, 20])
	#spider = Spider(configLegs(ctrl.motors, simulator = False))
	line = ""
	thread = GamepadHandler(None)
	thread.setDaemon(True)
	thread.start()
	
	while line != "quit":
		line = raw_input(">> ")
		if line == "help":
			print("help: print the available commands")
		elif line == "joystick":
			GamepadHandler.gamepad = PyPad('/dev/input/js0')
			print("Joystick Enabled")
			
		elif line.startswith("goto"):
			args = line.split(" ")
			if len(args) == 3:
				x = float(args[1])
				y = float(args[2])
				#spider.currentDirection = math.degrees(math.atan2(y, x))
			else:
				print("Invalid usage.")
		elif line.startswith("move"):
			args = line.split(" ")
			if len(args == 2):
				pass
				#spider.currentDirection = float(args[1])
			else:
				print("Invalid Usage.")
		elif line == "quit":
			pass
		else:
			print("Unknown command")

