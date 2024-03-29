# properties for tally reporting

import pandas as pd
import datetime

# output file
OUTFILE = '/content/tally-results-'  + pd.Timestamp.now().strftime("%d-%m-%Y") + '.xlsx' # output file

# input files
INPUT_FOLDER = '/content' # 'input'

# start date breakdown for the quarters
QUARTERS = [
	pd.Timestamp(datetime.date(2021, 4, 1)) # 1st april
	, pd.Timestamp(datetime.date(2021, 7, 1)) # 1st july
	, pd.Timestamp(datetime.date(2021, 10, 1)) # 1st october 
	, pd.Timestamp(datetime.date(2022, 1, 1)) # 1st Jan next year
	, pd.Timestamp(datetime.date(2022, 4, 1)) # 1st april next year
]

# for order invoicing
FY_START_DATE = pd.Timestamp(datetime.date(2021, 4, 1)) # 1st april

# indi_orders.py
INDI_ORDER_BAGGED_HEADER = ['person', 'product-group', 'gross-total', 'date', 'quarter', 'invoiced-date', 'voucher-number']
# indi_payments_due.py
INDI_PAYMENTS_DUE_HEADER = ['person', 'product-group', 'payments-due', 'date', 'quarter', 'invoiced-date', 'reference-number']
# direct_cost.py
DIRECT_COST_HEADER = ['product', 'direct-cost', 'inventory-value']
# opening_debtors.py
OPENING_DEBTORS_HEADER = ['product', 'pending']

# columns
RECEIVABLES_DATE = 'Date'

# product groups not to be considered
NOT_PRODUCT_GROUPS = ['Lease', 'Treasury'] # indi_orders.py