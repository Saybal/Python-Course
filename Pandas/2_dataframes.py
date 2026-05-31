import pandas as pd

# #!Creating a dataframe(example: csv file) from dictionary
people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
# print(df)
# print(df['email']) # Generally, in dictionary if we print this, we are supposed to get data in a list format but we will get this in a vertical alignment series because now df['email'] is a pandas series object.
#? A series is multiple rows of a single column. On the other hand, Dataframe is multiple rows of multiple column,simply a table

# print(df[['first','email']])
# print(df.columns) #Shows the name of columns with their datatype.
# print(df.iloc[1]) # For accessing a specific row
# print(df.iloc[[1,2]])
# print(df.iloc[[1,2],2]) # ?df.iloc[[row indexes],[column indexes]]
# print(df.loc[[0,2], ['first','email']])

#!Creating a dataframe(example: csv file) from list
# people_2d_list = [
#     ["First", "Last", "Email"],  # Header
#     ["Corey", "Schafer", "CoreyMSchafer@gmail.com"],
#     ["Jane", "Doe", "JaneDoe@email.com"],
#     ["John", "Doe", "JohnDoe@email.com"]
# ]

# df = pd.DataFrame(people_2d_list)
# print(df)

#! Dealing Datafram with actual stackoverflow data
# df = pd.read_csv('./StackOverflow Developer Survey/survey_results_public.csv', low_memory=False)
# print(df.columns)
# print(df['LearnCode'])
# print(df['DevEnvsChoice'].value_counts()) # Here, we counted number of 'Yes' and 'No'
# print(df.loc[[1]])
# print(df.loc[[1], ['DevEnvsChoice']])
# print(df.loc[[0,1,2,3,4], ['MainBranch', 'Age', 'DevEnvsChoice']])
# print(df.loc[0:4, ['MainBranch', 'Age', 'DevEnvsChoice']])