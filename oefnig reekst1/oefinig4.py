Data = input("hoeveel gig heb je gebruikt")
Data = float(Data)
SMS = input("hoeveel smsen heb je gestuurt")
SMS = int(SMS)
Bel= input("hoe lang heeb je aan de telefoon gehangen ")
Bel = int(Bel)
Prijs = 15.0
def tevelldata(Data, Prijs) :
    Data = Data - 1.5
    Data = round(Data)
    Data = Data * 5
    Prijs = Prijs + Data
def teveelSMS(SMS, Prijs):
    SMS = SMS - 200 
    SMS = float(SMS)
    Prijs = Prijs + SMS
def teveelBel(Bel , Prijs):
    Bel = Bel - 150
    Bel = float(Bel)
    Prijs = Prijs + Bel

if Data < 1.5 and SMS < 200 and Bel < 150:
    print("nice")
elif Data < 1.5 and SMS > 200 and Bel > 150:
    tevelldata(Data, Prijs)
elif Data < 1.5 and SMS < 200 and Bel > 150:
    tevelldata(Data, Prijs)
    teveelSMS(SMS, Prijs)
elif Data < 1.5 and SMS < 200 and Bel < 150:
    tevelldata(Data, Prijs)
    teveelSMS(SMS, Prijs)
    teveelBel(Bel, Prijs)
elif Data > 1.5 and SMS < 200 and Bel < 150:
    teveelSMS(SMS, Prijs)
    teveelBel(Bel, Prijs)
elif Data > 1.5 and SMS > 200 and Bel < 150:
    teveelBel(Bel, Prijs)
else:
    teveelSMS(SMS, Prijs)
print(Prijs)