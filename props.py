import pandas as pd
import datetime

# set close date cutoff
CLOSE_DATE = pd.Timestamp(datetime.date(2020, 1, 31))

# input file
IN_FILE = 'Leads and opportunities_FY20-21.xlsx';
IN_TAB = 'CRM report'

OUTFILE = 'output-' + CLOSE_DATE.strftime("%d-%b-%Y") + '.xlsx'
HT_SUMMARY_HEADER = ['product-group', 'order-booking-value', 'number-of-orders']
INDI_SUMMARY_HEADER = ['person', 'product-group', 'number-of-orders', 'total-revenue', 'total-leads']