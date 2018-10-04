"""Math functions for calculator."""

def add(num_list):
	"""Return the sum of all the numbers in the list"""
	#num_list = [a, b, c,...]
	total_sum = 0
	for num in num_list:
		total_sum += num

	return total_sum


def subtract(num_list):
	total_difference = num_list[0]
	for num in num_list[1:]:
		total_difference -= num

	return total_difference


def multiply(num_list):
	total_product = 1
	for num in num_list:
		total_product *= num

	return total_product


def divide(num_list):
	total_divide = num_list[0]
	for num in num_list[1:]:
		total_divide /= num

	return total_divide


def square(num_list):
	"""Returns a list of squared values"""
	squared_list = []
	for num in num_list:
		squared_list.append(num**2)

	return squared_list

def cube(num_list):
	cubed_list = []
	for num in num_list:
		cubed_list.append(num**3)

	return cubed_list

def power(num_list):
	power_list = []
	for i in range(len(num_list[:-1])):
		power_list.append(num_list[i]**num_list[i+1])

	return power_list


def mod(num_list):
	mod_list = []
	subset_length = len(num_list[1:])
	for i in range(1,subset_length+1):
		mod_list.append(num_list[0]%num_list[i])

	return mod_list