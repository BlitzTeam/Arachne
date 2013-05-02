import time
import math
from Spider import *
from Config import *
from Leg import *
import threading
import pydyn.dynamixel as dyn
import pydyn
from pypad import *

class GamepadReader(threading.Thread):
	xAxis = 1
	yAxis = 0
	noiseMin = 0.3
	aButton = 0

	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):			
		while True:
			if GamepadHandler.gamepad != None:
				event = GamepadHandler.gamepad.getEvent()
				if event.eventType == 'axis' and event.index == GamepadReader.xAxis and math.sqrt(event.value**2 + GamepadHandler.yValue**2) > GamepadReader.noiseMin:
					GamepadHandler.xValue = -event.value
				elif event.eventType == 'axis' and event.index == GamepadReader.yAxis and math.sqrt(event.value**2 + GamepadHandler.xValue**2) > GamepadReader.noiseMin:
					GamepadHandler.yValue = event.value
				elif event.eventType == 'button' and event.index == GamepadReader.aButton and event.value == True:
					GamepadHandler.aButtonValue = not GamepadHandler.aButtonValue
					
			else:
				time.sleep(0.5)

class GamepadHandler(threading.Thread):
	gamepad = None
	xValue = 0.0
	yValue = 0.0
	maxTurnSpeed = 3.0
	aButtonValue = True

	def __init__(self, spider):
		threading.Thread.__init__(self)
		self.readerThread = GamepadReader()
		self.readerThread.daemon = True
		self.readerThread.start()
		self.spider = spider
			
	def run(self):	
		direction = 0.0
		
		while True:
			if GamepadHandler.gamepad != None:
				x = GamepadHandler.xValue
				y = GamepadHandler.yValue
				direction = direction + min(max(-GamepadHandler.maxTurnSpeed, math.degrees(math.atan2(y, x)) - direction), GamepadHandler.maxTurnSpeed)
				self.spider.turnAngle = direction
				self.spider.moving = GamepadHandler.aButtonValue
				time.sleep(0.1)
			else:
				time.sleep(0.5)

class TerminalThread(threading.Thread):
	def __init__(self, spider):
		threading.Thread.__init__(self)
		self.spider = spider
		self.gamepadThread = gamepadThread
		
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
			
			elif line == "joystick" or line == "gamepad":
				if GamepadHandler.gamepad == None:
					GamepadHandler.gamepad = PyPad('/dev/input/js0')
					print("Joystick Enabled")
					self.spider.moving = True
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
	spider = None
	ctrl = dyn.create_controller(verbose = False, timeout = 0.5, motor_range = [0, 20])
	spider = Spider(configLegs(ctrl.motors, simulator = False))

	gamepadThread = GamepadHandler(spider)
	gamepadThread.daemon = True
	gamepadThread.start()

	terminalThread = TerminalThread(spider)
	terminalThread.daemon = True
	terminalThread.start()
	
	while True:
		time.sleep(1.0)
		spider.move(startNow = False)


