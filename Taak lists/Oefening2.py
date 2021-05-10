import random


print("Oefening 2 : twister")


aantal=int(input('geef een aantal op'))


kleuren = ['rood', 'geel', 'groen', 'blauw']
legaamsdelen= ['linkerhand', 'rechterhand', 'linkervoet', 'rechtervoet']
henk=0
while henk < aantal:
    mcdoo=random.randint(0,3)
    kleur=kleuren[mcdoo]
    burgerking=random.randint(0, 3)
    legaamsdeel=legaamsdelen[burgerking]
    print('je ', legaamsdeel, 'moet naar ', kleur )
    henk +=1

#De functie uitvoeren


