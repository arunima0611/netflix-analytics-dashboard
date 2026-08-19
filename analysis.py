import pandas as pd

def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    df.fillna("Unknown", inplace=True)
    return df

def content_by_type(df):
    return df['type'].value_counts()

def top_countries(df):
    return df['country'].value_counts().head(10)

def content_growth(df):
    df['year_added'] = df['date_added'].str.extract(r'(\d{4})')
    return df['year_added'].value_counts().sort_index()

def top_genres(df):
    return df['listed_in'].str.split(', ').explode().value_counts().head(10)