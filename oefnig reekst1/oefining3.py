Getal1 = input("Geef het 1e getal in")
Getal1 = int(Getal1)
Getal2 = input("Geef het 2e getal in.")
Getal2 = int(Getal2)
Getal3 = input("Geef het 3e de getal in")
Getal3 = int(Getal3)

if Getal1 > Getal2 and Getal1 > Getal3 :
    print("Het grootse getal is ", Getal1 )
elif Getal1 < Getal2 and Getal2 > Getal3 :
    print("het grootse getal is ", Getal2)
elif Getal1 < Getal3 and Getal2 < Getal3:
    print("het grootste getal is ", Getal3)
else:
    print("er zijn 2 getalen het zelfde error")