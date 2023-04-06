##########
"""
Votre tâche est simple:
Trouver les deux premiers nombres premiers de plus d'1 million, dont la somme de leurs chiffres est aussi un nombre premier.
Par exemple 23 qui est premier, la somme de ses chiffres est 5 qui est aussi un nombre premier.
La solution est la concaténation des deux nombres,
Exemple: Si le premier nombre est 1 234 567
et le second 8 765 432,
Votre solution sera 12345678765432
"""
##########

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])

def is_prime_sum(n):
    return is_prime(sum_of_digits(n))

def find_prime_pair():
    i = 1000001
    while True:
        if is_prime(i) and is_prime_sum(i):
            j = i + 1
            while True:
                if is_prime(j) and is_prime_sum(j):
                    return int(str(i) + str(j))
                j += 1
        i += 1

print(find_prime_pair())