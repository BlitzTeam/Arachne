import random
from Motion import *

def initPopulation(count = 100):
	pop = []
	random.seed()
	maxAmplitude = 1.0

	for i in range(count):
		pop.append(ServoMotion(random.uniform(), random.uniform(), random.uniform()))

	return pop

def evaluate(population):
	res = []
	for g in population:
		res.append(fitnessFunction(g))

	return res

def fitnessFunction(gene):
	return 1.0 # TODO

def evolve(pop, res):
	bestScore = max(res)


if __name__ == '__main__':
	generationCount = 100
	populationCount = 1000

	pop = initPopulation(populationCount)
	res = evaluate(population)

	for i in range(generationCount):
		pop = evolve(pop, res)
		res = evaluate(pop)

	# sort pop according to res to get the fastest one