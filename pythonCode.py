#Rene Disotuar
###DataFrames Information#####

######IMPORTANT INFORMATION ABOUT YOUR DATA######################
import pandas as pd
df = pd.read_csv('my_data.csv')
df.head()
df.info()
df.columns
df.describe()
df.shape
df.column.value_counts()
df.column.plot('hist')

#column wise
df.apply(cleaning_function, axis=0)

#row wise
df.apply(cleaning_function, axis=1)

assert(df.column > 0).all()

#combine DataFrame
pd.merge(df2,df2,...)

pd.concat([df1,df2,df3...])


#02/01/2019 Week 4 (Regular Expressions) Python Codes
import re
f = open('../data/scraping.txt')
content = f.readlines()
f.close()

for line in content: #interate through every line
    x = re.findall('[a-zA-Z]+\s[0-9][0-9],\s[0-9]{4}', line)
    #if a date is found
    if len(x) != 0:
        print(x)
##########Part 2#########
import re
f = open('../data/quiz4-scraping.txt')
content = f.readlines()
f.close()

cleanstring = "".join(line.strip().rstrip("\n") for line in content)
print(cleanstring)

pattern = re.compile(r"((10|11|12|13|0?[1-9]):[0-5][0-9] to (10|11|12|13|0?[1-9]):[0-5][0-9] a.m.|p.m.)")
re.findall(pattern, cleanstring)


############ Data Camp Code ###################
# Import the pandas package as pd
import pandas as pd
# Read in the Excel file
sales = pd.read_excel('ticket_sales.xlsx')

# Filter for New York sales only
new_york_sales = sales[sales['theater_location'] == 'New York'].reset_index(drop=True)

# Print the first 5 rows of new_york_sales
print(new_york_sales.head(5))


# Create summary by ticket type
ticket_type_summary = sales.groupby('ticket_type', as_index=False).sum()

# Print ticket_type_summary
print(ticket_type_summary)


# Merge transaction data with the movie data on movie_title
transactions_with_genres = transactions.merge(movies,on='movie_title',how='left' )

# Group by movie_genre and call the sum method
genre_summary = transactions_with_genres.groupby('movie_genre', as_index=False).sum()

# Sort the genre summary by ticket_quantity
genre_summary_sorted = genre_summary.sort_values('ticket_quantity', ascending=False).reset_index(drop=True)

# View the summary
print(genre_summary_sorted)
