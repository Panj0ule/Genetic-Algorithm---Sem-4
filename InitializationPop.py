# THIS CODE AUTHORED BY Panj0ule(RafiRizkya)
import random
#initialize population
def initPop(jumChromo, jumPops):
    populations =([[random.randint(0,1) for x in range(jumChromo)] for i in range(jumPops)])
    print("jenis tipe data:", type(populations))

    return populations

def splitter(populations):
    split = len(populations) // 2
    return (populations[:split], populations[split:])



