List1 = [2, 3, 4, 5, 6, 91, 32, 21, 12, 0, 43, 0, 1, 2]
a, b, c = [12, 23, 43]
List1.extend([12, 34])
List1 += [12, 34]
List1.append(84)
List1.insert(0, 0)
print(List1.index(4))
List1.pop(6)

print(List1)
List1.remove(2)
print(List1)
print(List1[::-1])
List1.reverse()
print(List1)
print(a)
List2 = ['Name1', 'Name2', 'List', 'Nayem', 'Munna', 'Rafiq']
print(List1 + List2)
print(List2 + List1)
print('List1'.center(60, '*'))
# List1 = []
print('List1 =', List1)
# Ascending Order = []
List1.sort()
print('Ascending Order = ', List1)
# Descending Order = []
List1.reverse()  #List1.sort(reverse=True)
print('Descending Order =', List1)
print('List2'.center(60, '*') )
List1.clear()
print(List1)






