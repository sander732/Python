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
import math
def valtijd(hoogte, plaats):
    if plaats == 'aarde':
        valversnelling = 9.81
    elif plaats == 'maan':
        valversnelling = 1.62
    else:
        return("wij kennen die plaats niet")
    valtijd = math.pow(2*hoogte/valversnelling,0.5)
    return(valtijd)

hoogte=int(input('wat is de hoogte '))
plaats=input('op welke planeet laat je het vallen')
print(valtijd(hoogte, plaats))

    