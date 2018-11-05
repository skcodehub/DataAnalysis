# Use this cell to set up import statements for all of the packages that you
#   plan to use.

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline

# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv('tmdb-movies.csv')
df.info()
df.head()

# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
# Check and duplicates and remove, if any
df.duplicated().value_counts()
df.drop_duplicates(inplace=True)

# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
#Find the number of releases in the last 20 years
# It is interesting to the number of movies released in each year to understand the growth in the movie industry
df_last_20 = df[df['release_year'] >= 1998]
ind = df_last_20['release_year'].value_counts().index
df_last_20.sort_index(ascending=True, inplace=True)
df_last_20['release_year'].value_counts()[ind].plot(kind='bar', title='Number of movies released per year', figsize=(8,8));
plt.xlabel('Release Year', fontsize=18)
plt.ylabel('Number of Movies', fontsize=18)

#Top 10 Popular titles in the last 20 years
# I chose last 20 years to keep the graph readable
#This reason I chose to plot this so it could be used as a quick recommendation to viewers under "popular movie" category
df_max_votes = df_last_20.groupby('original_title', sort=False)['vote_count'].max()
df_max_votes.head(10).plot(kind='bar', title='Popular Movies', alpha=.7)
plt.xlabel('Movie Title', fontsize=18)
plt.ylabel('Vote Count', fontsize=18)

# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.

#How did the budget v/s revenue compare in the last 20 years?
#Find average budget and revenue by release year and plot
# This is to understand Return on investment and Rate of Return on movies over the last 20 years
df_rev = df_last_20.groupby('release_year')['budget', 'revenue'].mean()
#Check how data looks
#df_rev.head()
df_rev.plot(kind='bar', title='Average revenue');
plt.xlabel('Release Year', fontsize=18);
plt.ylabel('Amounts in million', fontsize=18);

from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

# Conclusion 1 From this data, it always seemed like the movie revenue was higher than the budget.
# Conclusion 2 It seemed like (except a slight variation), in the last 20 years number of movies released per year is on the rise.
# Limitation1 Movie revenue is not always a true indicator of movie quality because some movies get a lot of interest before it comes out which may drive revenues up.
# Limitation2 From this set of data, it always seemed like the movie average revenue was higher than the budget however in reality that is not be the case always.