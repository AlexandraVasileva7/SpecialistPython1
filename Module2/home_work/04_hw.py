  
# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

a=int(input("введите число от 3 до 30: "))
number=1
    
if 2<a<=30:
    print("#"*a)
    while number<(a-1):
        print("#"," "*(a-4),"#")
        number=number+1
    print ("#"*a)    
else: 
    print("не верное число, попробуйте заново: ")
