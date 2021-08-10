import pandas as pd
import datetime

# set close date cutoff
CLOSE_DATE = pd.Timestamp(datetime.date(2021, 3, 31))

# creation date for sales funnel performance
CREATION_DATE = pd.Timestamp(datetime.date(2021, 4, 1))

# start date breakdown for the quarters
QUARTERS = [
	pd.Timestamp(datetime.date(2021, 4, 1)) # 1st april
	, pd.Timestamp(datetime.date(2021, 7, 1)) # 1st july
	, pd.Timestamp(datetime.date(2021, 10, 1)) # 1st october 
	, pd.Timestamp(datetime.date(2022, 1, 1)) # 1st Jan next year
	, pd.Timestamp(datetime.date(2022, 4, 1)) # 1st april next year
]

# input file
IN_FILE = '/content/data.xlsx' # 'Leads and opportunities_FY20-21, sample-data-set.xlsx, sample-set-rv-1
IN_TAB = 'sheet' # 'CRM report, Sheet1, Revised Sample set_2620'
PROPERTIES_FILE = '/content/input/properties.xlsx'
LOST_CASES_FILE = '/content/input/lost.xlsx'

DATE_TAB = 'biweek' # properties file for biweekly dates

PIPELINE_PHASES = ['Budgetary', 'FIRM', 'PQR'] # sales_funnel_pipeline.py

# pipeline phase column
PIPELINE_PHASE_COL = 'Pipeline Phase'

# which column to pick the revenue from
REVENUE_COL = 'Updated Revenue' # 'New Amount (Opportunity Id), Updated Revenue (Updated Revenue)'

# purchase timeframe for sales funnel and performance report
UP_PURCH_COL = 'Updated Purchase Timeframe'

# date on which lead is created, used in indi-biweek
CREATED_ON_COL = 'Created On'


# contract id field
CONTRACT_ID = 'Contract ID'

# contract close date, used in po-won-biweekly
CLOSE_DATE_COL = 'Actual Close Date'

# joint report offer id's like
JOINT_REPORT_OFFER_IDS = 'HT21'

OUTFILE = 'results-' + pd.Timestamp.now().strftime("%d-%m-%Y") + '.xlsx' # output file

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

# sales funnel performance base data with phase information headers
SALES_FUNNEL_PERFORMANCE_WITH_PHASE_HEADER = ['person', 'product-group', 'creation-date', 'quarter', 'start', 'end'
, 'phase', 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads','updated-purchase-timeframes'
]


# revenue organized in quarters  for product groups
GROUP_SALES_FUNNEL_HEADER = ['product-group', 'creation-date','quarter', 'start', 'end', 'order-booking-value', 'number-of-orders', 'order-ids']


# biweekly lead creation report header
BIWEEKLY_PERFORMANCE_HEADER = ['person', 'product-group', 'start-date', 'end-date', 'week-number'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads'
]

# leads_product_biweekly.py
GROUP_PERFORMANCE_BIWEEKLY = ['product-group', 'start-date', 'end-date', 'week-number', 'order-booking-value', 'number-of-orders', 'order-ids']

# expired leads
EXPIRED_LEADS_HEADER = ['person','product-group'
, 'orders-where-owner', 'order-ids-where-owner', 'total-revenue-where-owner', 'total-leads-where-owner'
,'orders-where-shared-1', 'order-ids-where-shared-1', 'total-revenue-where-shared-1', 'total-leads-where-shared-1'
, 'orders-where-shared-2', 'order-ids-where-shared-2', 'total-revenue-where-shared-2', 'total-leads-where-shared-2'
, 'total-revenue', 'total-leads']

# joint report
JOINT_REPORT_HEADER = ['offer-id', 'product-group', 'contract-no', 'opportunity-status', 'updated-revenue'
, 'agent-1', 'agent-2', 'agent-3', 'created-on', 'actual-close-date'
]