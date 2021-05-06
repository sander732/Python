def vraagint(prompt):
    while True:
        try:
            print(prompt, end = "")
            getal =input()
            intGetal = int(getal)
            return intGetal
        except:
            print(getal, "is geen getal")

vraagint("geef en getal : ")