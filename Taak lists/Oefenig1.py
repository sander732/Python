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
import random
print("Oefening 1 : getallen")
#De lijst met getallen maken
getallen = []
#TODO 1.1 de list getallen opvullen met 20 random getallen tussen 1 en 100
#
vis= 0
while vis < 20:
    getal=random.randint(1, 100)
    getallen.append(getal)
    vis += 1

print(getallen)

