
import pandas as pd

people = [
    {'Name': 'Peti', 'Age': '26', 'Height': 170},
    {'Name': 'Laci', 'Age': '20', 'Height': 160},
    {'Name': 'Mari', 'Age': '13', 'Height': 140}
]

df = pd.DataFrame(people)

df['ID'] = [ 'ID123', 'ID456', 'ID789' ]

# df['Age'] = [ '27', '21', '14' ]

df['Age'] = df['Age'].astype(int)
df['Age'] = [ x + 1 for x in df['Age'] ]

# print(df['Age'].mean())


df = pd.read_excel('transactions.xlsx', sheet_name='Sheet1')

print(df)
