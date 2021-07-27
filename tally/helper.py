import pandas as pd
import props
import datetime
from datetime import date

# calculate the quarter in which a date falls
def get_quarter(tallydate):
	
	# check before first quarter
	if tallydate < props.QUARTERS[0]:
		return 'Before-Q1' 

	# iterate over the quarters
	for i in range(1,len(props.QUARTERS)):
		
		# start and end for that quarter
		start = props.QUARTERS[i - 1]
		end = props.QUARTERS[i]
		# check if in that quarter
		if tallydate >= start and tallydate < end:
			return ('Q' + str(i))
		
	# next FY
	return 'NEXT-FY'

# calculate before or after using the voucher number
def get_before_after_fy(voucher):
	# remove spaces
	voucher = voucher.replace(" ", "")
	year = voucher[5:7] 
	#print(voucher, year)
	if year == '21':
		return ('after-' + props.FY_START_DATE.strftime("%d-%b-%Y"))
	else:
		return ('before-' + props.FY_START_DATE.strftime("%d-%b-%Y"))