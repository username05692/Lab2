import math
def roz(x):
    if x<=0 or x>=1:
        print("Значення х має бути 0<х<1")
        return None
    else:    
        z=(math.pow(math.e, math.sqrt(x)))/math.sqrt(1-x)
        return z

x = float(input("Введіть значення x: "))
print ("Значення виразу z = ", roz(x))

from funk2 import obr

print("***********************")
N = int(input("Введіть значення N: "))    
print("Значення виразу N =", obr(N)) 
