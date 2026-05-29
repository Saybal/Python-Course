import pandas as pd

# Some columns in our CSV contain multiple data types instead of one consistent type.

# For example, a column may contain:

# 123
# 456
# hello
# 789

# Here:

# 123, 456, 789 → numbers
# hello → string/text

# Pandas gets confused because it expects a column to usually have one consistent type.

# ?Why It Happens

# Your dataset:

# survey_results_public.csv

# is huge and contains messy real-world survey data.

# When pandas reads large CSV files, it loads them in chunks (low_memory=True by default). During chunk processing, it detects mixed types and shows this warning.

# TODO: What low_memory=False Does

# It tells pandas:

# “Read the whole file first before deciding column data types.”

# So pandas becomes more accurate and stops warning you.

# df = pd.read_csv('./StackOverflow Developer Survey/survey_results_public.csv', low_memory=False)
# pd.set_option('display.max_columns', 172)
# print(df)
# print(df.shape)
# print(df.info())

# schema_df = pd.read_csv('./StackOverflow Developer Survey/survey_results_schema.csv', low_memory=False)
# pd.set_option('display.max_rows', 172)
# print(schema_df)
# print(df.head()) #Shows first 5 rows of dataset (By default)
# print(df.head(10)) #Shows first 10 rows of dataset
# print(df.tail())#Shows last 5 rows of dataset
# print(df.tail(10))  #Shows last 10 rows of dataset



