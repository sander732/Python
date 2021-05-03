import sys
getal1 = int(input("geef het een begin getal op "))
getal2 = int(input("geef het eid getal op "))

getal = getal1 

if getal1 < getal2:
    print("getal 1 moet kleiner zijn dan getal2")
    sys.exit()

getal2 = getal2 +1 

for getal in range(getal1 , getal2):
    getal3 = getal ** 2
    print('het kwadraat van ', getal ,' is ', getal3)
    getal = getal + 1
    
print('einde progame')