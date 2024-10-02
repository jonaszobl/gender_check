import pandas as pd

file_path = "input_wachau.xlsx"

df = pd.read_excel(file_path)

def determine_team_type(genders):
    if all(g == 'M' for g in genders):
        return 'männlich'
    elif all(g == 'F' for g in genders):
        return 'weiblich'
    else:
        return 'mixed'

df['Überprüfung'] = df.groupby('Team ID')['Geschlecht'].transform(determine_team_type) == df['Team Typ/Geschlecht']
print(df['Überprüfung'])
df['Überprüfung'] = df['Überprüfung'].replace({True: 'Überprüft', False: 'Fehler'})
print(df['Überprüfung'])


output_path = "output_wachau.xlsx"
df.to_excel(output_path, index=False)
