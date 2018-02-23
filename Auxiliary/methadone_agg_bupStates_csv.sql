select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2012_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2013_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2014_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2015_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2016_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code

union all

select period_covered, state_code, sum(number_of_prescriptions), sum(total_amount_reimbursed)
from `2017_state_drug`
where product_fda_list_name <> '' and product_fda_list_name <> 'NALOXONE' and product_fda_list_name = 'METHADONE'  and state_code in ('AK', 'AR', 'AZ', 'CO', 'FL', 'ID', 'KY', 'LA', 'ME', 'MI', 'MN', 'MO', 'NC', 'NH', 'SC', 'TN', 'UT', 'WV', 'WY', 'XX')
group by state_code