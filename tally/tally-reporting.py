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

if __name__ == '__main__':
	start = time.time()
	print('Execution started...')

	# init output file
	writer = ExcelWriter(props.OUTFILE)
	
	# read sales data
	salesdf = pd.read_excel(props.SALES, props.SALES_TAB)
	# read receivables data
	receivablesdf = pd.read_excel(props.RECEIVABLES, props.RECEIVABLES_TAB)
	# individual wise report
	results = iorders.individual_orders_bagged(salesdf)
	results.to_excel(writer, 'indi-orders-bagged', index=False) # indi_orders.py
	
	results = ipaydue.individual_payments_due(receivablesdf)
	results.to_excel(writer, 'indi-payments-due', index=False) # indi_payments_due.py

	# save results
	writer.save()
	print('Results saved to', props.OUTFILE)
	# calculate execution time
	end = time.time()
	print('Execution finished in',str(round(end - start,2)),'secs')