# THIS CODE AUTHORED BY Panj0ule(RafiRizkya)
import random

def recombination(parent1, parent2):
    child1 = parent1
    child2 = parent2
    intersectP = random.randint(0,len(parent1)-1)
    print("INTERSECT POINT:")
    print(intersectP, "\n")

    #PROCESS SWAP USING 1 POINT
    temp = child1[intersectP:].copy()
    child1[intersectP:] = child2[intersectP:]
    child2[intersectP:] = temp

    return [child1, child2]

def mutation(chromosome):
    point1 = random.randint(0,(len(chromosome)//2) - 1)
    point2 = (len(chromosome)-1) - point1
    print("SWAP POINT: ")
    print(point1, "\n")

    temp = chromosome[point1]
    chromosome[point1] = chromosome[point2]
    chromosome[point2] = temp

    return chromosome

