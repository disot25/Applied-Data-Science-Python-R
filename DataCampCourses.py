#Rene Disotuar
###DataFrames Information#####

print(df.dtypes)
print(df.head())
print(df.info())

#################### CODE FROM DATACAMP PYTHON COURSES#####################
################## import pandas as pd ###################################
################# is assumed for datacamp work######################



############################TIDYING DATA##################################
####Using Melt############
print(airquality.head())
airquality_melt = pd.melt(frame=df, id_vars=['Month', 'Day'])
print(airquality_melt)



print(airquality.head())
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
print(airquality_melt.head())



########Using Pivot##############
print(airquality_pivot.index)
# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()
print(airquality_pivot_reset.index)
print(airquality_pivot_reset.head())



#####################Pivot Table################
# Pivot table the airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)
print(airquality_pivot.head())

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()
print(airquality_pivot.head())
print(airquality.head())


#######Melt and Str###############
# Melt tb: tb_melt
tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])
# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]
# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:4]
print(tb_melt.head())


################################Cleainig DATA######################3####
# Concatenate uber1, uber2, and uber3: row_concat

row_concat = pd.concat([uber1,uber2,uber3])
print(row_concat)
print(row_concat.head())



# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')
print(m2o)


# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')
# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')
print(m2m.head(20))


# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')
# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')
print(tips.info())


#############USING REGULAR EXPRESSIONGS##################
##########################################################
# Import the regular expression module
import re
# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))


import re
# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(matches)


# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)


# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    # Return 1 if gender is 'Male'
    elif gender == 'Male':
        return 1
    # Return np.nan
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)
print(tips.head())


# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])
print(tips.head())


#############WORKING WITH MISSING VALUES###################################
###########################################################################
#Info to see Missing Values
# Create the new DataFrame: tracks
tracks = billboard[['year','artist','track','time']]
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()
print(tracks_no_duplicates.info())

#Fill Missing Values
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality['Ozone'].mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)
print(airquality.info())



#########################PLOTING GRAPHS#################################
########################SAVING TO CSV FILE################################
# Import matplotlib.pyplot
        import matplotlib.pyplot as plt

        # Create the scatter plot
        g1800s.plot(kind='scatter', x='1800', y='1899')

        # Specify axis labels
        plt.xlabel('Life Expectancy by Country in 1800')
        plt.ylabel('Life Expectancy by Country in 1899')

        # Specify axis limits
        plt.xlim(20, 55)
        plt.ylim(20, 55)

        # Display the plot
        plt.show()

############################Using Assert############################

        def check_null_or_valid(row_data):
            #Function that takes a row of data,
            #drops all missing values,
            #and checks if all remaining values are greater than or equal to 0

            no_na = row_data.dropna()
            numeric = pd.to_numeric(no_na)
            ge0 = numeric >= 0
            return ge0

        # Check whether the first column is 'Life expectancy'
        assert g1800s.columns[0] == 'Life expectancy'

        # Check whether the values in the row are valid
        assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

        # Check that there is only one instance of each country
        assert g1800s['Life expectancy'].value_counts()[0] == 1


        # Concatenate the DataFrames row-wise
        gapminder = pd.concat([g1800s,g1900s,g2000s])

        # Print the shape, head of gapminder
        print(gapminder.shape)
        print(gapminder.head())



#########################PLOTING#####################
# Add first subplot
plt.subplot(2, 1, 1)

# Create a histogram of life_expectancy
gapminder.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot(kind='line')
gapminder.life_expectancy.plot(kind='hist')

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')




import pandas as pd
# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')
# Rename the columns
gapminder_melt.columns = ['country','year','life_expectancy']
# Print the head of gapminder_melt
print(gapminder_melt.head())

###############################
# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64

###############################################
# Create the series of countries: countries
countries = gapminder['country']

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)

#######################################################
# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all()

# Drop the missing values
gapminder = gapminder.dropna()

# Print the shape of gapminder
print(gapminder.head())
