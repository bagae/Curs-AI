
import pandas as pd
import numpy as np

# 1. Crearea DataFrame-ului
data = {
    'Nume': ['Ana', 'Dan', 'Mara', 'Vlad', 'Ioana'],
    'Vârstă': [23, 31, 27, 35, 29],
    'Departament': ['IT', 'HR', 'IT', 'Marketing', 'HR'],
    'Salariu': [4500, 5200, 4800, 5000, 4700],
    'Bonus': [np.nan, 300, np.nan, 400, np.nan],
    'Experiență': [2, 5, 3, 7, 4]
}

df = pd.DataFrame(data)
print(df, "\n")

# 2. Primele 3 rânduri
print(df.head(3), "\n")

# 3. Ultimele 2 rânduri
print(df.tail(2), "\n")

# 4. Informații generale
print(df.info(), "\n")

# 5. Statistici descriptive
print(df.describe(), "\n")

# 6. Valori lipsă
print(df.isnull().sum(), "\n")

# 7. Completează Bonus
df['Bonus'] = df['Bonus'].fillna(df['Salariu']*0.10)
print(df, "\n")

# 8. Șterge Experiență
df = df.drop(columns=['Experiență'])
print(df, "\n")

# 9. Sortează după Salariu descrescător
df_sorted = df.sort_values(by='Salariu', ascending=False)
print(df_sorted, "\n")

# 10. Angajați IT
print(df[df['Departament']=='IT'], "\n")

# 11. Vârstă între 25 și 32
print(df[(df['Vârstă']>=25) & (df['Vârstă']<=32)], "\n")

# 12. Coloanele Nume și Salariu
print(df[['Nume','Salariu']], "\n")

# 13. Salariu total
df['Salariu total'] = df['Salariu'] + df['Bonus']
print(df, "\n")

# 14. Redenumește Departament
df = df.rename(columns={'Departament':'Dept'})
print(df, "\n")

# 15. Dimensiunea DataFrame-ului
print(df.shape, "\n")

# 16. Numele coloanelor
print(df.columns, "\n")

# 17. Număr valori per departament
print(df['Dept'].value_counts(), "\n")

# 18. Rândurile 1,3,4
print(df.iloc[[1,3,4]], "\n")

# 19. Salariu total > 5000
print(df[df['Salariu total']>5000], "\n")

# 20. Sortează după Salariu total și resetează indexul
df_sorted_total = df.sort_values(by='Salariu total', ascending=False).reset_index(drop=True)
print(df_sorted_total)