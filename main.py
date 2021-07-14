import pandas as pd

accidents_dataset = pd.read_csv('./GermanCarAccidentsStats.csv')
#print(accidents_dataset.columns)

features = ['MONATSZAHL','AUSPRAEGUNG', 'JAHR', 'MONAT', 'WERT']

accidents_dataset = accidents_dataset[features]

#print(accidents_dataset.columns)

accidents_before_2020 = accidents_dataset[ accidents_dataset['JAHR'] < 2020]