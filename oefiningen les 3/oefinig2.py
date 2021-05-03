test = 0
while test == 0:
    getal = int(input("geef een even getal"))
    if getal < 0:
        print("je getal mag niet kleiner zijn dan nul")
        continue
    if getal % 2 == 0:
        test= test + 1
    else:
        print("je getal is oneven ", getal)
print("je getal is even", getal)


