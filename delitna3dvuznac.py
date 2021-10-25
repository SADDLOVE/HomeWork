#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая получает на вход неизвестное количество целых числа и определяет количество двузначных чисел которые делаятся на 3
a = list(map(int, input("Введите числа ").split()))
c = 0
def skolko_znakov(n):
    i1 = 0
    n = abs(n)
    while n > 0:
        n = n // 10
        i1 += 1
    return i1
for i in range(len(a)):
    if a[i] == 0:
        break
    if a[i] % 3 == 0 and skolko_znakov(a[i]) == 2:
        c += 1
print(c) 
