def modular_exponentiation(a, n, m):
    result = 1
    a = a % m  # Aseguramos que la base esté dentro del módulo
    while n > 0:
        if n % 2 == 1:  # Si n es impar, multiplica por la base
            result = (result * a) % m
        a = (a * a) % m  # Eleva la base al cuadrado y aplica el módulo
        n //= 2  # Divide el exponente por 2
    return result

# Ejemplo de uso
assert modular_exponentiation(3, 13, 7) == 3 ** 13 % 7
