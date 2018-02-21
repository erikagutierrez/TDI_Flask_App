'''do ttest to see if there is a difference in reimbursement rate based on the organization type'''
from scipy import stats
import pandas as import pd

df = pd.read_csv('org_years_money_Rx.csv')

# >>> df.head()
#      Yr   Org  Total Number of Prescriptions  Total Amount Reimbursed
# 0  2012  FFSU                           1001                344346.04
# 1  2012  FFSU                            121                   727.98
# 2  2012  FFSU                            165                  1832.92
# 3  2012  FFSU                             23                  6425.84
# 4  2012  FFSU                          24881                457668.36

x = df.loc[df['Org'] == 'FFSU'] #gives you all Org rows = FFSU
a = x['Total Amount Reimbursed'] #gives you just the 'total amount reimbursed column'

y = df.loc[df['Org'] == 'MCOU'] #gives you all Org rows = MCOU
b = y['Total Amount Reimbursed']


z = stats.ttest_ind(a, b)
print(z)
# Ttest_indResult(statistic=-1.033223567637414, pvalue=0.3015473266056193)
z = stats.ttest_ind(a, b, equal_var = False)
print(z)
# Ttest_indResult(statistic=-1.0276518664172083, pvalue=0.30416566534287803)


'''no difference in reimbursement rate between orgs'''
