#calcolo del volume di una sfera

import math

def sfera(r):
	Vol = (4*(r**3*math.pi))/3
	return Vol

r= input ("Digitare il raggio: ")
r= int(r)

print(sfera(r))