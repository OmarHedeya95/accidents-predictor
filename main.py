import pandas as pd
import matplotlib.pyplot as plt

accidents_dataset = pd.read_csv('./GermanCarAccidentsStats.csv')
#print(accidents_dataset.columns)

features = ['MONATSZAHL','AUSPRAEGUNG', 'JAHR', 'MONAT', 'WERT']

accidents_dataset = accidents_dataset[features]

#print(accidents_dataset.columns)

accidents_before_2020 = accidents_dataset[ accidents_dataset['JAHR'] < 2020]

# How many different values in every column
print(accidents_before_2020.nunique())

#What are the different categories of accidents are there
print(accidents_before_2020['AUSPRAEGUNG'].value_counts())

#plt.figure()
accidents_before_2020.plot.bar(x = 'JAHR', y= 'WERT', rot=0)

plt.show()

