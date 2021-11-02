import math
import random as rnd 

print('1. feladat:')
v = input('   írj be egy szót: ')
n = int(input('   írj be egy számot: '))
print('   ' + f'{v} ' * n)

print('2. feladat:')
print('   Add meg egy háromszög három oldalának hosszát cm-ben:')
a = int(input('   a = '))
b = int(input('   b = '))
c = int(input('   c = '))

if a + b <= c or a + c <= b or b + c <= a:
  print(f'   Ilyen háromszög nem szerkeszthető!')
else:
  s = (a + b + c) / 2
  t = math.sqrt(s * ((s - a) * (s- b) * (s - c)))
  print(f'   A háromszög területe: {t} cm^2')

print('3. feladat:')
print('   Add meg a tanuló következő adatait:')
nev = input('   név: ')
max_pont = int(input('   maximális pontszám: '))
akt_pont = int(input('   elért pontszám: '))

if akt_pont > max_pont:
  print('   Hibás adatokat adhattál meg, az elért pontszám nem lehet nagyobb, mint a maximális!')
else:
  szazalek = akt_pont / max_pont * 100
  if   szazalek < 51: print(f'   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: elégtelen')
  elif szazalek < 65: print(f'   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: elégséges')
  elif szazalek < 77: print(f'   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: közepes')
  elif szazalek < 90: print(f'   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: jó')
  else:               print(f'   {nev} {szazalek}%-ot ért el a dolgozaton, osztályzata: jeles')

print('4. feladat:')
talalat = 0
for f in range(1, 6):
  print(f'   {f}. kör:')
  x = rnd.randrange(10, 100)
  y = rnd.randrange(10, 100)
  if y > x: x, y = y, x
  print(f'     a két szám összege {x + y}, különbsége {x - y}. Mi lehet ez a két szám?')
  tx = int(input('       egyik szám: '))
  ty = int(input('       másik szám: '))
  if ty > tx: tx, ty = ty, tx
  if x == tx and y == ty:
    print('     helyes!')
    talalat += 1
  else:
    print(f'     sajnos nem, a válasz {x} és {y}')
print(f'   Végeztünk, helyes találataid száma: {talalat}')