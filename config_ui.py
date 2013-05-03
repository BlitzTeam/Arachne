import pydyn.dynamixel as dyn
import pydyn

if __name__ == '__main__':
	print('Put the spider in the init position')
	print('Press any key when ready')
	raw_input()
	
	for i in range(18):
		print('Move the motor %d of the leg %d and press any key when ready', i%3, i/3)
		raw_input()
	
	
