# Напишите функцию которая возвращает нат.лог
import math
a = list(map(float, input().split()))
def natlog(a):
    for i in range(len(a)):
        if a[i] == 0 or a[i] < 0:
            a[i] = None
            continue
        a[i] = math.log(a[i])
    print(a)
natlog(a)
