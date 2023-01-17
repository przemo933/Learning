
#argument wejsciowy policz_preie to funkcja ktora wywolujemy wewnatrz funkcji policz_wyplate
def polcz_wyplate(podstawa, policz_premie):
    return podstawa +policz_premie(podstawa)

def zwroc_zero(podstawa):
    return 0

def policz_premie_managera(podstawa):
    return 0.5 * podstawa

print(polcz_wyplate(1000, zwroc_zero))
print(polcz_wyplate(2000, policz_premie_managera))
print(polcz_wyplate(3000, lambda x: 0.25 * x))

#LAMBDA
def suma(a, b):
    return a + b

suma2 = lambda a, b: a + b

wynik = suma(2, 5)
wynik2 = suma2(2, 5)
print(f'suma z funkcji wynosi {wynik} a z lambdy {wynik2}')