# Oplossing 1
import math

def berekenOppCilinder(straal,hoogte):
    oppGrondvlakken = 2 * berekenOppCirkel(straal)
    print("oppgrondvlakken ",oppGrondvlakken)
    omtrekGrondvlak = 2 * math.pi * straal
    oppMantel = berekenOppRechthoek(omtrekGrondvlak,hoogte)
    print("oppMantel ",oppMantel)
    return(oppGrondvlakken + oppMantel)

def berekenOppRechthoek(lengte,breedte):
    return(lengte * breedte)

def berekenOppCirkel(straal):
    return(math.pi * straal * straal)

oppCilinder = berekenOppCilinder(3,6)
print("Een cilinder met straal 3dm en hoogte 6dm heeft als opp : ",oppCilinder,"dm²")

# Oplossing 2
import math
def oppCirkel(straal):
    return straal*straal*math.pi

def oppRechthoek(breedte,lengte):
    return lengte * breedte

def oppCilinder(hoogte,r):
    oppGrondvlakken = 2 * oppCirkel(r)
    oppMantel = oppRechthoek(hoogte,2*math.pi*r)
    return oppGrondvlakken + oppMantel

print("opp cilinder met straal 3 en hoogte 5 is",oppCilinder(5,3))
