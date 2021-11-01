# Написать функцию сортирующую
a  = list(map(int, input().split(",")))
def sortirovka(a):
    for i in range(len(a)):
        minm = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minm]:
                minm = j
        a[minm], a[i] = a[i], a[minm] 
    print(a)    
sortirovka(a)