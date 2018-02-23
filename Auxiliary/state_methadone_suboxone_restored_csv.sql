'''how to query sql for state_methadone_suboxone_restored.csv'''

qs1 = '''
select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2012_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2013_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2014_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2015_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2016_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2017_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name <> 'METHADONE' 
group by state_code

'''

qs2 = '''

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2012_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2013_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2014_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2015_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2016_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2017_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE' 
group by state_code

'''