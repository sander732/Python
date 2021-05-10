import random

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
print("Oefening 1 : getallen")
#De lijst met getallen maken
getallen = []
#TODO 1.1 de list getallen opvullen met 20 random getallen tussen 1 en 100
#...

print(getallen)    

#berekenen
som = 0
kleinste = getallen[0]
grootste = getallen[0]
#TODO 1.2 bereken de som, het kleinste en grootste
#for getal in getallen:
#   ...

#TODO 1.3 bereken het gemiddelde
gemiddelde = 0

print("Het gemiddelde getal is", gemiddelde)
print("Het kleinste getal is", kleinste)
print("Het grootste getal is", grootste)

#TODO 1.4 toon of het gemiddelde getal voorkomt in de list getallen


print("Oefening 2 : twister")
def twister(aantal):
    kleuren = ['rood', 'geel', 'groen', 'blauw']
    #TODO 2.1 plaats de lichaamsdelen in de list lichaamsdelen 
    #lichaamsdelen = ...
    for i in range(0, aantal):
        #TODO 2.2 kies een willekeurige kleur uit kleuren
        #TODO 2.3 kies een willekeurig lichaamsdeel uit lichaamsdelen
        #TODO 2.4 print de opdracht

#De functie uitvoeren
twister(10)        
print()

"""
Oefening 3 : getallenzoeker
maak een lege List getallenLijst
vul via een while loop de list op met 20 willekeurige getallen tussen 1 en 40, gebruik daarvoor de functie random.randint(van, tot).
In een while loop doe je het volgende :
Vraag de gebruiker een getal
Als het getal 0 is ga je uit de loop.
Als het getal niet tussen 1 en 40 ligt geef je een foutmelding en sla je de rest van de loop over.
Als het getal wel tussen 1 en 40 ligt geef je de volgende informatie:
Of het getal in getallenLijst voorkomt.
De index van het eerste element.
Hoeveel keer het getal in getallenlijst voorkomt.
"""
print("Oefening 3 : getallenzoeker")
