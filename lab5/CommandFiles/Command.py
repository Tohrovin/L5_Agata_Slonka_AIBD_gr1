import pandas as pd

# Set path to data
DIR = "../AnalysisData/"

# Read original data
tb_org = pd.read_csv(f"{DIR}tb_org.csv", sep=';')
print(tb_org)

# Choose the most interesting columns
tb_ana = tb_org[['iso2', 'year', 'new_sp']]
print(tb_ana)

tb_ana = tb_ana.sort_values(['iso2', 'year', 'new_sp'])

# Preparing the dataframe for sum
df_sm = tb_org[
    [ 'new_sp_m014', 'new_sp_m1524', 'new_sp_m2534', 'new_sp_m3544', 'new_sp_m4554',
     'new_sp_m5564', 'new_sp_m65', 'new_sp_mu']]
df_sf = tb_org[
    [ 'new_sp_f014', 'new_sp_f1524', 'new_sp_f2534', 'new_sp_f3544', 'new_sp_f4554',
     'new_sp_f5564', 'new_sp_f65', 'new_sp_fu']]

tb_ana.loc[:, 'm_cases'] = df_sm.sum(numeric_only=True, axis=1)
tb_ana.loc[:, 'f_cases'] = df_sf.sum(numeric_only=True, axis=1)

print(tb_ana)
tb_ana.to_csv(path_or_buf=f"{DIR}tb_ana.csv", sep=";")
