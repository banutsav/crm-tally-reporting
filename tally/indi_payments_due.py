import pandas as pd
import props as props
import helper as hp

# payments due from receivables for each person and each product group
def individual_payments_due(df):

	# init empty result dataframe
	results = pd.DataFrame(columns = props.INDI_PAYMENTS_DUE_HEADER)

	# replace null values with 0
	df['Pending'].fillna(0, inplace = True)
	# drop rows for blank people and bank products
	df = df.dropna(subset=['Agent', 'Product'])

	# iterate over the set of people
	print('Individual Payments Due...')
	data = df[[props.RECEIVABLES_DATE, 'Agent', 'Product', 'Pending', 'Ref. No.']]
	
	# iterate over all results
	for index, row in data.iterrows():
		# disregard product group = lease, treasury
		if row['Product'] in props.NOT_PRODUCT_GROUPS:
			continue

		# get before or after based on the reference number
		invoiced_date = hp.get_before_after_ref_no(row['Ref. No.'])

		# get the quarter
		quarter = hp.get_quarter(row[props.RECEIVABLES_DATE])
		obj = {'person': row['Agent'], 'product-group': row['Product']
		, 'payments-due': row['Pending'], 'date': row[props.RECEIVABLES_DATE]
		, 'quarter': quarter, 'invoiced-date': invoiced_date, 'reference-number': row['Ref. No.']}
		results = results.append(obj, ignore_index=True)
	
	return results