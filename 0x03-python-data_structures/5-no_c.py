#!/usr/bin/python3
def no_c(my_string):
	new_str = ''
	for el in my_string:
		if el != 'c' and el != 'C':
			new_str += el
	return new_str
