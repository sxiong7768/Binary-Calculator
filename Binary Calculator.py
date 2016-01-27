#----- Functions -----#
def decimal_to_binary(num):
	num = int(num)
	result = bin(num)
	return result[2:]

def binary_to_decimal(num):
	return int(num, 2)

def binary_checker(string):
	for x in string:
		if x != "1" and x != "0":
			print "You entered an invalid Binary Number."
			return False
	return True

def binary_checker_operations(string):
	for x in string:
		if x != "1" and x != "0":
			return False
	return True

def operation_checker(input):
	if operations.count(input) > 0:
		return True
	return False

def perform_calculation(input_equation):
	a = input_equation[0]
	b = input_equation[2]

	if input_equation[1] == "+":
		return a + b 
	elif input_equation[1] == "-":
		return a - b 
	elif input_equation[1] == "*":
		return a * b 
	elif input_equation[1] == "/":
		return a / b
	elif input_equation[1] == "<<":
		return a << b 
	else:
		return a >> b

#----- Start, Welcome Message -----#
does_continue = "yes"	# for to keep the calculator going
bin_check_array = ["0", "1"]
operations = ["+", "-", "*", "/", "<<", ">>"]

print "Welcome to my Binary Calculator"
print "-Type 'convert' to convert a binary to decimal or vice versa"
print "-Type 'calculate' to perform any calculations with binary values"

while does_continue == "yes" or does_continue == "y":
	perform = raw_input("\nWhat do you want me to help you with: convert or calculate?")

	# perform the conversion from binary to decimal or vice versa
	if perform == "convert":
		convert_continue = "y"
		while convert_continue == "y" or convert_continue == "yes":
			which_conversion = raw_input("Is your input binary or decimal?")
			# if the user wants to convert from binary into decimal
			if which_conversion == "binary":
				binary_continue = 0
				while binary_continue == 0:
					binary_num = raw_input("\nEnter your number: ")
					if binary_checker(binary_num):
						print "Your number in decimal is: " + str(binary_to_decimal(binary_num))
						binary_continue = 1
						convert_continue = raw_input("\nDo you wish to continue converting: yes(y) or no(n)?")
			#if the user wants to convert a decimal into a binary string
			elif which_conversion == "decimal":
				decimal_num = raw_input("\nEnter your number: ")
				binary_num = decimal_to_binary(decimal_num)
				print "Your number in binary is: " + str(binary_num)
				convert_continue = raw_input("\nDo you wish to continue converting: yes(y) or no(n)?")
			# else, print error message if invlaid input
			else:
				print "You entered an invalid option \n"
		does_continue = raw_input("Do you want to keep using this calculator: yes(y) or no(n)?")
		if does_continue == "n" or convert_continue == "no":
			print "Finished!"
	
	# perform computation given binary numbers
	# currently only able to handle single equations per calculation
	elif perform == "calculate":
		print "\nPerform any +, -, *, /, <<, or >> operations for two binary values"
		result = 0
		keep_prompting = 'y'
		while keep_prompting == 'y' or keep_prompting == "yes":
			_error = 0
			user_equation = raw_input("Please enter Binary Equation to compute: ")
			user_equation = user_equation.split()
			updated_equation = []
			# cycle through equation to convert to workable form
			for char in user_equation:
				# if there is any invalid inputs ie. decimal numbers and invalid operations
				if binary_checker_operations(char) == False and operation_checker(char) == False:
					print "Please enter a valid equation!"
					_error = 1
					break
				# check if the current string is binary
				elif operation_checker(char) == False and binary_checker_operations(char) == True:
					char = int(char, 2)
					updated_equation.append(char)
				# check if the current string is a operation
				elif operation_checker(char) == True and binary_checker_operations(char) == False:
					updated_equation.append(char)
				else:
					print "There is a error!"
					_error = 1
					break
			if _error == 0:
				result = perform_calculation(updated_equation)
				result = str(bin(result))
				print "Your equation: " + user_equation[0] + " " + user_equation[1] + " " + user_equation[2] + " = " + result[2:]
				keep_prompting = raw_input("\nDo you wish to continue solving equations: yes(y) or no(n)?")
				
		does_continue = raw_input("Do you want to keep using this calculator: yes(y) or no(n)?")
		if does_continue == "n" or convert_continue == "no":
			print "Finished!"

	# else return an error message on wrong input
	else:
		print "You entered an invalid option"
