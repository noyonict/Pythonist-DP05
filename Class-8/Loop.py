

# help('range')

# for a in range(4):
#     print(a**2)


# for a in range(0,40):
#     print(a**2)


# for a in range(4,40,3):
#     print(a**2)


# for a in range(4,40,3):
#     print(a+2)


# even number

# for i in range(2,51,2):
#     print(i)

# for a in range(0,20):
#     if a%2==0:
#         print(a)



# code time check

# import time
#
# start_time=time.time()
# for i in range(2,100000,2):
#     pass
# end_time=time.time()
# print("Time Need 1: {}".format(end_time-start_time))
#
# start_time=time.time()
# for i in range(100000):
#     if i%2==0:
#      pass
# end_time=time.time()
# print("Time Need 2: {}".format(end_time-start_time))



# token check

# s='je kono string run hobe'
# for i in s:
#     if i.isspace():
#         print()
#     else:
#         print(i,end='')

# s='je kono string run hobe'
# for i in s:
#     if i ==' ':
#         print()
#     else:
#         print(i,end='')




# reversed string

# s='je kono string run hobe'
# for i in s[::-1]:
#     if i ==' ':
#         print()
#     else:
#
#         print(i,end='')




#word based reversed

# s='je kono string run hobe'
# l=[]
# word=' '
# for i in s:
#     if i.isspace():
#         l.append(word)
#         word=''
#
#     else:
#         word +=i
#
# l.append(word)
# l.reverse()
# # print(l)
# for item in l:
#  print(item)



# single line comment
# s='je kono string run hobe'
# l=[]
# word=' '
# for i in s.strip():
#     if i.isspace():
#         if "#" not in word:
#          l.append(word)
#          word=''
#
#     else:
#         word +=i
#
# # l.append(word)
# # l.reverse()
# print(l)


# problem 2 single comment
# s='je kono #string run hobe'
# l=s.split('#')
# print(l[0])


#multiple comment
# s='je kono string """ run """ hobe'
# l=s.split('"""')
# print(l[0].strip()+l[2])





# 0----9 and 15----20
# for a in range(20):
#     if a==10:
#      a+=6
#     print(a)



# for a in range(0,20):
#     if a not in range(10,15):
#      print(a)


l=list(range(21))
for i in l[10:16]:
    l.remove(i)
print(l)




















