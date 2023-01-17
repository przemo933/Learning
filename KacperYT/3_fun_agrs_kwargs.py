def policz_wyplate(podstawa, premia_rzadu=0, premia_klienta=0, inwestycja=0):
    return podstawa + premia_rzadu + premia_klienta + inwestycja

print('WYPLATA')
pensja = policz_wyplate(1000, 500)
print(pensja)

pensja = policz_wyplate(inwestycja=2000, podstawa=500)
print(pensja)

#args przyjmuje rozne wartosci, zwraca jako tuple niemutowalne
def policz_srednia(*args):
    return sum(args) / len(args)


print('SREDNIA')
print(policz_srednia(2, 4))
print(policz_srednia(4, 5, 10, 23, 55))

#kwargs przyjmuje dane jako slownik
def wypisz_informacje(**kwargs):
    for klucz in kwargs:
        print(f' Pod kluczem {klucz} znajduje sie {kwargs[klucz]}')

        
print('KWARGS')
wypisz_informacje(imie='Przemek', nazwisko='Sobieraj', wiek=29)
