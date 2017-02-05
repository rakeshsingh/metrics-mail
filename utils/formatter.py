from prettytable import from_csv
''' format data files into different formats '''

def to_html_table(filepath, filetype='csv',**kwargs):
	table=None
	if filetype == 'csv':
		with open(filepath) as inputfile:
			table=from_csv(inputfile)
			table.format=True
		return table.get_html_string()
	else:
		pass

''' to ascii table '''
def to_ascii_table(filepath,filetype='csv', **kwargs):
	table=None
	if filetype == 'csv':
		with open(filepath) as inputfile:
			table=from_csv(inputfile)
			table.format=True
		return table
	else:
		pass
