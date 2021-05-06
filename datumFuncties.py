"""
Voorbeeld function library
gebruik :
Methode 1: Run deze file in IDLE
Methode 2: Plaats deze file in het juist path (zie cursus)
		   import datumFuncties
		   datumFuncties.isSchrikkelJaar(2000)
		   of 
		   from datumFuncties import isSchrikkelJaar
		   isSchrikkelJaar(2000)
		   of 
		   from datumFuncties import *
		   isSchrikkelJaar(2000)
na import kan je ook dir(datumFuncties) doen om te zien welke functies erin zitten.
"""
def isSchrikkelJaar(jaar):
    if jaar % 400 == 0:
        return True
    if jaar % 100 == 0:
        return False
    return jaar % 4 == 0

def volgendJaar(jaar):
    return jaar + 1

    
