import pandas as pd
# properties file
import props as props
import helper as hp

# quarterly breakdown of sales performance
def po_won_quarterly(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.SALES_FUNNEL_PERFORMANCE_HEADER)

	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared 1'].unique().tolist()) + (df['Shared 2'].unique().tolist())
	people = hp.get_unique_list(people)

	# unique product categories
	groups = df['Product Category'].unique().tolist()
	# iterate over the set of people
	print('PO Won Quarterly...')
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
			& (df['Opportunity Status'] == 'Won')
			& (df[props.CLOSE_DATE_COL] >= props.CLOSE_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] != 0:
				result = hp.construct_quarterly_dataframe(person, cat, data, props.CLOSE_DATE_COL, result
					, 'after-' + props.CLOSE_DATE.strftime("%d-%b-%Y"))

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
			& (df['Opportunity Status'] == 'Won')
			& (df[props.CLOSE_DATE_COL] < props.CLOSE_DATE)
			, :]

			# nothing to do if all rows empty
			if data.shape[0] != 0:
				result = hp.construct_quarterly_dataframe(person, cat, data, props.CLOSE_DATE_COL, result
					, 'before-' + props.CLOSE_DATE.strftime("%d-%b-%Y"))

	return result
