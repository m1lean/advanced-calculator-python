import math

# Функция для решения дискриминанта
def discriminant(a, b, c):
    return b*2 - 4ac

# Функция для нахождения корней
def find_roots(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        return None
    elif d == 0:
        return -b / (2a)
    else:
        x1 = (-b + math.sqrt(d)) / (2a)
        x2 = (-b - math.sqrt(d)) / (2a)
        return (x1, x2)

# Функция для сокращения дроби
def reduce_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Пример использования
a = 1
b = -5
c = 6

# Решаем дискриминант и выводим результат
d = discriminant(a, b, c)
print("Дискриминант:", d)

# Находим корни и выводим результат
roots = find_roots(a, b, c)
if roots is None:
    print("Нет корней")
elif isinstance(roots, float):
    print("Один корень:", roots)
else:
    print("Два корня:", roots)

# Сокращаем дробь и выводим результат
numerator = 6
denominator = 12
reduced = reduce_fraction(numerator, denominator)
print(f"Сокращенная дробь {numerator}/{denominator}: {reduced[0]}/{reduced[1]}")

# Вычисляем факториал и выводим результат
n = 5
fact = factorial(n)
print(f"{n}! = {fact}")
