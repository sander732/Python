import time
"""
Schrijf een programma dat het kwadraat van de getallen van 1 tot .. 
afdrukt door middel van while-lus.
Het programma stopt als het kwadraat groter is dan 1000;
Doe dit met een break;
"""
print("Oefening 4")
getal = 0
while True:
    getal += 1
    kwadraat = getal **2
    print("het kwadraat van ", getal , " is " , kwadraat)
    time.sleep( 0.5 )
    if kwadraat > 1000:
        break