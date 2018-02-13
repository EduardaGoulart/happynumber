"""
1. Dado um número inteiro positivo
2. Substitua o número pela soma dos quadrados dos seus dígitos
3. Se o resultado for 1, o número é feliz
4. Caso contrário, retira o processo infinitamente
"""

def happy(number):
    return number in (1, 7) if number < 10 else happy(sum(int(char) ** 2 for char in str(number)))


assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))