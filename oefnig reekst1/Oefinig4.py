Data = input("hoeveel gig heb je gebruikt")
Data = float(Data)
SMS = input("hoeveel smsen heb je gestuurt")
SMS = int(SMS)
Bel= input("hoe lang heeb je aan de telefoon gehangen ")
Bel = int(Bel)
Prijs = 15.0
Prijs = float(Prijs)

if Data < 1.5 and SMS < 200 and Bel < 150:
    print("nice")
if Data > 1.5:
    Data = Data - 1.5
    Data = round(Data)
    Data = Data * 5.0
    Prijs = Prijs + Data
if SMS > 200:
    SMS = SMS - 200 
    SMS = float(SMS)
    Prijs = Prijs + SMS
if Bel > 150:
    Bel = Bel - 150
    Bel = float(Bel)
    Prijs = Prijs + Bel
print(Prijs)