'''
  Lesson: Typecasting
  Author: Mikah Ho
  Date Created: Sept 23, 2024
  Date Last Modified: Sept 23, 2024
'''

def q1():
  #Write Assignment code here
  integer = input("Input an integer: ")
  integer = int(integer)
  integer = integer + 3
  print(integer)

def q2():
  #Write Assignment code here
  number = input("Input a number: ")
  number = str(number) + str(4)
  number = float(number)
  number = number + 2.0
  print(number)

def q3():
  #Write Assignment code here
  radius = input("Input a radius: ")
  radius = float(radius)
  area = 3.14 * radius * radius
  print(area)

def q4():
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  num = num * 12
  num = int(num)
  print(num)

def q5():
  #Write Assignment code here
  integer2 = input("Input an integer: ")
  integer2 = int(integer2)
  integer2 = integer2 + 5
  integer2 = str(integer2)
  print(f"Your number + 5 is {integer2}")

#Comment this code out when running tests
#Do not comment this out when running your program normally

q1()
q2()
q3()
q4()
q5()
