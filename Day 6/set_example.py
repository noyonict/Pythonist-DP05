print('set'.center(60, '*'))
s1 = {1, 3, 2, 1, 5, 3, 6, 'String', 'Another String', False}
s2 = set()
s3 = set([12, 34, 45, 45])
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))

evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
a = {3, 5}
print(evens.intersection(primes))
print(odds.union(evens))
print(a.issubset(odds))
print(a.issuperset(odds))
print(a.difference(evens))
evens.update(a)
print(evens)
print(odds.symmetric_difference(a))
evens.remove(4)
print(evens)
evens.clear()
print(evens)





