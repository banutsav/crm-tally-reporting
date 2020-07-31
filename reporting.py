import time
import datetime
import numpy as np
import pandas as pd
from pandas import ExcelWriter
pd.options.mode.chained_assignment = None  # default='warn'

# import code from other files
import props as props
import helper as hp
import individual as indi
import groups as gp
import sales_performance as sfp
import sales_funnel_pipeline as sfp_wp
import indi_biweek as bw
import po_won_biweekly as powon
import po_won_quarterly as powon_q
import leads_product_quarterly as lpq
import leads_product_biweekly as lpbw
import powon_product_biweekly as powpbw
import powon_product_quarterly as powpq
import expired_leads as exl
import joint_report as jr

if __name__ == '__main__':
	start = time.time()
	print('Execution started...')

	# read data into dataframe
	xls = pd.ExcelFile(props.IN_FILE)
	crmdf = pd.read_excel(xls, xls.sheet_names[0]) # read first sheet | props.IN_TAB
	lost_cases = pd.ExcelFile(props.LOST_CASES_FILE)
	lost_cases_df = pd.read_excel(lost_cases, lost_cases.sheet_names[0])

	# get set of biweekly dates
	biweekly_dates = hp.get_biweekly_dates_from_schedule()
	
	# ht summary report
	ht_sum_df = gp.ht_summary(crmdf) # groups.py
	# individual summary
	indi_sum_df = indi.indi_summary(crmdf) # individual.py
	
	# sales funnel and performnce calculation for individuals
	sfp_df = sfp.sales_funnel_performance_data(crmdf) # sales_performance.py
	sfp_wp_df = sfp_wp.sales_funnel_performance_with_phase_data(crmdf) # sales_funnel_pipeline.py
	# bi-weekly performance summary
	lc_bw_df = bw.leads_created_biweekly(crmdf, biweekly_dates) # indi_biweek.py
	# po won biweekly performance
	powon_bw_df = powon.po_won_biweekly(crmdf, biweekly_dates) # po_won_biweekly.py
	
	# po won by quarters
	powon_q_df = powon_q.po_won_quarterly(crmdf) # po_won_quarterly.py
	# per product group find leads created on quarterly basis
	group_leads_q_df = lpq.get_leads_by_group_quarterly(crmdf) # leads_product_quarterly.py
	# per product group, aggregate leads on a biweekly basis
	group_leads_bw = lpbw.get_leads_by_group_biweekly(crmdf, biweekly_dates) # leads_product_biweekly.py
	# per product group won opportunities grouped biwekly
	group_powon_bw = powpbw.get_powon_by_group_biweekly(crmdf, biweekly_dates) # powon_product_biweekly.py
	# per product get opportunities won a quarterly basis
	group_powon_q = powpq.get_powon_by_group_quarterly(crmdf) # powon_product_quarterly.py
	# expired leads
	expired_leads = exl.individual_product_expired_leads(crmdf) # expired_leads.py
	# joint report
	joint_report = jr.joint_report_data(crmdf) # joint_report.py
	
	# save data to file
	writer = ExcelWriter(props.OUTFILE)
	ht_sum_df.to_excel(writer, 'product-group', index=False) # groups.py
	indi_sum_df.to_excel(writer, 'individual', index=False) # individual.py
	
	sfp_df.to_excel(writer, 'sales-funnel-performance', index=False) # sales_performance.py
	sfp_wp_df.to_excel(writer, 'sales-funnel-phase', index=False) # sales_funnel_pipeline.py
	
	lc_bw_df.to_excel(writer, 'leads-created-biweekly', index=False) # indi_biweek.py
	powon_bw_df.to_excel(writer, 'po-won-biweekly', index=False) # po_won_biweekly.py
	powon_q_df.to_excel(writer, 'po-won-quarterly', index=False) # po_won_quarterly.py
	
	group_leads_q_df.to_excel(writer, 'product-leads-quarterly', index=False) # leads_product_quarterly.py
	group_leads_bw.to_excel(writer, 'product-leads-biweekly', index=False) # leads_product_biweekly.py
	group_powon_bw.to_excel(writer, 'product-powon-biweekly', index=False) # powon_product_biweekly.py
	group_powon_q.to_excel(writer, 'product-powon-quarterly', index=False) # powon_product_quarterly.py
	expired_leads.to_excel(writer, 'expired-leads', index=False) # expired_leads.py
	joint_report.to_excel(writer, 'joint-report', index=False) # joint_report.py
	
	# write the main crm data set
	crmdf.to_excel(writer, 'crm-master', index=False)
	lost_cases_df.to_excel(writer, 'lost-cases-master', index=False)
	writer.save()

	print('Results saved to', props.OUTFILE)
	# calculate execution time
	end = time.time()
	print('Execution finished in',str(round(end - start,2)),'secs')
	input('You can close this window now...')
