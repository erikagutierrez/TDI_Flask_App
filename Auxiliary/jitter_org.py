

'''this plot shows how much each org type is getting paid per Rx'''

'''--->conclusion: MCOs are making more money due to outliers'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

#load dataframes into pandas
df = pd.read_csv('org_years_money_Rx.csv')

#period_covered column will not show up, so trying something to fix that.
col_name = df.columns[0]
df = df.rename(columns = {col_name:'Year'})

col_name =df.columns[1]
df=df.rename(columns = {col_name:'Organization'})

df['Total Amount Reimbursed'] = df['Total Amount Reimbursed'].astype('float')
df['Total Number of Prescriptions'] = df['Total Number of Prescriptions'].astype('float')

df['Price per Prescription'] = df['Total Amount Reimbursed']/df['Total Number of Prescriptions']

# ax = sns.stripplot(x="org", y="price_per_Rx", hue="year", data=df, jitter=True)
ax = sns.stripplot(x="Year", y="Price per Prescription", hue="Organization", data=df, palette="Set2", dodge=True)
plt.ylim(0, 2000)

plt.show()
