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
import random
getallen = []
nummers=[]
vis= 0
while True:
    while vis < 20:
        getal=random.randint(1, 40)
        getallen.append(getal)
        vis += 1
    mcdoo=int(input("geef een getal tussen 1 en 40  "))
    print(getallen)
    if mcdoo == 0:
        break
    if mcdoo < 0 or mcdoo > 40:
        print('error niet tussen 0 en 40')
        continue
    kip=0
    while kip < 20:
        test=getallen[kip]
        if test == mcdoo:
            nummers.append(test)
        kip += 1
    print(len(nummers))
    
