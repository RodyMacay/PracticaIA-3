def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)
    else:
        return 0

def ejecutar_pertenencia():
    temperatura = 25
    grado = triangular(temperatura, 15, 25, 35)
    print(f"Grado de pertenencia de {temperatura}°C a 'cálida': {grado:.2f}")

if __name__ == "__main__":
    ejecutar_pertenencia()
