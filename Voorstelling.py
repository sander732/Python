import datetime
#Dit programma vraagt mijn gegevens op en print ze af.

#vraaft om je naam 
naam = input('Wat is jouw naam: ')

#vraagt waar je woont
woonplaats = input('Waar woon je?')

geboorteJaar = input('In welk jaar ben je geboren: ')
#De input functie geeft ALTIJD String terug
geboorteJaar = int(geboorteJaar) 
geboorteMaand = input('in de hoeveelste maant ben je geboeren')
geboorteDag   = input('op welke dag ben je geboren')
geboorteMaand= int(geboorteMaand)
geboorteDag = int(geboorteDag)
#Process : Gegevens verwerken

# https://www.w3schools.com/python/python_datetime.asp
# maakt een datum 
Geboortedatum = datetime.datetime(geboorteJaar, geboorteMaand, geboorteDag)

#haalt de dag vanvandaag op 
vandaag = datetime.datetime.now()

leeftijd= vandaag - Geboortedatum
dagen= leeftijd.days
print(dagen)
#doet wat wiskunde
jaren = dagen//365
dagen = dagen % 365

print()
print('Hallo, ik ben', naam)
#TODO vervolledig zodat je dezelfde output krijgt als in de opgave.
print('Ik woon in', woonplaats)
print('Ik ben geboren op', Geboortedatum)
print('Ik ben nu', leeftijd)
print('Ik ben nu',jaren,'jaar en', dagen, 'dagen')