#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def add(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Returns the difference of two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Returns the product of two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Returns the quotient of two numbers."""
  return num1 / num2

def power(num1, num2):
  """Returns the first number raised to the power of the second number."""
  return math.pow(num1, num2)

def square_root(num):
  """Returns the square root of a number."""
  return math.sqrt(num)

def exponential_function(num, exponent):
  """Returns the exponential function of a number and an exponent."""
  return math.exp(num * exponent)

def logarithmic_function(num, base):
  """Returns the logarithmic function of a number and a base."""
  return math.log(num, base)

def trigonometric_functions(angle):
  """Returns the sine, cosine, and tangent of an angle in degrees."""
  sine = math.sin(math.radians(angle))
  cosine = math.cos(math.radians(angle))
  tangent = math.tan(math.radians(angle))
  return sine, cosine, tangent

# Get the user's input.
operation = input("Enter an operation (+, -, *, /, pow, sqrt, exp, log, sin, cos, tan): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number (if applicable): "))

# Perform the operation based on the user's input.
if operation == "+":
  result = add(num1, num2)
elif operation == "-":
  result = subtract(num1, num2)
elif operation == "*":
  result = multiply(num1, num2)
elif operation == "/":
  result = divide(num1, num2)
elif operation == "pow":
  result = power(num1, num2)
elif operation == "sqrt":
  result = square_root(num1)
elif operation == "exp":
  result = exponential_function(num1, num2)
elif operation == "log":
  result = logarithmic_function(num1, num2)
elif operation == "sin":
  result = trigonometric_functions(num1)[0]
elif operation == "cos":
  result = trigonometric_functions(num1)[1]
elif operation == "tan":
  result = trigonometric_functions(num1)[2]
else:
  print("Invalid operation.")

# Print the result.
print(f"{num1} {operation} {num2} = {result}")


# In[ ]:




