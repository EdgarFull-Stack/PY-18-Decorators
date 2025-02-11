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
# Example
class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None

    def change_employee_name(self, vardas):
        if not vardas:
            raise ValueError('Name is not provided')
        self.vardas = vardas

    @staticmethod
    def divide(a ,b):
        if b == b:
            raise ZeroDivisionError('Can not divide by zero')
        return a / b

    @classmethod
    def super_constructor(cls, vardas, pavarde, pareigos):
        return cls(vardas, pavarde, pareigos)

    @property
    def atlyginimas(self):
        return self.__atlyginimas

def registratorius(funkcija):
    print(f'Funkcija: {funkcija}')
    def apvalkalas(argumentas):
        print(f'Argumentas: {argumentas}: ')
        rezultatas = funkcija (argumentas)
        if rezultatas % 2 == 0:
            print(f'{rezultatas} yra lyginis')
        else:
            print(f'{rezultatas} yra nelyginis')
        return rezultatas
    return apvalkalas

@registratorius
def kvadratu(skaicius):
    return skaicius ** 2
print(kvadratu(8))
print('-'*40)
# Example
import time
def top_level_delay(seconds):
    def returner_of_delayed_func(func):
        def wrapper(*args, **kwargs):
            print(f'Function work will start after:{seconds}')
            time.sleep(seconds)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return returner_of_delayed_func

@top_level_delay(3)
def grazink500():
    return 500

@top_level_delay(5)
def vykdyk_aritmetika(skaicius1, skaicius2, veiksmas = None):
    if veiksmas == 'atimtis':
        return skaicius1 - skaicius2
res = grazink500()
print(res)
res = vykdyk_aritmetika(100,1, 'atimtis')
print(res)
