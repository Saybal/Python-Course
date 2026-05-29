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

df = pd.read_csv('./StackOverflow Developer Survey/survey_results_public.csv', low_memory=False)
print(df)