#!/usr/bin/python3
if __name__ == "__main__":
	import sys

	res = 0
	num = len(sys.argv) - 1
	if num == 1:
		print (res)
	elif num > 1:
		for i in range(num):
			res = res + int(sys.argv[i + 1])
	print ("{:d}".format(res))
