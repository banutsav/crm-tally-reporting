import pandas as pd
# properties file
import props as props
import helper as hp

# iterate over all the leads accorsing to creaton date and group on a biweekly basis
def leads_created_biweekly(df, biweekly_dates):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.BIWEEKLY_PERFORMANCE_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared to 1'].unique().tolist()) + (df['Shared to 2'].unique().tolist())
	people = hp.get_unique_list(people)


	# unique product categories
	groups = df['Product Category'].unique().tolist()

	# iterate over the set of people
	print('Bi-weekly lead creation...')
	for person in people:
		
		# check all groups for that person
		for cat in groups:
			# get records which are after creation date
			data = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared to 1'] == person) # if person is part of shared 1
				| (df['Shared to 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& (df['Created On'] >= props.CREATION_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] == 0:
				continue
			result = hp.construct_biweekly_df(person, cat, data, props.CREATED_ON_COL, result, biweekly_dates)

	return result