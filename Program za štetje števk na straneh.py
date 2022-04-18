
def števke(strani):
    rezultat=0
    for i in range(1, strani + 1):
        a = len(str(i))
        rezultat += a
    print(rezultat)


def meni():
    print('Dobrodošli!')
    print('Vpišite število strani prosim.')
    vnos = int(input('Strani: '))
    števke(vnos)

while True:
    meni()