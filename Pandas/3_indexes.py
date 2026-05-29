import pandas as pd

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

#! Setting our own index
#Using People dictionary. We can use email as index, since it is unique.
# print(df.set_index('email')) #It just show the email as index. Do not change the actual table format
# print('--- See the second df is remained same as it was ---- ')
# print(df) #See the df is remained as it was.
# df.set_index('email', inplace=True) #It will change the actual dataframe
# print('---- Now the df has changed ----')
# print(df)
# print(df.loc['JohnDoe@email.com'])
# df.reset_index(inplace=True) #To back to default index

#! Setting Our Own Index in StackOverflow dataset
# df = pd.read_csv('./StackOverflow Developer Survey/survey_results_public.csv', low_memory=False)
# df.set_index('ResponseId', inplace=True)
# df = pd.read_csv('./StackOverflow Developer Survey/survey_results_public.csv', low_memory=False, index_col='ResponseId') #We use this also
# print(df)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('./StackOverflow Developer Survey/survey_results_schema.csv', low_memory=False, index_col='qname')
print(df.sort_index())
# print(df.loc['TechEndorse_1', ['question']])