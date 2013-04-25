import time
import math
from Spider import *
from Config import *
from Leg import *
import threading
import pydyn.dynamixel as dyn
import pydyn
from pypad import *

class GamepadHandler(threading.Thread):
	gamepad = None
	xAxis = 1
	yAxis = 0
	noiseMin = 0.3

	def __init__(self, spider):
		threading.Thread.__init__(self)
		self.spider = spider
		
	def run(self):	
		x, y = 0.0, 0.0	
		while True:
			if GamepadHandler.gamepad != None:
				event = GamepadHandler.gamepad.getEvent()
				if event.eventType == 'axis' and (event.index == GamepadHandler.xAxis or event.index == GamepadHandler.yAxis):
					if event.index == GamepadHandler.xAxis:
						x = -event.value
					elif event.index == GamepadHandler.yAxis:
						y = event.value
					
					direction = math.degrees(math.atan2(y, x))
					self.spider.currentDirection = direction
					print(direction)
			else:
				time.sleep(0.5)

class TerminalThread(threading.Thread):
	def __init__(self, spider):
		threading.Thread.__init__(self)
		self.spider = spider
		
	def run(self):
		line = ""
		while line != "quit":
			line = raw_input(">> ")
			if line == "help":
				print("help: print the available commands")
				print("joystick: enable/disable the joystick to control the spider")
				print("goto [x] [y]: move the spider to the give position")
				print("move [direction]: move the spider toward the given direction")
				print("stop: stops the spider")
				print("quit: quits the program")
			
			elif line == "joystick":
				if GamepadHandler.gamepad == None:
					GamepadHandler.gamepad = PyPad('/dev/input/js0')
					print("Joystick Enabled")
				else:
					GamepadHandler.gamepad = None
			elif line.startswith("goto"):
				args = line.split(" ")
				if len(args) == 3:
					x = float(args[1])
					y = float(args[2])
					spider.currentDirection = math.degrees(math.atan2(y, x))
				else:
					print("Invalid usage.")
			elif line == "stop":
				spider.moving = False
			elif line.startswith("move"):
				args = line.split(" ")
				if len(args) == 2:
					spider.moving = True
					spider.currentDirection = float(args[1])
					print("moving toward ", float(args[1]))
				else:
					print("Invalid Usage.")
			elif line == "quit" or line == "":
				pass
			else:
				print("Unknown command")
			
if __name__ == "__main__":	
	ctrl = dyn.create_controller(verbose = False, timeout = 0.5, motor_range = [0, 20])
	spider = Spider(configLegs(ctrl.motors, simulator = False))

	gamepadThread = GamepadHandler(spider)
	gamepadThread.daemon = True
	gamepadThread.start()

	terminalThread = TerminalThread(spider)
	terminalThread.daemon = True
	terminalThread.start()
	
	while True:
		spider.move(startNow = False)


