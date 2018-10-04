"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

#from arithmetic import *
from arithmeticList import *

# Your code goes here

while True:
	input_string = input(">")
	tokens = input_string.split(" ")
	if tokens[0] == "q":
		break
	else:
		num_list = tokens[1:]
		try:
			for i in range(len(num_list)):
				num_list[i] = float(num_list[i])
			# num1 = float(tokens[1])
			# if len(tokens) > 2:
			# 	num2 = float(tokens[2])
			# pass
		except ValueError:
			print("Those are not numbers!")
			continue
		

		if tokens[0] == "+":
			answer = float(add(num_list))
			print(answer)
		elif tokens[0] == "-":
			answer = float(subtract(num_list))
			print(answer)
		elif tokens[0] == "*":
			answer = float(multiply(num_list))
			print(answer)
		elif tokens[0] == "/":
			answer = float(divide(num_list))
			print(answer)
		elif tokens[0] == "square":
			answer = square(num_list)
			print(answer)
		elif tokens[0] == "cube":
			answer = cube(num_list)
			print(answer)
		elif tokens[0] == "pow":
			if len(num_list)<2:
				print("Does not compute! Not enough numbers")
				continue
			answer = power(num_list)
			print(answer)
		elif tokens[0] == "mod":
			answer = mod(num_list)
			print(answer)
		else:
			print("Invalid Function")