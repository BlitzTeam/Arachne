import math

def locationToAngle(x, y, z, b, c):
	alpha = 150 + (90 - math.degrees(math.atan2(x / y)))
	
	return (alpha, 150, 150)
	
	
