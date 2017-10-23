# Palindrome Number
# name="121"
#
# if name[::-1]==name:
#    print('{} is a palindrome.'.format(name))
#    # print(name,'is a palindrome')
# else:
#     print('{} is not a palindrome.'.format(name))


# *****
# *****
# *****
# *****

# a=input('value :')
# for i in range(a):
#     print('******')



# a=int(input('value :'))
# for i in range(a):
#     for b in range(a):
#      print('*',end='')
#     print()


 # *
 # **
 # ***
 # ****



# a=int(input('value :'))
# for i in range(1,a+1):
#     for b in range(i):
#      print('*',end='')
#     print()


 # *
 # ***
 # *****


# a=int(input('value :'))
# for i in range(1,a+1,2):
#     for b in range(i):
#      print('*',end='')
#     print()






# ****
# ***
# **
# *


# a=int(input('value :'))
# for i in range(a,0,-1):
#     for b in range(i):
#      print('*',end='')
#     print()



#1
#22
#333
#4444
#55555


# a=int(input('value :'))
# for i in range(1,a+1):
#         for b in range(i):
#          print(i,end='')
#         print()




#1
#23
#123
#1231
#23123


# a=5
# count=1
# for line in range(1,a+1):
#         for star in range(line):
#          print(count,'',end='')
#          count +=1
#          if count==4:
#             count=1
#         print()


#3
#23
#321
#3213
#3123


a=5
count=3
for line in range(1,a+1):
        for star in range(line):
         print(count,'',end='')
         count -=1
         if count==0:
            count=3
        print()
