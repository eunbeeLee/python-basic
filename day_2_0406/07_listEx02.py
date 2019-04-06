a = [1, 2]
b = [3, 4]
print(a+b)
a *= 3
print(a)

a[1] = 100
print(a)

a[2:4] = []
print(a)

a[0] = 50
print(a)

# del 함수
del a[1]
print(a)

#정렬
a.sort()
print(a)
a.reverse()
print(a)