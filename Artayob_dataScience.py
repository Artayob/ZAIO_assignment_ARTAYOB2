import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("imdb_top_1000.csv", delimiter= ',')

def missing_values():
    missing_percet = (df.isnull().sum() / len(df)) * 100
    print("Missing Values in %: \n", missing_percet)
df.dropna(subset=["Gross", "IMDB_Rating"], inplace=True)


def remove_duplicates(df):
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"Found {duplicate_count} duplicate row(s). Removing them...")
        df = df.drop_duplicates()
    else:
        print("No duplicates found.")
    return df


df['Duration'] = df['Runtime'].str.extract('(\d+)').astype(float)
df['Decade'] = (pd.to_numeric(df['Released_Year'], errors='coerce') // 10) * 10
df['Lead_Actors'] = df[['Star1', 'Star2', 'Star3', 'Star4']].fillna('').agg(', '.join, axis=1)

class Visualizer:
    def __init__(self, df):
        self.df = df

    def histogram(self):
        plt.figure(figsize=(10,5))
        sns.histplot(data=df, x='IMDB_Rating', bins=20, kde=True)
        plt.title('IMDB Rating Distribution')
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10,5))
        sns.histplot(data=df, x='Meta_score', bins=20, kde=True)
        plt.title('Meta Score Distribution')
        plt.tight_layout()
        plt.show()
    
    def Bar_plot(self):
        top_genres = df['Genre'].value_counts().nlargest(10) 
        plt.figure(figsize=(10,5))
        sns.barplot(x=top_genres.index, y=top_genres.values)
        plt.title('Top 10 Genres')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def scatter_plot(self):
        plt.figure(figsize=(10,5))
        sns.scatterplot(data=df, x='Gross', y='No_of_Votes')
        plt.title('Gross vs Number of Votes')
        plt.tight_layout()
        plt.show()

    def Box_plot(self):
        plt.figure(figsize=(10,5))
        sns.boxplot(data=df, x='Certificate', y='IMDB_Rating')
        plt.title('IMDB Rating by Certificate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def descriptive_statistics():

    df['Gross'] = df['Gross'].replace('[\$,]', '', regex=True) 
    df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')   


    columns = ['Gross', 'No_of_Votes', 'IMDB_Rating']
    stats = {}

    for col in columns:
        df[col] = pd.to_numeric(df[col], errors= 'coerce')
        stats[col]={
            'Mean': float(df[col].mean()),
            'Median': float(df[col].median()),
            'Standard Deviation': float(df[col].std())
        }
    print("Descriptive Statistics: \n", stats)
    return stats

def correlation():
    def __init__(self, df):
        self.df = df
    corr = df[['Gross', 'No_of_Votes']].corr(method='pearson')
    print("Correlation between Gross and No_of_Votes:\n", corr)

class Highest_Gross:
    def __init__(self, df):
        self.df = df

    def Top_5_Directors(self):
        df['Gross'] = df['Gross'].replace('[\$,]', '', regex=True) 
        df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce') 
        
        avg_gross_by_director = df.groupby('Director')['Gross'].mean()
        top_directors = avg_gross_by_director.sort_values(ascending=False)
        print("Top 5 Directors by Average Gross: \n", top_directors)
    
    def Plot_of_top5_directors(self):
        avg_gross_by_director = df.groupby('Director')['Gross'].mean()
        top_directors = avg_gross_by_director.sort_values(ascending=False).head(5)

        plt.figure(figsize=(8, 5))
        top_directors.plot(kind='bar', color='gold')
        plt.title('Top 5 Directors by Average Gross')
        plt.xlabel('Director')
        plt.ylabel('Average Gross (USD)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()  


loadingCSV = df.to_csv("Cleaned_imdb_top_1000.csv", index= False)
missing_values()
print(df.columns.tolist())
print(remove_duplicates(df))
print(df)
visualizing = Visualizer(df)
visualizing.histogram()
visualizing.Bar_plot()
visualizing.scatter_plot()
visualizing.Box_plot()
descriptive_statistics()
correlation()
highest = Highest_Gross(df)
highest.Top_5_Directors()
highest.Plot_of_top5_directors()