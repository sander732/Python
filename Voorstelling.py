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
geboorteMaand = 8
geboorteDag   = 10

#Process : Gegevens verwerken

#TODO Zoek op in https://www.w3schools.com/python/python_datetime.asp
#  hoe je een datetime Object kan maken.
geboortedatum = None

#TODO Zoek op hoe je de huidige datum ophaalt
vandaag = datetime.datetime.now()

leeftijd = vandaag - geboortedatum
dagen = leeftijd.days
#TODO bereken jaren door dagen te delen door 365 (gehele deling)
#     bereken dagen door de rest van de deling van dagen gedeeld door 365
jaren = None
dagen = None

#Output
print()
print('Hallo, ik ben', naam)
#TODO vervolledig zodat je dezelfde output krijgt als in de opgave.
