#Opdracht1 : Schrikkeljaren : Oplossing
#Input
jaar = int(input('Geef het jaartal : '))

#Verwerking
schrikkelJaar = False
#TODO test of jaar een scrikkeljaar is.
if jaar % 400 == 0:
    schrikkelJaar = True
elif jaar % 100 == 0:
    schrikkelJaar = False
elif jaar % 4 == 0:
    schrikkelJaar = True
else:
    schrikkelJaar = False
    
#Output
if schrikkelJaar:
    print(jaar, 'is een schrikkelJaar')
else:
    print(jaar, 'is geen schrikkelJaar')
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

#Opdracht2 : Leeftijd Hond : Oplossing
#Input
print('Geef de leeftijd van uw hond in jaren en maanden')
jaren   = int(input('jaren   : '))
maanden = int(input('maanden : '))

#Verwerking
hondMaanden = 12 * jaren + maanden
maandenInJaar1 = 0
maandenInJaar2 = 0
maandenInJaar3 = 0
if hondMaanden >= 24:
    maandenInJaar1 = 12
    maandenInJaar2 = 12
    maandenInJaar3 = hondMaanden - 24
elif hondMaanden >= 12:
    maandenInJaar1 = 12
    maandenInJaar2 = hondMaanden - 12
    #maandenInJaar3 = 0
else:    
    maandenInJaar1 = hondMaanden
    #maandenInJaar2 = 0
    #maandenInJaar3 = 0

totaalMaanden = maandenInJaar1 * 14 + maandenInJaar2 * 9 + maandenInJaar3 * 5
mensJaren     = totaalMaanden // 12
mensMaanden   = totaalMaanden % 12

#Output
print('De leeftijd van uw hond komt overeen met ',
      mensJaren, 'Jaar en ', mensMaanden, ' maanden')
