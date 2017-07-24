
'''A module to test exceptions'''
import sys

def convert(s):
	'''Convert to integer'''
	x = -1
	try:
		x=int(s)
	except(ValueError,TypeError) as e:
		print("Conversion error: {} "\
			.format(str(e)),file=sys.stderr)
	return x