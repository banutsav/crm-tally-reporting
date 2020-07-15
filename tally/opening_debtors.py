import pandas as pd
import props as props
import helper as hp

def get_opening_debtors(df):
	# init empty result dataframe
	results = pd.DataFrame(columns = props.OPENING_DEBTORS_HEADER)
	
	# drop rows for blank ledger products
	df = df.dropna(subset=['Ldgr Product'])
	# iterate over all results
	for index, row in df.iterrows():

		# disregard product group = lease, treasury
		if row['Ldgr Product'] in props.NOT_PRODUCT_GROUPS:
			continue

		# get the quarter
		obj = {'product': row['Ldgr Product'], 'pending': row['Pending']}
		results = results.append(obj, ignore_index=True)
	
	return results