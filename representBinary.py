# THIS CODE AUTHORED BY Panj0ule(RafiRizkya)
import math
def decodeChromo(rBx,rAx,rBy,rAy, chromoX, chromoY):
    sigma=0.0
    gX=0.0
    gY=0.0
    #sigma N:
    N=len(chromoX)
    for i in range(1, N+1):
        sigma=sigma+2**(-(i))
    #formula g:
    for i in range(N):
        gX=gX+chromoX[i]*(2**(-(i+1)))
        gY=gY+chromoY[i]*(2**(-(i+1)))
    #formula x:
    resultX=rBx+((rAx-rBx)/sigma)*gX
    resultY=rBy+((rAy-rBy)/sigma)*gY

    return[resultX, resultY]

def calcFitness(x, y):
    h=(math.sin(x**2)*math.sin(y**2))+(x+y)

    return h


