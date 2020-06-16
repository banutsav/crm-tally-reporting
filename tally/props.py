# properties for tally reporting

import pandas as pd
import datetime

# output file
OUTFILE = 'tally-results.xlsx'

# input files

SALES = 'input/Sales.xlsx'
SALES_TAB = 'Sales Register'
RECEIVABLES = 'input/Receivables.xlsx'
RECEIVABLES_TAB = 'Bills Receivable'
STOCK = 'input/Stock.xlsx'

# start date breakdown for the quarters
QUARTERS = [
	pd.Timestamp(datetime.date(2020, 4, 1)) # 1st april
	, pd.Timestamp(datetime.date(2020, 7, 1)) # 1st july
	, pd.Timestamp(datetime.date(2020, 10, 1)) # 1st october 
	, pd.Timestamp(datetime.date(2021, 1, 1)) # 1st Jan next year
	, pd.Timestamp(datetime.date(2021, 4, 1)) # 1st april next year
]

# indi_orders.py
INDI_ORDER_BAGGED_HEADER = ['person', 'product-group', 'gross-total', 'date', 'quarter']
# indi_payments_due.py
INDI_PAYMENTS_DUE_HEADER = ['person', 'product-group', 'payments-due', 'date', 'quarter']

# columns
RECEIVABLES_DATE = 'Date'