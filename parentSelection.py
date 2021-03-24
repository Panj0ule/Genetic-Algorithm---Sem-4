# THIS CODE AUTHORED BY Panj0ule(RafiRizkya)
import random
import numpy.random as npr

def roulleteWheel(listFitness, listPopulation):
    
    sum=0.0
    #formula for probability:
    for i in range(len(listFitness)):
        sum = sum + listFitness[i]
    pick = random.uniform(0, sum)
    current = 0

    for i in range(len(listFitness)):
        current += listFitness[i]
        if current > pick:
            return listPopulation[i]

