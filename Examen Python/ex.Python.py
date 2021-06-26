#5
def ggd (a, b):
    kleinste = min(a,b)
    for deler in range(1, kleinste+ 1):
        if ((a % deler == 0)) and (b % deler == 0):
            ggd = deler
            return ggd 

print(ggd(12, 60))


#oefinig 7
voorraad2 = {'ringmap 4A': {'school1':74 , 'school2': 64},'Cursusblok gelijnd': {'school1': 45, 'school2': 60}, 'cursusblok geruit': {'school1':70 , 'school2': 68}}
aantalProducten=len(voorraad2)
print(aantalProducten)








#oefining 10 
steden = {"Gent": 337914, "Brugge":131589, "Brussel":1381011,"Antwerpen":689902 }
formatstring = ("De stad {} heeft {} inwoners")
for stad, inwoners in steden.items():
    print(formatstring.format(stad, inwoners))