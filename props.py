import pandas as pd
import datetime

# set close date cutoff
CLOSE_DATE = pd.Timestamp(datetime.date(2020, 3, 31))

# creation date for sales funnel performance
CREATION_DATE = pd.Timestamp(datetime.date(2020, 4, 1))

# input file
IN_FILE = 'input/Leads and opportunities_FY20-21.xlsx' # 'sample-data-set.xlsx'
IN_TAB = 'CRM report' # 'Sheet1'

# which column to pick the revenue from
REVENUE_COL = 'Updated Revenue (Updated Revenue)' # 'New Amount (Opportunity Id)'

# purchase timeframe for sales funnel and performance report
UP_PURCH_COL = 'Updated Purchase Timeframe (Updated Updated Purchase Timeframe)'

OUTFILE = 'output-' + CLOSE_DATE.strftime("%d-%b-%Y") + '.xlsx'
HT_SUMMARY_HEADER = ['product-group', 'order-booking-value', 'number-of-orders']

# individual summary tab headers
INDI_SUMMARY_HEADER = ['person', 'product-group'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# sales funnel performance base data headers
SALES_FUNNEL_PERFORMANCE_HEADER = ['person', 'product-group', 'creation-date', 'quarter'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# start date breakdown for the quarters
QUARTERS = [
	pd.Timestamp(datetime.date(2020, 4, 1)) # 1st april
	, pd.Timestamp(datetime.date(2020, 7, 1)) # 1st july
	, pd.Timestamp(datetime.date(2020, 10, 1)) # 1st october 
	, pd.Timestamp(datetime.date(2021, 1, 1)) # 1st Jan next year
	, pd.Timestamp(datetime.date(2021, 4, 1)) # 1st april next year
]