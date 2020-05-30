import pandas as pd
import props

# revenue and lead calculation for individual based on lead sharing
def revenue_lead_individual(df):
	# init revenue and leads
	revenue = 0
	leads = 0

	# iterate across the data for one person and one product group
	for index, row in df.iterrows():
		
		# calculate sharing factor for this order
		factor = 1
		if pd.isnull(row['Shared to 1']) == False:
			factor += 1
		if pd.isnull(row['Shared to 2']) == False:
			factor += 1
		
		# add to total revenue and leads
		revenue += (row[props.REVENUE_COL] / factor)
		leads += (1 / factor)
		
		# DEBUG
		#print(row['Offer ID'], row['Product Category'], row['Owner'], row['Shared to 1'], row['Shared to 2'], factor)

	return revenue, leads