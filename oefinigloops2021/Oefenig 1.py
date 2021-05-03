"""
Oefening 1
Maak een teller van 1 tem 10. Maak de oefening 2 keer zowel met een gewone while-loop,
als met een for-loop met de range functie.
Print telkens de waarde van de teller uit tijdens de loop en ook
de waarde na de loop als dit mogelijk is (scope).
"""
print("Oefening1")
print("Gewone while loop")
nrwhile =0
while nrwhile <  10:
    nrwhile +=1
    print(nrwhile)
print('na de loop is het numer', nrwhile)
print("for loop en range functie")
nrfor = 0
for nrfor in range(0 , 10):
    nrfor += 1
    print(nrfor)
print('na de loop is het numer', nrfor)


