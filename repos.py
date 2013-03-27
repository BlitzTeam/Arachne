import sys, time
import pydyn.dynamixel as dyn
from Config import *
from Spider import *
from Leg import *
from Servo import *
import pydyn

pydyn.enable_vrep()
ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])

s = None 

def config():
    #Limitation vitesse(speed) et force(torque):
    for m in ctrl.motors:
        m.compliant = False
        m.max_torque = 50
        m.speed = 30


def repos():
	global s
	'''
	tabPositions =  [0]*18

	#patte 1
	tabPositions[0]  =  180
	tabPositions[4]  =  85
	tabPositions[5]  =  50

	#patte2
	tabPositions[13]  =  200
	tabPositions[2]  =  190
	tabPositions[16]  =  175

	#patte3
	tabPositions[8]  =  200
	tabPositions[6]  =  190
	tabPositions[7]  =  130

	#patte4
	tabPositions[11]  =  180
	tabPositions[10]  =  85
	tabPositions[14]  =  240

	#patte5
	tabPositions[15]  =  -1
	tabPositions[3]  =  -1
	tabPositions[9]  =  -1

	#patte6
	tabPositions[17]  =  180
	tabPositions[1]  =  -1
	tabPositions[12]  =  -1




	for m in ctrl.motors:
		print m.id ," " ,m.position , "->", tabPositions[m.id-1]
		if tabPositions[m.id-1]>0 :
	    	m.position = tabPositions[m.id-1]
	'''
	l = configLegs(ctrl.motors);
	s = Spider(l)
	print("s : " ,s)
	s.getLeg(1).goToAngle(100,100,100)
	print("position 1 " , s.getLeg(1).getPosition())
	print("appuyez pour aller a la prochaine position . . .")
	raw_input()
	s.getLeg(1).goToAngle(150,100,100)
	print("position 2 " ,s.getLeg(1).getPosition())
	print("appuyez pour aller a la prochaine position . . .")
	raw_input()
	s.getLeg(1).goToAngle(150,100,50)
	print("appuyez pour avoir les valeurs apres le mouvement . . .")
	raw_input()
	print("position 3 " ,s.getLeg(1).getPosition())
	print("appuyez pour aller a la prochaine position . . .")
	raw_input()
	'''
	s.makeCompliant(True)
	print("Mettez l'araignee dans la position initiale voulue")
	raw_input()
	s.initStartPosition()
	print("Bougez l'araignee")
	raw_input()
	s.makeCompliant(False)
	s.goToStartPosition()
	raw_input()
	'''

if __name__ == "__main__":
   # config()
    repos()

    
    raw_input()
    
