from helper import get_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_SET_URL = ["https://www.dropbox.com/sh/euppz607r6gsen2/AACYNkq6O4UEjacsBy6FhT6La/Wine%20Quality%20Ratings%20and%20Chemicals?dl=1"]
DATA_SET = "./data/winequality-white.csv"
def plot_features(train):
    colormap = plt.cm.viridis
    plt.figure(figsize=(14,12))
    plt.title('Pearson Correlation of Features', y=1.05, size=15)
    sns.heatmap(train.astype(float).corr(),linewidths=0.5,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.show()
def main():
    get_data(DATA_SET_URL)
    data = pd.read_csv(DATA_SET, delimiter=";")
    plot_features(data)

if __name__ == "__main__":
    main()
