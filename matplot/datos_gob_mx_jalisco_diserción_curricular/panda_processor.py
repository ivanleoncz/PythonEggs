#!/usr/bin/python3

import pandas as pd

csv_path = "cct_indicadores.csv"
csv_columns = ['NOM TURNO', ' NOMBRE LOCALIDAD', 'SOSTENIMIENTO', 'NIVEL',
               'PROGRAMA', 'DESERCIîN INTRACURRICULAR']


csv_data = pd.read_csv(csv_path, usecols = csv_columns, encoding = "ISO-8859-1")

#print(list(csv_data.columns))

#print(csv_data.loc[(csv_data["NOM TURNO"] == 'MATUTINO')])

filter_df = csv_data[(csv_data['NOM TURNO'] == 'MATUTINO') & (csv_data['DESERCIîN INTRACURRICULAR'] != 'N.A.')]
print(filter_df)
