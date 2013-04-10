import math

def locationToAngle(x, y, z, a, b):
	alpha = 150 + (90 - math.degrees(math.atan2(x / y)))
	
	p = math.sqrt(x**2 + y**2)
	l = math.sqrt(p**2 + z**2)
	
	gamma = math.degrees(math.acos((-l**2 + a**2 + b**2) / (2 * a * b))) + 60

	tmp1 = math.degrees(acos((-p**2 + z**2 + l**2) / (2 * z * l)))
	tmp2 = math.degrees(acos((-b**2 + a**2 + l**2) / (2 * a * l)))
	beta = 150  + (90 - (tmp1 + tmp2))	

	return (alpha, beta, gamma)
	
	
