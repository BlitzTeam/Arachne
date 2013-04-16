import random
import operator
from Motion import *

def initPopulation(count = 100):
	pop = []
	random.seed()
	maxAmplitude = 1.0

	for i in range(count):
		pop.append(ServoMotion(random.random(), random.random(), random.random()))

	return pop

def evaluate(population):
	res = []
	for g in population:
		res.append(fitnessFunction(g))

	return res

def fitnessFunction(gene):
	return 1.0 # TODO

def evolve(pop, res):
	generation = zip(pop, res)
	generation.sort(key=operator.itemgetter(1))
	#print(generation)
	newGeneration = []
	weightSum = sum([j for i,j in generation])

	for i in range(len(pop)):
		newGeneration.append(crossover(weightedRandomChoice(generation, weightSum), weightedRandomChoice(generation, weightSum)))

	return newGeneration

def weightedRandomChoice(generation, weightSum):
	rand = random.random() * weightSum
	for j in generation:
		rand -= j[1]
		if rand < 0:
			return j

def crossover(a, b):
	a_score = a[1]
	b_score = b[1]
	a = a[0]
	b = b[0]
	
	return ServoMotion((a.amplitude + b.amplitude)/2, (a.period + b.period)/2, (a.center + b.center)/2)

def mutate(a):
	pass

if __name__ == '__main__':
	generationCount = 100
	populationCount = 1000

	pop = initPopulation(populationCount)
	res = evaluate(pop)

	for i in range(generationCount):
		print("Generation #%d" % i)
		pop = evolve(pop, res)
		res = evaluate(pop)

	# sort pop according to res to get the fastest one
