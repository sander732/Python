"""
Oefening 5
We moeten een aantal getallen kunnen ingeven. 
Van het aantal ingegeven getallen wordt de som berekent en weergegeven. 
De getallen die ingegeven worden zijn van het type int. 
De getallenreeks eindigt met de ingave van een negatief getal. 
Dit laatste negatief getal wordt niet bij de som geteld. 
Indien we als eerste een negatief getal ingeven, dan is de som = 0.
"""
print("Oefening 5")
som =0
loop= 1
nummers= []
getal = int(input('geef een getal '))
if getal < 0:
    loop = 0
    nummers.append(getal)
    print("gelieve niet als eerst getal een negatief nummer ingeven ")
else:
    nummers.append(getal)
    som += getal 
while loop == 1:
    getal = input('geef een getal "om te stoppen druk alleen enter in"')
    if getal == '':
        break
    else:
        getal= int(getal)
        nummers.append(getal)
        som += getal 

print("Som berekenen")
print("de som van deze getallen ", nummers, " is " ,som )