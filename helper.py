import pandas as pd
import props
import datetime
from datetime import date

# revenue and lead calculation for individual based on lead sharing
def revenue_lead_individual(df):
	# init revenue and leads
	revenue = 0
	leads = 0

	# iterate across the data for one person and one product group
	for index, row in df.iterrows():
		
		# calculate sharing factor for this order
		factor = 1
		if pd.isnull(row['Shared to 1']) == False:
			factor += 1
		if pd.isnull(row['Shared to 2']) == False:
			factor += 1
		
		# add to total revenue and leads
		revenue += (row[props.REVENUE_COL] / factor)
		leads += (1 / factor)
		
		# DEBUG
		#print(row['Offer ID'], row['Product Category'], row['Owner'], row['Shared to 1'], row['Shared to 2'], factor)

	return revenue, leads

# get the next weekday from a date
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

# biweekly dates from a schedule of dates
def get_biweekly_dates_from_schedule():
	results = []
	# properties file
	properties = pd.ExcelFile(props.PROPERTIES_FILE)
	# biweekly dates
	bw_dates =  pd.read_excel(properties, props.DATE_TAB)
	# iterate across the biweekly dates
	for index, row in bw_dates.iterrows():
		results.append({'start': row['Start Date'], 'end': row['End Date'], 'slot': row['EM']})
	
	return results

# get a list of biweekly dates for this FY
def get_biweekly_dates():
	# get todays month
	this_month = date.today().month
	# set stopping month to one month from now
	next_month = this_month + 2
	# start from the creation date
	bw_date = next_weekday(props.CREATION_DATE, 5) # monday = 0
	# 2 weeks diff
	two_weeks = datetime.timedelta(weeks = 2)
	# init and populate resultset
	results = []
	while bw_date.month != next_month:
		results.append(bw_date)
		bw_date = bw_date + two_weeks
	return results

# construct dataframe based on records on a quarterly basis
def construct_quarterly_dataframe(person, cat, data, column, result, created):
	# iterate over the quarters
	for i in range(1,len(props.QUARTERS)):
		# start and end for that quarter
		start = props.QUARTERS[i - 1]
		end = props.QUARTERS[i]
		# get results for that quarter
		dfq = data.loc[(data[column] >= start) & (data[column] < end), :]
		obj = construct_person_record(person, cat, dfq) # helper.gs
		# set the quarter
		obj['quarter'] = 'Q' + str(i)
		obj['start'] = start
		obj['end'] = end - datetime.timedelta(days=1) # get end of that quarter
		obj['creation-date'] = created
		result = result.append(obj, ignore_index=True)
			
	# results beyond last quarter
	df_ny = data.loc[data[column] >= end, :]
	obj = construct_person_record(person, cat, df_ny) # helper.gs
	obj['quarter'] = 'NEXT-FY'
	obj['start'] = end
	obj['creation-date'] = created
	# append row to result
	result = result.append(obj, ignore_index=True)
	return result

# iterate across the biweekly dates and consruct the biweekly performance report
def construct_biweekly_df(person, cat, data, column, result, biweekly_dates):
	#bw_dates = get_biweekly_dates() DISCONTINUED
	
	# iterate across the biweekly dates
	for x in biweekly_dates:
		# get start and end for that bi-week
		start = x['start']
		end = x['end']
		# extract data from dataframe and construct row for that person
		df = data.loc[(data[column] >= start) & (data[column] <= end), :]
		obj = construct_person_record(person, cat, df) # helper.gs
		# set the start and end dates
		obj['start-date'] = start
		obj['end-date'] = end
		obj['week-number'] = x['slot']
		result = result.append(obj, ignore_index=True)

	return result

# get a single output row for a person and product category
def construct_person_record(person, cat, data):
	# split dataframes according to where person is owner, share to 1 or shared to 2
	df_1 = data.loc[data['Owner'] == person]
	df_2 = data.loc[data['Shared to 1'] == person]
	df_3 = data.loc[data['Shared to 2'] == person]

	# calculate revenue and leads where owner
	revenue_1, leads_1 = revenue_lead_individual(df_1) # helper.py 
	# calculate revenue and lead breakdown where first share
	revenue_2, leads_2 = revenue_lead_individual(df_2) # helper.py
	# calculate revenue and lead breakdown where second share
	revenue_3, leads_3 = revenue_lead_individual(df_3) # helper.py

	obj = {
	'person': person , 'product-group': cat
	# where person is owner
	, 'orders-where-owner': df_1.shape[0]
	, 'order-ids-where-owner': df_1['Offer ID'].tolist()
	, 'total-revenue-where-owner': revenue_1
	, 'total-leads-where-owner': leads_1
	# where person is shared to 1
	, 'orders-where-shared-1': df_2.shape[0]
	, 'order-ids-where-shared-1': df_2['Offer ID'].tolist()
	, 'total-revenue-where-shared-1': revenue_2
	, 'total-leads-where-shared-1': leads_2
	# where person is shared to 2
	, 'orders-where-shared-2': df_3.shape[0]
	, 'order-ids-where-shared-2': df_3['Offer ID'].tolist()
	, 'total-revenue-where-shared-2': revenue_3
	, 'total-leads-where-shared-2': leads_3
	# cumulative
	, 'total-revenue': revenue_1 + revenue_2 + revenue_3
	, 'total-leads': leads_1 + leads_2 + leads_3
	}

	return obj

# for one product group, group the revenue on a biweekly basis
def group_biweekly_revenue(data, cat,column, result, biweekly_dates):
	#bw_dates = get_biweekly_dates() DISCONTINUED
	
	# iterate across the biweekly dates
	for x in biweekly_dates:
		# get start and end for that bi-week
		start = x['start']
		end = x['end']
		# extract data from dataframe and construct row for that person
		df = data.loc[(data[column] >= start) & (data[column] <= end), :]
		# calculated revenue sum
		revenue = df[props.REVENUE_COL].sum()
		# append row to result
		result = result.append({'product-group': cat
			, 'start-date': start
			, 'end-date': end
			, 'week-number': x['slot']
			, 'order-booking-value': revenue
			, 'number-of-orders': df.shape[0]
			, 'order-ids': df['Offer ID'].tolist() # all the order id's of that product group
			}, ignore_index=True)


	return result

# for one product group, group the revenue on a biweekly basis
def group_quarterly_revenue(data, cat, column, result):
	# iterate over the quarters
	for i in range(1,len(props.QUARTERS)):
		# start and end for that quarter
		start = props.QUARTERS[i - 1]
		end = props.QUARTERS[i]
		# get results for that quarter
		df = data.loc[(data[column] >= start) & (data[column] < end), :]
		# calculated revenue sum
		revenue = df[props.REVENUE_COL].sum()
		# append row to result
		result = result.append({'product-group': cat
			, 'quarter': 'Q' + str(i)
			, 'start': start
			, 'end': end - datetime.timedelta(days=1) # get end of that quarter
			, 'order-booking-value': revenue
			, 'number-of-orders': df.shape[0]
			, 'order-ids': df['Offer ID'].tolist() # all the order id's of that product group
			}, ignore_index=True)

	# results beyond last quarter
	df = data.loc[data[column] >= end, :]
	# calculated revenue sum
	revenue = df[props.REVENUE_COL].sum()
	# append row to result
	result = result.append({'product-group': cat
		, 'quarter': 'NEXT-FY'
		, 'start': end
		, 'end': '' 
		, 'order-booking-value': revenue
		, 'number-of-orders': df.shape[0]
		, 'order-ids': df['Offer ID'].tolist() # all the order id's of that product group
		}, ignore_index=True)
	
	return result
