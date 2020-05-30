import time
import datetime
import numpy as np
import pandas as pd
from pandas import ExcelWriter
pd.options.mode.chained_assignment = None  # default='warn'

# import code from other files
import props as props
import helper as hp
import individual as indi
import groups as gp
import sales_performance as sfp

if __name__ == '__main__':
	start = time.time()
	print('Execution started...')
	# read data into dataframe
	xls = pd.ExcelFile(props.IN_FILE)
	crmdf = pd.read_excel(xls, props.IN_TAB)
	
	# ht summary report
	ht_sum_df = gp.ht_summary(crmdf) # groups.py
	# individual summary
	indi_sum_df = indi.indi_summary(crmdf) # individual.py
	# sales funnel and performnce calculation for individuals
	sfp_df = sfp.sales_funnel_performance_data(crmdf) # sales-performance.py

	# save data to file
	writer = ExcelWriter(props.OUTFILE)
	ht_sum_df.to_excel(writer, 'product-group', index=False)
	indi_sum_df.to_excel(writer, 'individual', index=False)
	sfp_df.to_excel(writer, 'sales-funnel-performance', index=False)
	writer.save()

	print('Results saved to', props.OUTFILE)
	# calculate execution time
	end = time.time()
	print('Execution finished in',str(round(end - start,2)),'secs')