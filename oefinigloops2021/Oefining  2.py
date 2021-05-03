"""
Oefening 2
De gebruiker geeft het aantal getallen in (aantal > 1) die hij wenst 
in te geven. 
Voer daarna een reeks getallen in. 
Bepaal het grootste getal in de rij. Gebruik geen List.
"""
print("Oefening2")

nietaantal = 0
nummers= []
aantal = int(input("hoeveel getalen wil je geven"))
while nietaantal < aantal:
    nietaantal +=1
    nummer=int(input("Geef een geheel getal"))
    nummers.append(nummer)
nummers.reverse()
print("Grootste getal")
print(nummers[0])
nummers.sort()
print("de nummers zijn, ", nummers)


"""
Oefening 2 bis
Zoals oefening2, maar in plaats van op voorhand het aantal 
getallen vragen, stoppen als de gebruiker 0 ingeeft.
"""
print("Oefening2 bis")
nietaantal = 0
nummers= []
aantal= 5
while nietaantal < aantal:
    nietaantal +=1
    nummer=int(input("Geef een geheel getal"))
    nummers.append(nummer)
nummers.reverse()
print("Grootste getal")
print(nummers[0])
nummers.sort()
print("de nummers zijn, ", nummers)