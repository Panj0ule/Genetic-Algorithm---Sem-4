# THIS CODE AUTHORED BY Panj0ule(RafiRizkya)
import InitializationPop
import representBinary
import pprint
import parentSelection
import childSelection
import selectionSurvivor
import random
from tabulate import tabulate
listSplit=[]
listPtype=[]
listFitness=[]

# Chromosome menggunakan tipe BINARY
# dan untuk seleksi orang tua menggunakan teknik roulette wheel
# Rekombinasi menggunakan satu titik
# seleksi survivor menggunakan elitisme

jumChromo = int(input("Masukan jumlah chromosome: "))
jumPops = int(input("masukan jumlah populasi: "))
jumGenerasi = int(input("masukan jumlah Generasi: "))
prob = float(input("masukan jumlah probabilitas mutasi(0-100): "))
populations = InitializationPop.initPop(jumChromo,jumPops)
print("Generating Population: ")
print(populations)
print("\n")

print("Generating f(h):")
rBx = int(input("Masukan batas bawah X: "))
rAx = int(input("Masukan batas Atas X: "))
rBy = int(input("Masukan batas bawah Y: "))
rAy = int(input("Masukan batas Atas Y: "))
print("\n")

for i in range(jumPops):
    listSplit.append(InitializationPop.splitter(populations[i]))
    
print("this is the list of splitted phenotype:", type(listSplit))
pprint.pprint(listSplit)
print("\n")

#PROCESS DECODE
for i in range(jumPops):
    listPtype.append(representBinary.decodeChromo(rBx,rAx,rBy,rAy, listSplit[i][0], listSplit[i][1])) 

print("this is the list of Decoded Chromosome:", type(listPtype))
pprint.pprint(listPtype)
print("\n")

#PROCESS FITNESS CALCULATION
for i in range(jumPops):
    listFitness.append(representBinary.calcFitness(listPtype[i][0], listPtype[i][1]))

print("this is the list of Fitness:", type(listFitness))
pprint.pprint(listFitness)
print("\n")

#PROCESS PARENT SELECTION
print("this is the choosen Parents 1:")
parent1 = parentSelection.roulleteWheel(listFitness, populations)
status = False
while not status:                                                       #condition for parent2 chromosome not the same with chromosome parent1
    parent2 = parentSelection.roulleteWheel(listFitness, populations)
    if parent1 != parent2:
        status = True
print("this is the choosen Parents 2:")
print(parent2)
print("\n")

#SUMMARY
print("SUMMARY GENERATION 1: \n")
merge=zip(populations, listPtype, listFitness)
print(tabulate(merge, headers =["Populations", "Phenotype(x, y)", "Fitness"]))
print("Highest Fitness:")
print(max(listFitness))
print("\n")

#PROCESS CHILD SELECTION
newChild=childSelection.recombination(parent1, parent2)

#PROCESS MUTATION
if random.uniform(0, 100) < prob:
    newChild[0] = childSelection.mutation(newChild[0])
    newChild[1] = childSelection.mutation(newChild[1])

print("CHILD:", newChild, "\n")

newGene = populations

#IF GENERATION 1 THE HIGHEST
bestFitness=max(listFitness)
indexMax=listFitness.index(bestFitness)
bestChromo=populations[indexMax]
bestPtype=listPtype[indexMax]
bestGene = 0
#LOOPING FOR NEXT GENERATION, and removed unnecessary print
for j in range(1, jumGenerasi):


    newGene = selectionSurvivor.steadyState(listFitness,newGene,newChild[0],newChild[1])
    
    #CLEARING list for new generation
    listFitness.clear()
    listSplit.clear()
    listPtype.clear()

    #calculation section
    for i in range(jumPops):
        listSplit.append(InitializationPop.splitter(newGene[i]))

    for i in range(jumPops):
        listPtype.append(representBinary.decodeChromo(rBx,rAx,rBy,rAy, listSplit[i][0], listSplit[i][1])) 

    for i in range(jumPops):
        listFitness.append(representBinary.calcFitness(listPtype[i][0], listPtype[i][1]))

    parent1 = parentSelection.roulleteWheel(listFitness, newGene)
    status = False
    while not status:                                                       #condition for parent2 chromosome not the same with chromosome parent1
        parent2 = parentSelection.roulleteWheel(listFitness, newGene)
        if parent1 != parent2:
            status = True

        #SUMMARY
    print("SUMMARY GENERATION ", j+1, ": \n")
    merge=zip(newGene, listPtype, listFitness)
    print(tabulate(merge, headers =["Populations", "Phenotype(x, y)", "Fitness"]))
    print("Highest Fitness:")
    print(max(listFitness))
    print("\n")
    
        #PROSES CHILD SELECTION
    newChild=childSelection.recombination(parent1, parent2)

    #PROCESS MUTATION
    if random.uniform(0, 100) < prob:
        newChild[0] = childSelection.mutation(newChild[0])
        newChild[1] = childSelection.mutation(newChild[1])
    
    print("CHILD:", newChild, "\n")

    #CHECKING THE HIGHEST
    if bestFitness < max(listFitness):
        bestFitness=max(listFitness)
        indexMax=listFitness.index(bestFitness)
        bestChromo=populations[indexMax]
        bestPtype=listPtype[indexMax]
        bestGene = j+1

print("Chromosome terbaik ialah di generasi: ", bestGene)
print("Chromosome: ", bestChromo)
print("Phenotype (x,y): ", bestPtype)
print("Fitness: ", bestFitness)
print("\n")

