import sys, time
import pydyn.dynamixel as dyn

ctrl = dyn.create_controller(verbose = True, motor_range = [0, 20])


for m in ctrl.motors:
    m.compliant = True
    print m.id," = ",m.position

    
    ctrl.wait(2)
