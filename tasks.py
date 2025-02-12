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
# Task 2
def sekimo_dekoratorius(funkcija):
    def wrapper (*args, **kwargs):
        print(f'Vykdoma funkcija')
        res = funkcija(*args, **kwargs)
        print(f'Funkcija baigta')
        return res
    return wrapper

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return 'dalyba is nulio negalima'
    return a / b

print(dauginti(2,1))
print(dalinti(4,1))
# Task 3
class SkaiciuSekosIteratorius:
    def __init__(self, pradinis, galinis):
        self.skaiciai = list(range(pradinis, galinis+1,2))

    def __iter__(self):
        return iter(self.skaiciai)

    def atgaline_seka(self):
        return iter(self.skaiciai[::-1])

iteratorius = SkaiciuSekosIteratorius(1, 10)
for skaicius in iteratorius:
    print(skaicius)

for skaicius in iteratorius.atgaline_seka():
    print(skaicius)
