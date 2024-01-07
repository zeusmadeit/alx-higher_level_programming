#!/usr/bin/python3
def no_c(my_string):
	for el in range(0, len(my_string)):
		if my_string[el] == 'c' or my_string[el] == 'C':
			my_string[el] = ''
	return my_string
