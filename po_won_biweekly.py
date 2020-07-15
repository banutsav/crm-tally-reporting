import pandas as pd
# properties file
import props as props
import helper as hp

# contracts won group based on close date on a bi-weekly basis
def po_won_biweekly(df, biweekly_dates):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.BIWEEKLY_PERFORMANCE_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared 1'].unique().tolist()) + (df['Shared 2'].unique().tolist())
	people = hp.get_unique_list(people)

	# unique product categories
	groups = df['Product Category'].unique().tolist()
	# iterate over the set of people
	print('PO Won Bi-weekly...')
	for person in people:
		# check all groups for that person
		for cat in groups:
			# get records which are after creation date
			data = df.loc[
			(
				(df['Owner'] == person) # if person is owner
				| (df['Shared 1'] == person) # if person is part of shared 1
				| (df['Shared 2'] == person) # if person is part of shared 2
			) # data for that person 
			& (df['Product Category'] == cat) # and that category
			& (df[props.CONTRACT_ID].notnull()) # non null contract number
			& (df[props.CONTRACT_ID] != '0') # some rows have contract id set to 0
			& (df[props.CLOSE_DATE_COL] > props.CLOSE_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] == 0:
				continue

			result = hp.construct_biweekly_df(person, cat, data, props.CLOSE_DATE_COL, result, biweekly_dates)

	return result
