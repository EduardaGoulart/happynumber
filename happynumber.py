"""
1. Dado um número inteiro positivo
2. Substitua o número pela soma dos quadrados dos seus dígitos
3. Se o resultado for 1, o número é feliz
4. Caso contrário, retira o processo infinitamente
"""

def sum_of_square(number):
    return sum(int(char) ** 2 for char in str(number))


def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_square(n)
    return n == 1


assert sum_of_square(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))