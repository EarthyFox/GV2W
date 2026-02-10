import pandas as pd
from easygui import fileopenbox

file = fileopenbox(msg='Open it')

df = pd.read_excel(file)

print('Original Data Frame:')
print(df)

df = df.drop_duplicates(subset=['ADDRESS'])

df.to_excel('Duplicates_removed.xls', index=False, engine="xlsxwriter")