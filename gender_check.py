import pandas as pd
import gender_guesser.detector as gender

input_file = 'input.xlsx'  
output_file = 'output.xlsx'  

df = pd.read_excel(input_file)

d = gender.Detector()

def check_gender(row):
    vorname = row['Vorname']
    eingetragenes_geschlecht = row['Geschlecht']

    geschlecht = d.get_gender(vorname)

    print(f"Eingetragendes Geschlecht: {eingetragenes_geschlecht}, Geschätztes Geschlecht: {geschlecht}")

    if geschlecht in ['male', 'mostly_male'] and eingetragenes_geschlecht == 'F':
        return 'Überprüfen'
    elif geschlecht in ['female', 'mostly_female'] and eingetragenes_geschlecht == 'M':
        return 'Überprüfen'
    else:
        return 'Passt'
    
df['Geschlecht überprüfen'] = df.apply(check_gender, axis=1)

df.to_excel(output_file, index=False)

print("Überprüfung abgeschlossen und in die neue Excel-Datei gespeichert.")
