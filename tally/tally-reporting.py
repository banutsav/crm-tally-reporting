import sys, os
from os import listdir
from os.path import isfile, join
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

import sys, os
from os import listdir
from os.path import isfile, join
import time
import datetime
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# check files in input folder to construct sales, receivables and stock data frames
def construct_dataframes():
  # init the dataframe lists
  sales = []; receivables = []; stock = []
  
  mypath = props.INPUT_FOLDER
  print("Checking files under...", mypath)
  files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  
  # check files
  for file in files:
    # ignore if not an excel file
    if '.xls' not in file.lower():
      continue

		# construct dataframe from file
    filepath = mypath + '/' + file
    xls = pd.ExcelFile(filepath)
    df = pd.read_excel(xls, xls.sheet_names[0])
    
    # put into combined sales list
    filename = file.strip().lower()
    if 'sale' in filename:
      sales.append(df)
    elif 'receivable' in filename:
      receivables.append(df)
    elif 'stock' in filename:
      stock.append(df)
  
  # construct individual dataframes
  salesdf = pd.concat(sales)
  receivablesdf = pd.concat(receivables)
  stockdf = pd.concat(stock)
  
  return salesdf, receivablesdf, stockdf


# main driving function
def master(salesdf, receivablesdf, stockdf):
	
	# init output file
	writer = ExcelWriter(props.OUTFILE)
	
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
	salesdf, receivablesdf, stockdf = construct_dataframes()
	master(salesdf, receivablesdf, stockdf)

	# calculate execution time
	end = time.time()
	print('Execution finished in',str(round(end - start,2)),'secs')