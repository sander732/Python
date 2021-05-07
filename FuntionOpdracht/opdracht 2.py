"""
Opdracht 2 :
    Schrijf de functie salaris(uren, wedde, overurenpercent)
    Geeft aan hoeveel de werkgever moet betalen : 
    minder of gelijk aan 8 uur is uren * wedde.
    meer dan dan 8 uur worden de eerste 8 uur gewoon betaald,
    de volgende uren wordt een overurenpercent extra betaald.
    voorbeeld : salaris(10, 20, 5) => 202
"""
def salaris(uren, wedde, overurenpercent):
    if uren < 8:
        overuren = uren -8
        uren = uren - overuren
        wedde = wedde* uren + (overuren * wedde * overurenpercent)
    else:
        wedde = wedde *uren
    return wedde
print(salaris(10,20,5))