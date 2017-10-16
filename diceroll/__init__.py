"""
A dice expression parser

Author: Sam Clements <sam@borntyping.co.uk>

https://github.com/borntyping/diceroll
http://pypi.python.org/pypi/diceroll
"""
from __future__ import print_function
import sys

import pkg_resources

from diceroll.parser import roll, ParseException

__all__ = ['roll', 'ParseException']
__version__ = pkg_resources.require('diceroll')[0].version

def command ():
	""" Command line entry point """
	import sys, argparse
	parser = argparse.ArgumentParser(
        description="Return the results of a dice expression")
	
	parser.add_argument('--version', action='version',
		version='diceroll v%s' % __version__)
	
	parser.add_argument('-v', '--verbose', action='store_true',
		help='log the evaluation')
	
	parser.add_argument('expression', type=str,
		help='the expression to roll')
		
	args = parser.parse_args()
	
	try:
		result = roll(**vars(args))
		if args.verbose:
			print("Result:", result)
		else:
			print(result)
	except ParseException as exception:
		print("Parse failed:", exception, file=sys.stderr)

if __name__ == '__main__':
	command()
