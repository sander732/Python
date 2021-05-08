"""
Opdracht 5 :
Schrijf de functie kwadraat(van, tot)
output :
>>>kwadraat(1, 4)
1 *                 #kwadraat van 1 = 1*1 = 1 => 1  ster printen
2 ****              #kwadraat van 2 = 2*2 = 4 => 4  sterren printen
3 *********         #kwadraat van 3 = 3*3 = 9 => 9  sterren printen
4 ****************
"""
import math

def kwadraat(van, tot):
    andwoord=math.pow(van,tot)
    return(andwoord)

x=int(input("geef een getal op"))
y=int(input("geef nog een getal op"))
print(kwadraat(x, y))