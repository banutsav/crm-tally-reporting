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

# calculate before or after current FY start
def get_before_after_fy(tallydate):
	if tallydate >= props.FY_START_DATE:
		return ('after-' + props.FY_START_DATE.strftime("%d-%b-%Y"))
	return ('before-' + props.FY_START_DATE.strftime("%d-%b-%Y"))	