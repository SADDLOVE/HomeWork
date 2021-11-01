# Словарь с именем и возрастом
a = list(map(str,input().split()))
b = list(map(int,input().split()))
c = {}
if len(a) != len(b):
    print("Списки имеют разную длину \n")
else:
    c = dict((list(zip(a,b))))
print(c)