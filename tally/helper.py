import pandas as pd
import props
import datetime
from datetime import date

# calculate the quarter in which a date falls
def get_quarter(tallydate):
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
	year = voucher[5:7]
	#print(voucher, year)
	if year == '20':
		return ('after-' + props.FY_START_DATE.strftime("%d-%b-%Y"))
	else:
		return ('before-' + props.FY_START_DATE.strftime("%d-%b-%Y"))

# get before or after based on the reference number
def get_before_after_ref_no(reference):
	# replace any spaces
	reference = reference.replace(" ", "")
	year = reference[5:7]
	#print(reference, year)
	if year == '20':
		return ('after-' + props.FY_START_DATE.strftime("%d-%b-%Y"))
	else:
		return ('before-' + props.FY_START_DATE.strftime("%d-%b-%Y"))
