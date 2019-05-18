a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for aa in a:
    dif = aa % 2
    if dif == 0:
        b.append(aa)

print(b)