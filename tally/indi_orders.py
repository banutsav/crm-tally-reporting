import pandas as pd
import props as props
import helper as hp

# all orders bagged per person per product group
def individual_orders_bagged(df):
	
	# init empty result dataframe
	results = pd.DataFrame(columns = props.INDI_ORDER_BAGGED_HEADER)
	
	# change null values with 0
	df['Gross Total (G-I-J)'].fillna(0, inplace = True)
	df['CGST'].fillna(0, inplace = True)
	df['SGST'].fillna(0, inplace = True)

	# add new column to dataframe = G - I - J
	df['gross-total'] = df['Gross Total (G-I-J)'] - df['CGST'] - df['SGST']

	# drop rows for blank people and bank products
	df = df.dropna(subset=['Agent', 'Cost Centre'])

	# iterate over the set of people
	print('Individual Orders Bagged...')
	data = df[['Date', 'Agent', 'Cost Centre', 'gross-total']]
	
	# iterate over all results
	for index, row in data.iterrows():
		# get the quarter
		quarter = hp.get_quarter(row['Date'])
		# get before or after FY start
		invoiced_date = hp.get_before_after_fy(row['Date'])
		# construct object
		obj = {'person': row['Agent'], 'product-group': row['Cost Centre']
		, 'gross-total': row['gross-total'], 'date': row['Date'], 'quarter': quarter, 'invoiced-date': invoiced_date}
		results = results.append(obj, ignore_index=True)
	
	return results