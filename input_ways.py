# a=input('Enter your Name:')
# print("My Name is",a)
# print("My Name is",a,sep="-")
# print("My Name is",int(a))
# print("My Name is",float(a))
# print("My Name is"+' '+str(a))
# print("My Name is"+' '+a)

# a=int(input('Enter your Phone Number:'))
# print("your Phone Number is",a)
# print("your Phone Number is",a,sep=" ")
# print("your Phone Number is",int(a))
# print("your Phone Number is",float(a))
# print("your Phone Number is"+' '+str(a))

# a=float(input('Enter your BMI:'))
# print("your BMI is",a)
# print("your BMI is",a,sep=" ")
# print("your BMI is",int(a))
# print("your BMI is",float(a))
# print("your BMI is"+' '+str(a))

# name=input("Enter Your Name:")
# age=int(input("Enter Your Age:"))
# per=float(input("Enter your Graduation percentage:"))

# print(name,age,per)

# print(age,name,per)

# print(name,age,name)

# print(name)

# name=input("Enter Your Name:")
# age=int(input("Enter Your Age:"))
# per=float(input("Enter your Graduation percentage:"))

# print("Your Name is",name,"and age is",age, \
# "Gradution percentage is",per)

# print("Your Name is"+''+name,"and age is",age, \
# "Gradution percentage is",str(per)+'%')

# print("Your Name is %s and age is %d. \
# Gradution percentage is %.2f"%(name,age,per))

# print("Your Name is {} and age is {}. \
# Gradution percentage is {}".format(name,age,per))

# print("Your Name is {1} and age is {0}. \
# Gradution percentage is {2}".format(name,age,per))

# print(f"Your Name is {name} and age is {age}. \
# Gradution percentage is {per}%")

print(r'hello\nworld')

a=int(input())
b=int(input())
print(a+b)

a,b=[int(x) for x in input('Enter any two Numbers: ').split()]
print(a+b)

a=[float(x) for x in input().split(',')]
print(sum(a))

import math
a=[float(x) for x in input().split(',')]
print(math.prod(a))

x='1235465653'
print(int(x[0])+int(x[-1]))

x=input()
print(int(x[0])+int(x[-1]))