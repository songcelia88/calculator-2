"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
	input_string = input(">")
	tokens = input_string.split(" ")
	if tokens[0] == "q":
		break
	else:
		num1 = float(tokens[1])
		if len(tokens) > 2:
			num2 = float(tokens[2])

		if tokens[0] == "+":
			answer = float(add(num1, num2))
			print(answer)
		elif tokens[0] == "-":
			answer = float(subtract(num1, num2))
			print(answer)
		elif tokens[0] == "*":
			answer = float(multiply(num1, num2))
			print(answer)
		elif tokens[0] == "/":
			answer = float(divide(num1, num2))
			print(answer)
		elif tokens[0] == "square":
			answer = float(square(num1))
			print(answer)
		elif tokens[0] == "cube":
			answer = float(cube(num1))
			print(answer)
		elif tokens[0] == "pow":
			answer = float(power(num1, num2))
			print(answer)
		elif tokens[0] == "mod":
			answer = float(mod(num1, num2))
			print(answer)
		else:
			print("Invalid Function")