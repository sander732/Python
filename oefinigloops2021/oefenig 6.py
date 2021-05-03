"""
Oefening 6
We delen 2 getallen, deeltal en deler, elk van het type int,
door elkaar zonder gebruik te maken van de deeloperatoren (/ %).
Hierbij nemen we wel aan dat deler > 0.
Als resultaat worden 2 zaken weergegeven, nl. het quotient 
en de rest van de deling.
"""
print("Oefening 6")
print("Geef deel tal en deler in zonder / als deeteken (gescheiden door een enter)")
deeltal=int(input())
deler=int(input())
quotient=0
print("De bewerking is {0}/{1}".format(deeltal,deler))
while deeltal >= deler:
    deeltal -= deler
    quotient +=1
print("uitkomst is ", quotient)
print("de rest is ", deeltal)