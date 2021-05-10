"""
Oefening 1 : getallen
maak een lege List
vul via een loop de list op met 20 willekeurige getallen tussen 1 en 100, 
   gebruik daarvoor de functie random.randint(van, tot).
Bereken dan 
het gemiddelde van deze getallen, met integer division.
het kleinste van deze getallen.
het grootste van deze getallen.
Toon ook 
of het gemiddelde voorkomt in de lijst.
hoeveel getallen er kleiner zijn dan het gemiddelde.
hoeveel getallen er groter zijn dan het gemiddelde.
"""
import math
import random
print("Oefening 1 : getallen")
#De lijst met getallen maken
getallen = []
grooter= []
kleiner=[]
#TODO 1.1 de list getallen opvullen met 20 random getallen tussen 1 en 100
#
vis= 0
while vis < 20:
    getal=random.randint(1, 100)
    getallen.append(getal)
    vis += 1

print(getallen)
#het gemidelde van de getallen 
lang=len(getallen)
totaal=sum(getallen)
gemiddelde= totaal / lang
print(gemiddelde)
gemiddelde= int(gemiddelde)

testing=0
while testing < 20:
    test=getallen[testing]
    if test > gemiddelde:
        grooter.append(test)
    testing += 1
print(grooter)
testing=0
while testing < 20:
    test=getallen[testing]
    if test < gemiddelde:
        kleiner.append(test)
    testing += 1
print(kleiner)
print("er zijn ", len(grooter)," groter dan het gemiddelde en er zijn ", len(kleiner),' kleiner dan het gemiddelde het gemiddelde was ', gemiddelde)
getallen.sort()
print("het klienste getal is " ,getallen[0], " en het grootste getal ", getallen[-1])