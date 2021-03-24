
#selects Survivor menggunakan steady state

def steadyState(listFitness,listPopulation, child1, child2):
    indexMin = listFitness.index(min(listFitness))
    listPopulation[indexMin]=child1
    listFitness[indexMin]= 9999999
    indexMin = listFitness.index(min(listFitness))
    listPopulation[indexMin]=child2
    
    return listPopulation
