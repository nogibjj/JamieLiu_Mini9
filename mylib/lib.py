"""
    library file
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'

# check = pd.read_csv(dataset)
# print(check.shape)

def load_dataset():
    df = pd.read_csv(dataset)
    return df

def process_mean(df, col):
    return df[col].mean()

def process_median(df, col):
    return df[col].median()

def process_max(df, col):
    return df[col].max()

def process_min(df, col):
    return df[col].min()

def process_std(df, col):
    return df[col].std()

def bar_visual(df, col, jupyter_render):
    """bar graph of a column over all airlines"""
    x = df['airline']
    y = df[col]
    plt.figure(figsize=(15, 12))
    plt.bar(x, y)
    plt.xlabel('Airlines')
    plt.ylabel(col)
    plt.title(f'{col} over Airlines')
    plt.xticks(rotation=90, fontsize=6)
    if not jupyter_render:
        plt.savefig(f'{col}.png')
    else:
        plt.show()
    # Close the figure to avoid memory warnings
    plt.close()

def hist_visual(df, col, jupyter_render):
    """histogram of a column over all airlines"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[col])
    plt.xlabel(f'Number of {col}')
    plt.ylabel('Frequency')
    plt.title(f'Frequency of {col}')
    if not jupyter_render:
        plt.savefig(f'Frequency_{col}_hist.png')
    else:
        plt.show()
    # Close the figure to avoid memory warnings
    plt.close()