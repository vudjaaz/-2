# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# n = int(input("Введите 1 набор чисел: "))
# n1 = []
# for i in range(n):
#     n1.append(int(input("Введите элементы множества: ")))

# m = int(input("Введите 2 набор чисел: "))
# m1 = []
# for i in range(m):
#     m1.append(int(input("Введите элементы множества: ")))

# s = set(n1)
# s1 = set(m1)

# sp = []
# for i in s:
#     if i in s1:
#         sp.append(i)
# print(sp)




# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# Пример
# 4 -> 1 2 3 4
# 9



n = int(input("Введите число кусток: "))
n1 = []
for i in range(n):
    n1.append(int(input("Введите урожойность куста: ")))
    
max = 0

for i in range(1,n-1):
    if (n1[i-1] + n1[i] + n1[i+1]) > max:
        max = n1[i-1] + n1[i] + n1[i+1]
print(max)


