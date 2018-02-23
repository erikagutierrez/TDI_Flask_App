'''how to query for org_years_money_Rx.csv'''

qs1 = '''select period_covered, record_id, number_of_prescriptions, total_amount_reimbursed
from `2012_state_drug`
where product_fda_list_name <> '' and number_of_prescriptions <> ''  and product_fda_list_name <> 'NALOXONE'

union

select period_covered, record_id, number_of_prescriptions, total_amount_reimbursed
from `2013_state_drug`
where product_fda_list_name <> '' and number_of_prescriptions <> ''  and product_fda_list_name <> 'NALOXONE'

union 

select period_covered, record_id, number_of_prescriptions, total_amount_reimbursed
from `2014_state_drug`
where product_fda_list_name <> '' and number_of_prescriptions <> ''  and product_fda_list_name <> 'NALOXONE'

union

select period_covered, record_id, number_of_prescriptions, total_amount_reimbursed
from `2015_state_drug`
where product_fda_list_name <> '' and number_of_prescriptions <> ''  and product_fda_list_name <> 'NALOXONE' '''

qs2 = '''select period_covered, utilization_type, number_of_prescriptions, total_amount_reimbursed
from `2016_state_drug`
where product_fda_list_name <> '' and number_of_prescriptions <> '' and product_fda_list_name <> 'NALOXONE'
'''