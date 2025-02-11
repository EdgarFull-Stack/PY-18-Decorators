# Task 1
def prideti_zenkliuka(tekstas):
    return tekstas + '*'
print(prideti_zenkliuka('Labas'))
def apversti_teksta(tekstas):
    return tekstas[::-1]
print(apversti_teksta('Labas'))
def apdoroti_teksta(tekstas,funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.lower()
print(apdoroti_teksta('Labas'))
def keli_apdorojimai(tekstas, *funkcijos):
    for func in funkcijos:
        tekstas = func(tekstas)
    return tekstas
print(keli_apdorojimai("LABAS", prideti_zenkliuka, apversti_teksta))
