#!/usr/bin/python3
def element_at(my_list, idx):
	count = len(my_list)
	if idx < 0 or idx >= count:
		return ('None')
	else:
		return my_list[idx]
