import pandas as pd
# properties file
import props as props

# create ht summary data
def ht_summary(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.HT_SUMMARY_HEADER)
	# unique product categories
	pc = df['Product Category'].unique().tolist()
	print('Product Group summary...')
	# iterate across the product categories
	for cat in pc:
		# rows of that product category and contract ID created
		data = df.loc[(df['Product Category'] == cat)  # product category match
		& (df[props.CONTRACT_ID].notnull()) # non null contract number
		& (df[props.CONTRACT_ID] != '0') # some rows have contract id set to 0
		& (df[props.CLOSE_DATE_COL] > props.CLOSE_DATE)
		, ['Offer ID',props.REVENUE_COL]]
		# calculated revenue sum
		revenue = data[props.REVENUE_COL].sum()
		# append row to result
		result = result.append({'product-group': cat 
			, 'order-booking-value': revenue
			, 'number-of-orders': data.shape[0]
			, 'order-ids': data['Offer ID'].tolist() # all the order id's of that product group
			}, ignore_index=True)
	return result