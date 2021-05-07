#Opdracht Functions1
"""
Opdracht 1 :
    Schrijf de functie afstand(x1, y1, x2, y2)
    De afstand tussen punt1 en punt2 is : ((x1-x2)^2 + (y1-y2)^2)^0.5
    x^y Betekent : x tot de macht y : 4^2 is 16.
    Gebruik import math en dan math.pow voor de machtverheffing.
"""
import math 
def afstand(x1,y1,x2,y2):
    x= x1-x2
    y= y1-y2
    y= math.pow(y, 2)
    x = math.pow(x,2)
    a = y+x
    a = math.pow(a, 0.5)
    return a

print(afstand(10,15,5,10))