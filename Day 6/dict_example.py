print(' dict '.center(60, '*'))
student1 = {
    'name': 'Python 3',
    'age': 11,
    'id': 11-21-21,
    'phone': '+88016 7839743',
    1 : 34
}
student1['add'] = 'Dhaka, Dangladesh'
student1['name'] = 'Python 2'
print(student1['name'])
print(student1.get('jfsl'))
print(student1.items())
print(student1.keys())
print(student1.values())

student1.popitem()
print(student1)
if not 'nme' in student1:
    student1.pop('name')
else:
    print('Name is not in student1')

print(student1)




