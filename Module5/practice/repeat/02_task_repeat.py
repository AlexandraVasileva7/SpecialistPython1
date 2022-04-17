# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    number_first = number
    number_palin = 0
    while number != 0:
        digit = number % 10
        number_palin = number_palin * 10 + digit
        number = number // 10
    return  number_palin == number_first



print(palindrome(1231))
