#Oefening Dictionary
def cleanLine(lijn):
    """
    Deze functie verwijdert leestekens en dergelijke uit een lijn.
    """
    lijn = lijn.replace(',', ' ')
    lijn = lijn.replace('.', ' ')
    lijn = lijn.replace('\n', ' ')
    lijn = lijn.replace('\t', ' ')
    lijn = lijn.replace('"', ' ')
    lijn = lijn.replace("'", ' ')
    lijn = lijn.replace('-', ' ')
    #Leestekens zijn vervangen door spaties 
    #   => nu nog de dubbele spaties verwijderen
    while True:
        lijn = lijn.replace('  ', ' ')
        dubbeleSpaties = lijn.count('  ')
        if dubbeleSpaties == 0:
            break
    #De lijn zonder leestekens returnen     
    return lijn

#Start hoofdprogramma
#TODO 1 het path aanpassen naar waar je python.txt gedownload hebt.
tekstFile = open("D:\\Mijn Drive\\schooljaar_2020-2021\\Python\\Code\\OpdrachtDictt\\python.txt", mode="r", encoding="utf-8")

woordDict = dict() #Een lege dictionary
while True:
    lijn = tekstFile.readline()
    #TODO 2 lijn omzetten in kleine letters
    
    lijn.lower()
    #TODO 3 als de lijn een lege String ('') is uit de loop gaan
    #    Een blanco lijn, midden het bestand is '\n', enkel na de laatste lijn krijg je ''
    if lijn == '' or lijn == '\n' :
        lijn = cleanLine(lijn)
    
    #TODO 4 de list woorden maken door de functie split(' ') toe te passen op lijn
    woorden = lijn.split(' ')

    #TODO 5 een loop maken over de list woorden en tellen
    #hoeveel keer elk woord in de dictionary woordDict voorkomt
    #Na de loop moet de dictionary woordDict voor elk woord weergeven
    #hoeveel keer het voorkomt in de tekst.
    frequetieDict = {}
    for woorden in lijn:
        if woorden in frequetieDict:
            aantal = frequetieDict[woorden]
        else:
            aantal = 0
        frequetieDict[woorden] = aantal + 1





print('Deze woorden komen meer dan 10 keer voor in de tekst.')
#TODO 6 De dictionary uitprinten
#ENKEL de woorden die meer dan tien keer voorkomen 
print()





#TODO 7 Het meest voorkomende woord uitprinten
#TODO 7.a Eerst het meest voorkomende zoeken door max van values te nemen
meeste = 0
print('Dit woord komt het meest voor in de tekst.')
#TODO 7.b. dan een loop over de dictionary maken om te printen
#    print enkel de woorden die meer dan 10 keer voorkomen.

print()
    
