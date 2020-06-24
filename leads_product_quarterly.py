import pandas as pd
import datetime
# properties file
import props as props
import helper as hp

# create ht summary data
def get_leads_by_group_quarterly(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.GROUP_SALES_FUNNEL_HEADER)
	# unique product categories
	pc = df['Product Category'].unique().tolist()
	# iterate across the product categories
	print('Leads by Product Group aggregated quarterly...')
	for cat in pc:
		# rows of that product category and contract ID created before creation date
		data = df.loc[(df['Product Category'] == cat)  # product category match
		& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
		& (df['Created On'] < props.CREATION_DATE)
		, :]
		# nothing to do if all rows empty
		if data.shape[0] != 0:
			result = group_quarterly_revenue(data, cat, result, 'before-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

		# rows of that product category and contract ID created after creation date
		data = df.loc[(df['Product Category'] == cat)  # product category match
		& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
		& (df['Lead Status'] != 'Disqualified') # lead not disqualified
		& (df['Created On'] >= props.CREATION_DATE)
		, :]
		# nothing to do if all rows empty
		if data.shape[0] != 0:
			result = group_quarterly_revenue(data, cat, result, 'after-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

	return result

# group the revenue by quarters
def group_quarterly_revenue(data, cat, result, created):
	# iterate over the quarters
	for i in range(1,len(props.QUARTERS)):
		# start and end for that quarter
		start = props.QUARTERS[i - 1]
		end = props.QUARTERS[i]
		# make a quarter timeframe string
		# get results for that quarter
		df = data.loc[(data[props.UP_PURCH_COL] >= start) & (data[props.UP_PURCH_COL] < end), :]
		# calculated revenue sum
		revenue = df[props.REVENUE_COL].sum()
		# append row to result
		result = result.append({'product-group': cat
			, 'creation-date': created
			, 'quarter': 'Q' + str(i) 
			, 'start': start
			, 'end': end - datetime.timedelta(days=1) # get end of that quarter
			, 'order-booking-value': revenue
			, 'number-of-orders': df.shape[0]
			, 'order-ids': df['Offer ID'].tolist() # all the order id's of that product group
			}, ignore_index=True)

	# get results for the next FY
	df = data.loc[data[props.UP_PURCH_COL] >= end, :]
	# calculated revenue sum
	revenue = df[props.REVENUE_COL].sum()
	# append row to result
	result = result.append({'product-group': cat
		, 'creation-date': created
		, 'quarter': 'NEXT-FY'
		, 'start': end 
		, 'order-booking-value': revenue
		, 'number-of-orders': df.shape[0]
		, 'order-ids': df['Offer ID'].tolist() # all the order id's of that product group
		}, ignore_index=True)

	return result