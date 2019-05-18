a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# commom_list = []

# for num in a:
#    if num in b:
#        if num not in commom_list:
#            commom_list.append(num)

#print(commom_list)

print(set(a) & set(b))
