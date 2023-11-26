#!/usr/bin/env python3

# Assignment 1

def admin_login(username, password):
  if username == "admin" or "ADMIN" and password == 12345:
    print("Acces granted")
  else:
    print("Acess denied")

admin_login("ADMIN", 12345)

# Assignment 2
def hows_the_weather(temp):
  if temp > 85:
    print ("It's too dang hot out there!")
  elif temp > 70:
    print ("It's pretty warm out there.")
  elif temp > 50:
    print ("It's pretty chilly out there.")
  elif temp > 30:
    print ("It's pretty cold out there.")
  else:
    print ("Brrr... it's freezing out there.")

hows_the_weather(15)


# Assignment 3
def fizzbuzz(num):
  if num % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)

fizzbuzz(50)

# Assignment 4

def calculator(oper, num1, num2):
  if oper == "+":
    return num1 + num2
  elif oper == "-":
    return num1 - num2
  elif oper == "*":
    return num1 * num2
  elif oper == "/":
    return num1 / num2
  else:
    print("Invalid operation")
    return None
print(calculator("nope", 5, 6))
