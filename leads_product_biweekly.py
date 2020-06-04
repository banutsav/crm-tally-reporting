import pandas as pd
# properties file
import props as props
import helper as hp

# for each group get all leads grouped on a biweekly basis 
def get_leads_by_group_biweekly(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.GROUP_PERFORMANCE_BIWEEKLY)
	# unique product categories
	pc = df['Product Category'].unique().tolist()
	# iterate across the product categories
	print('Leads by Product Group aggregated biweekly...')
	for cat in pc:
		# rows of that product category and contract ID created
		data = df.loc[(df['Product Category'] == cat)  # product category match
		, :]
		# nothing to do if all rows empty
		if data.shape[0] == 0:
			continue

		result = hp.group_biweekly_revenue(data, cat, props.CREATED_ON_COL, result)

	return result