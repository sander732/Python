import datetime
#Dit programma vraagt mijn gegevens op en print ze af.

#Input : Gegevens verzamelen
naam = input('Wat is jouw naam: ')

#TODO woonplaats opvragen
woonplaats = input('Waar woon je?')

geboorteJaar = input('In welk jaar ben je geboren: ')
#De input functie geeft ALTIJD String terug
geboorteJaar = int(geboorteJaar) 

#TODO geboorteMaand en geboorteDag opvragen en omzetten naar int
geboorteMaand = input('in de hoeveelste maant ben je geboeren')
geboorteDag   = input('op welke dag ben je geboren')
geboorteMaand= int(geboorteMaand)
geboorteDag = int(geboorteDag)
#Process : Gegevens verwerken

#TODO Zoek op in https://www.w3schools.com/python/python_datetime.asp
#  hoe je een datetime Object kan maken.
Geboortedatum = datetime.datetime(geboorteJaar, geboorteMaand, geboorteDag)

#TODO Zoek op hoe je de huidige datum ophaalt
vandaag = datetime.datetime.now()

leeftijd= vandaag - Geboortedatum
dagen= leeftijd.days
print(dagen)
#TODO bereken jaren door dagen te delen door 365 (gehele deling)
#     bereken dagen door de rest van de deling van dagen gedeeld door 365
jaren = dagen//365
dagen = dagen % 365

#Output
print()
print('Hallo, ik ben', naam)
#TODO vervolledig zodat je dezelfde output krijgt als in de opgave.
print('Ik woon in', woonplaats)
print('Ik ben geboren op', Geboortedatum)
print('Ik ben nu', leeftijd)
print('Ik ben nu',jaren,'jaar en', dagen, 'dagen')