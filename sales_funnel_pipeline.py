import pandas as pd
# properties file
import props as props
import helper as hp

# quarterly breakdown of sales performance
def sales_funnel_performance_with_phase_data(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.SALES_FUNNEL_PERFORMANCE_WITH_PHASE_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared 1'].unique().tolist()) + (df['Shared 2'].unique().tolist())
	people = hp.get_unique_list(people)

	# unique product categories
	groups = df['Product Category'].unique().tolist()
	# iterate over the set of people
	print('Sales Funnel Performance Summary with Pipeline Phase Data...')
	for person in people:
		
		# check all groups for that person
		for cat in groups:
			# records before the creation date
			data = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared 1'] == person) # if person is part of shared 1
				| (df['Shared 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
			& (df['Lead Status'] != 'Disqualified') # lead not disqualified
			& (df[props.CREATED_ON_COL] < props.CREATION_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] != 0:
				result = hp.construct_quarterly_dataframe_with_phase(person, cat, data, props.UP_PURCH_COL, result
					, 'before-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

			# records after the creation date
			data = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared 1'] == person) # if person is part of shared 1
				| (df['Shared 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& ((df['Opportunity Status'] == 'Open') | (df['Opportunity Status'].isnull()))
			& (df['Lead Status'] != 'Disqualified') # lead not disqualified
			& (df[props.CREATED_ON_COL] >= props.CREATION_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] != 0:
				result = hp.construct_quarterly_dataframe_with_phase(person, cat, data, props.UP_PURCH_COL, result
					, 'after-' + props.CREATION_DATE.strftime("%d-%b-%Y"))

	return result

