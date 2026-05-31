import pandas as pd

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
# print(df)
# print('---------------------')
# print(df['last'])
# print('---------------------')
# print(df['last'] == 'Doe')
# print('---------------------')
# flit = df['last'] == 'Doe'
# print(df[flit])
# print(df.loc[flit]) #This is the most recommended way
#Because we can do this (Not using print(df[flit]))
# print(df.loc[flit, 'email'])
# con = (df['first'] == 'Jane') & (df['last'] == 'Doe')
# print(df.loc[con]) # ?To get the same output as line 28 we can write print(df.loc[-con]) also
# print('---------------------')
# con = (df['first'] == 'Jane') | (df['last'] == 'Doe')
# print(df.loc[con]) # ?To get the same output as line 30 we can write print(df.loc[-con]) also
# print('---------------------')
# con = (df['first'] != 'Jane') & (df['last'] != 'Doe')
# print(df.loc[con])
# print('---------------------')
# con = (df['first'] != 'Jane') | (df['last'] != 'Doe')
# print(df.loc[con])

df = pd.read_csv('./StackOverflow Developer Survey/2019/survey_results_public.csv')
# print(df)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', 85)
# df = pd.read_csv('./StackOverflow Developer Survey/2019/survey_results_schema.csv' , low_memory=False)
# print(df)
# high_salary = df['ConvertedComp'] > 70000
# print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])
countries = ['Bangladesh']
# flit = df['Country'].isin(countries)
flit = df['Country'].isin(countries) & df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[flit, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])
