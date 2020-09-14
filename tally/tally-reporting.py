import time
import datetime
import numpy as np
import pandas as pd
from pandas import ExcelWriter
pd.options.mode.chained_assignment = None  # default='warn'

# import code from other files
import props as props
import indi_orders as iorders
import indi_payments_due as ipaydue
import direct_cost as dc
import opening_debtors as od

# main driving function
def master():
	# init output file
	writer = ExcelWriter(props.OUTFILE)
	
	# read sales data
	salesdf = pd.read_excel(props.SALES, props.SALES_TAB)
	# read receivables data
	receivablesdf = pd.read_excel(props.RECEIVABLES, props.RECEIVABLES_TAB)
	# read stock data
	stockdf = pd.read_excel(props.STOCK, props.STOCK_TAB)
	
	# individual wise report + data extracted from sales and receivables
	results = iorders.individual_orders_bagged(salesdf)
	results.to_excel(writer, 'indi-orders-bagged', index=False) # indi_orders.py
	
	results = ipaydue.individual_payments_due(receivablesdf)
	results.to_excel(writer, 'indi-payments-due', index=False) # indi_payments_due.py

	# product wise report
	results = dc.get_direct_cost(stockdf)
	results.to_excel(writer, 'direct-cost', index=False) # direct_cost.py

	# opening debtors
	results = od.get_opening_debtors(receivablesdf)
	results.to_excel(writer, 'opening-debtors', index=False) # opening_debtors.py

	# write the base data to the results
	salesdf.to_excel(writer, 'sales-master', index=False) # sales base data
	receivablesdf.to_excel(writer, 'receivables-master', index=False) # receivables base data
	stockdf.to_excel(writer, 'stock-master', index=False) # stock base data

	# save results
	writer.save()
	print('Results saved to', props.OUTFILE)


if __name__ == '__main__':
	
	start = time.time()
	print('Execution started...')

	try:
		master()
	# exception
	except Exception as e:
		print('[ERROR] There was an issue with the execution:',e)
	
	# calculate execution time
	end = time.time()
	print('Execution finished in',str(round(end - start,2)),'secs')
	input('You can close this window now...')