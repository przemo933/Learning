tekst = 'abcdefghijklmnopqrstuvwxy'

def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    licznik = 0
    for i in alphabet:
        if i not in sentence:
            licznik += 1
    if licznik > 0:
        return False
    return True



print(is_pangram(tekst))