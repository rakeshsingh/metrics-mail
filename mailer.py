from __future__ import print_function 
from __future__ import unicode_literals
from builtins import input
import sys
from mm import formatter, publisher

''' mailer app '''
if __name__=='__main__':
	print('starting')
	if len(sys.argv) <1:
	 raise(Exception('Not Enough Arguments'))
	else:
		filepath=sys.argv[1]
		print(filepath)
		# cleanse file or throw error
		# transform file
		# apply filters
		# map columns 
		print('html version')
		print(formatter.to_html_table(filepath))
