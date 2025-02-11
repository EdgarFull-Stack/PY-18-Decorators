# Example
def apversti_teksta(tekstas):
    return tekstas[::-1]

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])

print(apversti_teksta("ABC"))
print(apversti_sakini("Labas Pasauli Dabar!!!"))

def sudetinga_funkcija(func):
    for i in range(1, 10):
        print(func('Kartojantis 123 321'))

sudetinga_funkcija(apversti_sakini)

def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()
print(i_didziasias('labas', apversti_teksta))
print('-'*40)

