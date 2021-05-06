#TODO gebruik de IO functies

#Opdracht Functions1
"""
Opdracht 1 :
    Schrijf de functie afstand(x1, y1, x2, y2)
    De afstand tussen punt1 en punt2 is : ((x1-x2)^2 + (y1-y2)^2)^0.5
    x^y Betekent : x tot de macht y : 4^2 is 16.
    Gebruik import math en dan math.pow voor de machtverheffing.
"""
#TODO

"""
Opdracht 2 :
    Schrijf de functie salaris(uren, wedde, overurenpercent)
    Geeft aan hoeveel de werkgever moet betalen : 
    minder of gelijk aan 8 uur is uren * wedde.
    meer dan dan 8 uur worden de eerste 8 uur gewoon betaald,
    de volgende uren wordt een overurenpercent extra betaald.
    voorbeeld : salaris(10, 20, 5) => 202
"""
#TODO

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
#TODO

"""
Opdracht 4 :
Schrijf de functie ggd(a, b)
De grootste gemene deler van twee getallen kan je als volgt vinden :
    Begin met deler = 1
    een loop zolang deler < min(a, b): (minimum)
	als a deelbaar door deler en b deelbaar door deler:
	      grootsteGemDeler = deler	 
        deler = deler +1
return grootsteGemDeler
"""
#TODO

"""
Opdracht 5 :
Schrijf de functie kwadraat(van, tot)
output :
>>>kwadraat(1, 4)
1 *                 #kwadraat van 1 = 1*1 = 1 => 1  ster printen
2 ****              #kwadraat van 2 = 2*2 = 4 => 4  sterren printen
3 *********         #kwadraat van 3 = 3*3 = 9 => 9  sterren printen
4 ****************
"""
#TODO
	
"""
Opdracht 6 :
Schrijf de valtijd(hoogte, valversnelling = 9.81)
De valversnelling is op aarde is 9.81 m/s^2 en op de maan is 1.62 m/s^2.
Bereken hoeveel seconden het duurt als een voorwerp vanaf een bepaald
hoogte in meters valt voor het de grond raakt.
valtijd(in sec) = vierkantswortel(2*hoogte(in m) / valversnelling)
vierkantswortel(x) = math.pow(x, 0.5)
parameter valversnelling heeft een default waarde.
"""
#TODO
	


