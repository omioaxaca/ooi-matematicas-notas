def binary_exponentiation(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  # Si n es impar, multiplica por la base
            result *= a
        a *= a  # Eleva la base al cuadrado
        n //= 2  # Divide el exponente por 2
    return result

# Ejemplo de uso
assert binary_exponentiation(3, 13) == 3 ** 13