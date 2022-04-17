# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.


import random



def gen_list(size, of, to):
    numbers= []
    i = 0
    while i < size:
        number = random.randint(of, to)
        numbers.append(number)
        i += 1
    return numbers

print (gen_list(5,3,20))

