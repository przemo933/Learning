from math import sqrt

def policz_dlugosc_odcinka(x1, x2, y1, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

print(policz_dlugosc_odcinka(2, 3, 5, 5))

#kword arguments
print(policz_dlugosc_odcinka(y2=5, y1=5, x2=3, x1=2))
