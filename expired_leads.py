import pandas as pd
# properties file
import props as props
# code from other files
import helper as hp

# get expired leads for both individuals and products
def individual_product_expired_leads(df):

	# init empty result dataframe
	result = pd.DataFrame(columns = props.EXPIRED_LEADS_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared 1'].unique().tolist()) + (df['Shared 2'].unique().tolist())
	people = hp.get_unique_list(people)

	# current time
	currtime = pd.Timestamp.now()

	print('Expired leads for People...')
	
	for person in people:

		# rows of that individual
		data = df.loc[
		(
			(df['Owner'] == person) # if person is owner
			| (df['Shared 1'] == person) # if person is part of shared 1
			| (df['Shared 2'] == person) # if person is part of shared 2
		)
		& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
		& (df['Lead Status'] != 'Disqualified') # lead not disqualified
		& (df[props.UP_PURCH_COL] <= currtime)
		, :]

		obj = hp.construct_person_record(person, "", data)

		# append row to result
		result = result.append(obj, ignore_index=True)

	# unique product categories
	groups = df['Product Category'].unique().tolist()

	print('Expired leads for Product Groups...')
	for product in groups:
		
		# rows of that product category
		data = df.loc[(df['Product Category'] == product)  # product category match
		& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
		& (df['Lead Status'] != 'Disqualified') # lead not disqualified
		& (df[props.UP_PURCH_COL] <= currtime)
		, :]

		# append row to result
		result = result.append({'product-group': product
		, 'total-revenue': round(data[props.REVENUE_COL].sum()) 
		, 'total-leads': data.shape[0]
		, 'order-ids-where-owner': data['Offer ID'].tolist()
		}, ignore_index=True)

	return result