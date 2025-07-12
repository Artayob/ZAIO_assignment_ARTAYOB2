import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("imdb_top_1000.csv", delimiter=',')

missing_percent = (df.isnull().sum() / len(df)) * 100
print("Missing Values (%):\n", missing_percent)
df.dropna(subset=['Gross', 'IMDB_Rating'], inplace=True)
df['Duration'] = df['Runtime'].str.extract('(\d+)').astype(float)
df['Decade'] = (pd.to_numeric(df['Released_Year'], errors='coerce') // 10) * 10
df['Lead_Actors'] = df[['Star1', 'Star2', 'Star3', 'Star4']].fillna('').agg(', '.join, axis=1)
print(df)
print(df.head())
def visualizer():
    # Histogram: IMDB Rating vs Meta_score
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

    # Top 10 Genres
    top_genres = df['Genre'].value_counts().nlargest(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_genres.index, y=top_genres.values)
    plt.title('Top 10 Genres')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # # Scatter: Gross vs Votes
    # plt.figure(figsize=(10,5))
    # sns.scatterplot(data=df, x='Gross', y='No_of_Votes')
    # plt.title('Gross vs Number of Votes')
    # plt.tight_layout()
    # plt.show()

    # Boxplot: IMDB Rating by Certificate
    plt.figure(figsize=(10,5))
    sns.boxplot(data=df, x='Certificate', y='IMDB_Rating')
    plt.title('IMDB Rating by Certificate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print(visualizer())
