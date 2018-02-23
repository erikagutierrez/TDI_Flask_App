'''to recreate bup.csv'''

qs1 = '''select period_covered, record_id, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2012_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> ''

union 
select period_covered, record_id, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2013_state_drug`
where product_fda_list_name <> '' and  product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> ''

union

select period_covered, record_id, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2014_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> ''

union

select period_covered, record_id, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2015_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> '' '''

qs2 = '''select period_covered, utilization_type, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2016_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> ''

union 
select period_covered, utilization_type, state_code, number_of_prescriptions, total_amount_reimbursed, product_fda_list_name
from `2017_state_drug`
where product_fda_list_name <> '' and  product_fda_list_name <> 'NALOXONE' and number_of_prescriptions <> '' '''