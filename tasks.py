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
def keli_apdorojimai(tekstas, *args):
    for func in args:
        tekstas = func(tekstas)
    return tekstas
print(keli_apdorojimai('LABAS', prideti_zenkliuka, apversti_teksta))
print('-'*40)
#  Task 2

def sekimo_dekoratorius(funkcija):
    def wrapper (*args, **kwargs):
        print(f'Vykdoma funkcija {funkcija}')
        res = funkcija(*args, **kwargs)
        print(f'Funkcija baigta')
        return res
    return wrapper

@sekimo_dekoratorius
def vykdyk_aritmetika(skaicius1, skaicius2, veiksmas = None):
    if veiksmas == 'dauginti':
        return skaicius1 * skaicius2
    if veiksmas == 'dalinti':
        if  skaicius2 == 0:
            raise ValueError ('Can not be divided by zero')
        return skaicius1 / skaicius2

print(vykdyk_aritmetika(3,4,'dauginti'))
print(vykdyk_aritmetika(8,4,'dalinti'))
print(vykdyk_aritmetika(1,2,'dalinti'))


