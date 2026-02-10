# put additional filtering including unique
from rich import print

import pandas as pd
import numpy as np

# file_name = './__input_files/output_Dec-02-2022_output.xlsx'
file_name = './__input_files/nate.xls'



df = pd.read_excel(open(file_name, "rb"))
# df2 = pd.read_excel(open(file_name2, "rb"))
# print(df.columns)


unique = np.unique(df[['FULLNAME']].values)
unique_addresses_count = df.ADDRESS.nunique(dropna = True)
unique_full_name_count = df.FULLNAME.nunique(dropna = True)
unique_charges = df.CHARGE.nunique(dropna = True)


print(f'there are {unique_full_name_count} unique full names and {unique_addresses_count} unique addresses and {unique_charges} unique charges')
# print(unique_addresses_count)

df.rename(columns = {'FIRST_NAME':'FNAME', 'LASTNAME':'LNAME'}, inplace = True)


new_df = df[['LNAME', 'FNAME', 'ADDRESS', 'CITYSTATEZIP', 'CHARGE']]

new_df_missing = new_df.loc[new_df['LNAME'] == 'missing']
new_df_filtered = new_df.loc[new_df['LNAME'] != 'missing']
# new_df_filtered = new_df.loc[new_df['LNAME'] |= 'missing']
# print(new_df_filtered)
# remove files with missing
#create file with missing data
new_df.to_csv(f"all_information.csv")
new_df_missing.to_csv(f"missing_information.csv")
new_df_filtered.to_csv(f"filtered_information.csv")
# unique_only = new_df_filtered.LNAME.unique()
# get nmuber of unique values total
# unique_count = new_df_filtered.LNAME.nunique(dropna = True)
# unique_count = new_df_filtered.ADDRESS.nunique(dropna = True)

# new_df.to_csv(f"sendtopaula.csv")

# FILENAME	FULLNAME	ADDRESS	CITYSTATEZIP	LASTNAME	FIRST_NAME
# IMG_3256.jpg_Dec-02-2022_out.txt	MONTANO GUTIERREZ, RAUL EDGAR	409 BAILEY CT	STERLING, VA 20164	MONTANO GUTIERREZ	 RAUL EDGAR
#
# 
# rename columns to LNAME	FNAME	ADDRESS	CITYSTATEZIP

# LNAME	FNAME	ADDRESS	CITYSTATEZIP
# REYES-CANALES	CARLOS	8103 MACE CT	MANASSAS, VA 20111

# rename columns
# find duplicates
# create new file as csv

# LNAME	FNAME	ADDRESS	CITYSTATEZIP


# df3 = df[['LASTNAME']]
# df4 = df2[['LASTNAME']]

# concatenated = pd.concat([df3, df4])

# # # print(df3)
# print(concatenated.duplicated())