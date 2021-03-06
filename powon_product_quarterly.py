import pandas as pd
# properties file
import props as props
import helper as hp

# per product group, get the opportunities won and then group on a biweekly basis
def get_powon_by_group_quarterly(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.GROUP_SALES_FUNNEL_HEADER)
	# unique product categories
	pc = df['Product Category'].unique().tolist()
	# iterate across the product categories
	print('Leads PO Won per Product Group aggregated quarterly...')
	for cat in pc:
		# rows of that product category and contract ID created
		data = df.loc[(df['Product Category'] == cat)  # product category match
		& (df[props.CONTRACT_ID].notnull()) # non null contract number
		& (df[props.CONTRACT_ID] != '0') # some rows have contract id set to 0
		& (df['Opportunity Status'] == 'Won')
		, :]
		# nothing to do if all rows empty
		if data.shape[0] == 0:
			continue

		result = hp.group_quarterly_revenue(data, cat, props.CLOSE_DATE_COL, result)

	return result
