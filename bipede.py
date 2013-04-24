import math
import pydyn.dynamixel as dyn
import pydyn
from Config import *
import time
from Spider import *

def bipedeMove(spider):
	leftLeg = spider.getLeg(0)
	rightLeg = spider.getLeg(5)
	
	spider.getLeg(1).setAngle(150, 150, 150 + 90)
	spider.getLeg(2).setAngle(150 + 90, 150, 150 + 90)
	spider.getLeg(3).setAngle(150 - 90, 150, 150 + 90)
	spider.getLeg(4).setAngle(150, 150, 150 + 90)
		
	while True:
		pass
		
if __name__ == "__main__":
	ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])	
	legs = configLegs(ctrl.motors, simulator = False)
	s = Spider(legs)
	bipedeMove(s)
