list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.append(15)
print(list)
# list.sort()
list.insert(3, 14)
print(list)

list.reverse()
print(list)

list.remove(0)
print(list)

list.count(3)
print(list)

list.pop()
print(list)

list.pop(6)
print(list)


list.extend((5, 9 , 4, 3))  # adding multiple element at once
print(list)

list.extend([[55, 43, 11, 68]])
print(list)

list.clear()
print(list)