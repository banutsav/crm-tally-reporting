import pandas as pd
import props as props
import helper as hp

# use the stock data to get the direct cose
def get_direct_cost(df):

	# init empty result dataframe
	results = pd.DataFrame(columns = props.DIRECT_COST_HEADER)

	# replace nulls with 0's
	df.fillna(0, inplace = True)
	# iterate over all results
	print('Direct Costs and other Stock Data...')
	for index, row in df.iterrows():
		dc = row['Value-1'] + row['Value-2'] - row['Value-4']
		obj = {'product': row['Product Group'], 'direct-cost': dc, 'inventory-value': row['Value-4']}
		results = results.append(obj, ignore_index=True)
	
	return results