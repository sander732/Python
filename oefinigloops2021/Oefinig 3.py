"""
De gebruiker geeft getallen in.
De ingegeven getallen kunnen zowel positief als negatief zijn.
Het programma stopt als de gebruiker Enter indrukt (lege string).
De output zal het aantal negatieve getallen, positieve getallen en
nul-getallen weergeven.
"""
print("Oefening3")
nummers= []
while True:
    getal = input('geef een getal "om te stoppen druk alleen enter in"')
    if getal == '':
        break
    else:
        getal= int(getal)
        nummers.append(getal)
def positiefnr(x):
    if x <0:
        return True
    else:
        return False
def negatiefnr(x):
    if x > 0:
        return True
    else:
        return False
def nulnr(x):
    if x == 0:
        return True
    else:
        return False
positiefnummer = filter(positiefnr, nummers)
negatiefnummer = filter(negatiefnr ,nummers)
nulnummer  = filter(nulnr, nummers)

positiefnummers=[]
negatiefnummers=[]
nulnummers=[]
for x in positiefnummer:
    positiefnummers.append(x)
for x in negatiefnummer:
    negatiefnummers.append(x)
for x in nulnummer:
    nulnummers.append(x)
print("aantal postiefnrs ", len(positiefnummers))
print("aantal negativenumers ", len(negatiefnummers))
print("aantal nul nummes ", len(nulnummers))