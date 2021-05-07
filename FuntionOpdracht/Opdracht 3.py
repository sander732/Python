"""
Opdracht 3 :
Schrijf de functie zinbevat(zin, woord)
    Als de zin het woord bevat is het resultaat True, anders false.
    Tip 
        gebruik woorden = zin.split(“ “) om de zin te splitsen in een reeks woorden.
        gebruik for localwoord in range(woorden)
        >>>zinbevat("Python is gemakkelijk", "gemakkelijk")
        True
        >>>zinbevat("Python is gemakkelijk", "moeilijk")
        False
"""

def zinbevat(zin, woord):
    woorden = zin.split(zin)
    andwoord = False

    for woord in woorden:
        andwoord = True
    return andwoord


zin=input("geef een zin op.")
woord=input("Geef een woord op.")
print(zinbevat(zin, woord))