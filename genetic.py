import random
import operator
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
	generation = zip(pop, res)
	generation.sort(key=operator.itemgetter(1))
	newGeneration = []
	weightSum = sum([j for i,j in generation])

	for i in range(len(pop)):
		newGeneration.append(mutate(weightedRandomChoice(generation, weightSum), weightedRandomChoice(generation, weightSum))

	return newGeneration

def weightedRandomChoice(generation, weightSum):	
	rand = random.random() * weightSum
	for j in pop:
		rand -= j[1]
		if rand < 0:
			return j



def mutate(a, b):
	a_score = a[1]
	b_score = b[1]
	a = a[0]
	b = b[0]
	
	return ServoMotion((a.amplitude + b.amplitude)/2, (a.period + b.period)/2, (a.center + b.center)/2)

if __name__ == '__main__':
	generationCount = 100
	populationCount = 1000

	pop = initPopulation(populationCount)
	res = evaluate(population)

	for i in range(generationCount):
		pop = evolve(pop, res)
		res = evaluate(pop)

	# sort pop according to res to get the fastest one
