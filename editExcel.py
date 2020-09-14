import pandas as pd
import openpyxl

df = pd.read_excel(r'c:\tmp\Teste.xlsx',sheet_name="Sheet1",header=0,thousands=None)

df.insert(20,'TOTAL',df['one'].sub(df['two'], axis=0))

df.to_excel(r'', sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=False, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)

