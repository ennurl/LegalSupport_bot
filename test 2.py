# Проверка всех id
a =[]

b = []

for i in range(len(b)):
    if b[i] not in a:
        a.append(b[i])

print(len(a))
print('****************************')
print(a)