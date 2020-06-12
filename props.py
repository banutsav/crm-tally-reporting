import pandas as pd
import datetime

# set close date cutoff
CLOSE_DATE = pd.Timestamp(datetime.date(2020, 1, 1)) #datetime.date(2020, 3, 31)

# creation date for sales funnel performance
CREATION_DATE = pd.Timestamp(datetime.date(2020, 1, 1)) #datetime.date(2020, 4, 1)

# input file
IN_FILE = 'input/sample-set-rv-1.xlsx' # 'Leads and opportunities_FY20-21, sample-data-set.xlsx, sample-set-rv-1
IN_TAB = 'Revised Sample set_2620' # 'CRM report, Sheet1, Revised Sample set_2620'
PROPERTIES_FILE = 'input/properties.xlsx'

DATE_TAB = 'biweek' # properties file for biweekly dates

# which column to pick the revenue from
REVENUE_COL = 'New Amount (Opportunity Id)' # 'New Amount (Opportunity Id), Updated Revenue (Updated Revenue)'

# purchase timeframe for sales funnel and performance report
UP_PURCH_COL = 'Updated Purchase Timeframe (Updated Updated Purchase Timeframe)'

# date on which lead is created, used in indi-biweek
CREATED_ON_COL = 'Created On'

# contract close date, used in po-won-biweekly
CLOSE_DATE_COL = 'Actual Close Date - autogenerated (Opportunity Id)'

OUTFILE = 'results.xlsx' #'output-' + CLOSE_DATE.strftime("%d-%b-%Y") + '.xlsx'
HT_SUMMARY_HEADER = ['product-group', 'order-booking-value', 'number-of-orders', 'order-ids']

# individual summary tab headers
INDI_SUMMARY_HEADER = ['person', 'product-group'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# sales funnel performance base data headers
SALES_FUNNEL_PERFORMANCE_HEADER = ['person', 'product-group', 'creation-date', 'quarter', 'start', 'end'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# revenue organized in quarters  for product groups
GROUP_SALES_FUNNEL_HEADER = ['product-group', 'creation-date','quarter', 'start', 'end', 'order-booking-value', 'number-of-orders', 'order-ids']

# start date breakdown for the quarters
QUARTERS = [
	pd.Timestamp(datetime.date(2019, 4, 1)) # 1st april
	, pd.Timestamp(datetime.date(2019, 7, 1)) # 1st july
	, pd.Timestamp(datetime.date(2019, 10, 1)) # 1st october 
	, pd.Timestamp(datetime.date(2020, 1, 1)) # 1st Jan next year
	, pd.Timestamp(datetime.date(2020, 4, 1)) # 1st april next year
]


# biweekly lead creation report header
BIWEEKLY_PERFORMANCE_HEADER = ['person', 'product-group', 'start-date', 'end-date', 'week-number'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# leads_product_biweekly.py
GROUP_PERFORMANCE_BIWEEKLY = ['product-group', 'start-date', 'end-date', 'week-number', 'order-booking-value', 'number-of-orders', 'order-ids']
