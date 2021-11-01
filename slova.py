# Написать функцию которая принимает строчку и возвращает ее в нижнем рег
a = str(input())
def slova(a):
    B = []
    A = list(map(str, a.split()))
    [B.append(i.lower()) if not i.islower() else B.append(i) for i in A]
    print(B)
slova(a)