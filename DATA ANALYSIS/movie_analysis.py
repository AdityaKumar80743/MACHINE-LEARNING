import pandas as pd 
import matplotlib.pyplot as plt 

# ---------- data cleaning
df = pd.read_csv("movies.csv")
# print(df.head())
print(df.isnull().sum())

# remove duplicates
df = df.drop_duplicates()

# remove NaN movie names
df = df.dropna()

# convert movie duration to int type
# convert to int
# fill NaN with 0
hours = df['Duration'].str.extract(r'(\d+)\s*h')[0].fillna(0).astype(int)
minutes = df['Duration'].str.extract(r'(\d+)\s*m')[0].fillna(0).astype(int)
df['Duration'] = hours * 60 + minutes

# convert number of rators to int
df["Number of Rators"] = df["Number of Rators"].str.extract(r'\((\d+)\s*K\)')[0].fillna(0).astype(int) * 1000

# fill 0 with mean value
df = df.fillna(df.mean().astype(int))
df = df.replace(0, df.mean())

print(df.isnull().sum())


# ------------- data visualisation

# movies duration histogram
plt.figure(figsize=(6,4))
plt.hist(df['Duration'], bins=30, edgecolor="black", color='teal')
plt.title("Movies Duration Distribution")
plt.xlabel('Duration in mins')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig("movies_duration_histogram.png", dpi = 300)
# plt.show()

# conclusino
print('most of the movies are of 140 mins)

# releases per year
release_year = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10,12))
plt.plot(release_year.index, release_year.values, marker="o", color="orange")
plt.title("Movies Release Year Comparison")
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.savefig("movies_release_bargraph.png", dpi = 300)
# plt.show()

#  conclusion
print("In Year 2023 most movies were released")

# top 10 rated moveies
# colors
tableau_colors = [
    'tab:blue', 
    'tab:orange', 
    'tab:green', 
    'tab:red', 
    'tab:purple', 
    'tab:brown', 
    'tab:pink', 
    'tab:gray', 
    'tab:olive', 
    'tab:cyan'
]
top_movies = df.sort_values(by='Ratings', ascending=True).tail(10)
plt.figure(figsize=(8,5))
plt.barh( top_movies['Film Name'], top_movies['Ratings'], color=tableau_colors)
plt.title("Top 10 Rated Movies")
plt.xlabel('Rating')
plt.ylabel('Movies')
plt.tight_layout()
plt.savefig("top_10_movies_bargraph.png", dpi = 300)
plt.show()

# conclusion
print('4 movies have rating 9.9')
