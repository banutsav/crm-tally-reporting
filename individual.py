import pandas as pd
# properties file
import props as props
# code from other files
import helper as hp

# create individual summary data
def indi_summary(df):
	# init empty result dataframe
	result = pd.DataFrame(columns = props.INDI_SUMMARY_HEADER)
	
	# unique individuals
	people = (df['Owner'].unique().tolist()) + (df['Shared 1'].unique().tolist()) + (df['Shared 2'].unique().tolist())
	people = hp.get_unique_list(people)

	# unique product categories
	groups = df['Product Category'].unique().tolist()
	# iterate over the set of people
	print('Individual Summary...')
	for person in people:
		# check all groups for that person
		for cat in groups:
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
			& (df[props.CLOSE_DATE_COL] > props.CLOSE_DATE)
			, :]
			
			
			# nothing to do if all rows empty
			if data.shape[0] == 0:
				continue
			#print('Records found hence processing',person,cat)
			obj = hp.construct_person_record(person, cat, data)

			# append row to result
			result = result.append(obj, ignore_index=True)

	return result
