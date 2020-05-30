import pandas as pd
# properties file
import props as props
import helper as hp

def sales_funnel_performance_data(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.SALES_FUNNEL_PERFORMANCE_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared to 1'].unique().tolist()) + (df['Shared to 2'].unique().tolist())

	# unique product categories
	groups = df['Product Category'].unique().tolist()
	# iterate over the set of people
	print('Sales Funnel Performance Summary...')
	for person in people:
		# check all groups for that person
		for cat in groups:
			# records before the creation date
			data = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared to 1'] == person) # if person is part of shared 1
				| (df['Shared to 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
			& (df['Created On'] < props.CREATION_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] == 0:
				continue
			
			#print('Records found hence processing',person,cat)
			result = construct_performance_dataframe(person, cat, data, result
				, 'before-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

			# records after the creation date
			data_1 = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared to 1'] == person) # if person is part of shared 1
				| (df['Shared to 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
			& (df['Created On'] >= props.CREATION_DATE)
			, :]

			# nothing to do if all rows empty
			if data_1.shape[0] == 0:
				continue
			result = construct_performance_dataframe(person, cat, data, result
				, 'after-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

	return result

# get rows for records before and after the creation date
def construct_performance_dataframe(person, cat, data, result, created):
	# iterate over the quarters
	for i in range(1,len(props.QUARTERS)):
		# start and end for that quarter
		start = props.QUARTERS[i - 1]
		end = props.QUARTERS[i]
		# get results for that quarter
		dfq = data.loc[(data[props.UP_PURCH_COL] >= start) & (data[props.UP_PURCH_COL] < end), :]
		obj = construct_sfp_record(person, cat, dfq)
		# set the quarter
		obj['quarter'] = 'Q' + str(i)
		obj['creation-date'] = created
		result = result.append(obj, ignore_index=True)
			
	# results beyond last quarter
	df_ny = data.loc[data[props.UP_PURCH_COL] >= end, :]
	obj = construct_sfp_record(person, cat, df_ny)
	obj['quarter'] = 'NEXT-FY'
	obj['creation-date'] = created
	# append row to result
	result = result.append(obj, ignore_index=True)
	return result

# construct sales performance record for one person and one group
def construct_sfp_record(person, cat, data):
	# split dataframes according to where person is owner, share to 1 or shared to 2
	df_1 = data.loc[data['Owner'] == person]
	df_2 = data.loc[data['Shared to 1'] == person]
	df_3 = data.loc[data['Shared to 2'] == person]

	# calculate revenue and leads where owner
	revenue_1, leads_1 = hp.revenue_lead_individual(df_1) # helper.py 
	# calculate revenue and lead breakdown where first share
	revenue_2, leads_2 = hp.revenue_lead_individual(df_2) # helper.py
	# calculate revenue and lead breakdown where second share
	revenue_3, leads_3 = hp.revenue_lead_individual(df_3) # helper.py

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