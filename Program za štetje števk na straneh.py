

from msilib.schema import _Validation_records
from re import T


def števke(strani):
    rezultat=0
    for i in range(1, strani):
        a = len(str(i))
        rezultat =+ a
    print(rezultat)


def meni():
    print('Dobrodošli!')
    print('Vpišite število strani prosim.')
    vnos = print(input('Strani: '))
    števke(str(vnos))

meni()