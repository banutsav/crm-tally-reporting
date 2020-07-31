import pandas as pd
# properties file
import props as props
# code from other files
import helper as hp

# get data to be used for the joint report
def joint_report_data(df):

	# init empty result dataframe
	result = pd.DataFrame(columns = props.JOINT_REPORT_HEADER)

	print('Generating Joint Report Data...')
	data = df.loc[(df['Offer ID'].str.startswith(props.JOINT_REPORT_OFFER_IDS, na=False)) 
	, :]

	for index, row in data.iterrows():
		# append row to result
		result = result.append({'offer-id': row['Offer ID']
			, 'product-group': row['Product Category']
			, 'contract-no': row['Contract ID']
			, 'opportunity-status': row['Opportunity Status'] 
			, 'updated-revenue': row['Updated Revenue']
			, 'agent-1': row['Owner']
			, 'agent-2': row['Shared 1']
			, 'agent-3': row['Shared 2']
			, 'created-on': row['Created On']
			, 'actual-close-date': row['Actual Close Date']}
			, ignore_index=True)

	return result