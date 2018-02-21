import numpy as np
import pandas as pd

def process_data():
    df = pd.read_csv('state_methadone_suboxone_restored.csv')

    state_list = list(df['State'].unique())



    def morph(series):
         if series.loc['Year'] == 2017:
                 series2 = series.copy()
                 series2['Total Amount Reimbursed'] = series2['Total Amount Reimbursed'] * 2
                 series2['Total Number of Prescriptions'] = series2['Total Number of Prescriptions'] * 2
                 return series2
         else:
                 return series

    df2 = df.apply(morph, axis = 1)

    population = df2['Total Number of Prescriptions']

    # Turn population into bubble sizes. Use min_size and factor to tweak.
    scale_factor = 4
    population_size = np.sqrt(population / np.pi) / scale_factor
    min_size = 15
    population_size = population_size.where(population_size >= min_size).fillna(min_size)

    return population_size, state_list
