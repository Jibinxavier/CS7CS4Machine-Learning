import os
import zipfile
import urllib.request
from pyquery import PyQuery as pq
import pandas as pd
def unzip_data(zip_f,data_folder_path):
    """
        unzips files into data folder
    """ 

    with zipfile.ZipFile(zip_f,"r") as zip_ref:
            zip_ref.extractall(data_folder_path)
             
def download(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()
 
    with open("temp_file.zip", "wb") as f :
        f.write(data)


def get_data(urls):
    data_folder_path = "data"

    
    if not os.path.exists(data_folder_path):

        os.makedirs(data_folder_path) # create a data folder

        for url in urls:  # download files from dropbox one by one
            download(url)
            unzip_data("temp_file.zip", data_folder_path)
        os.remove("temp_file.zip")



def get_census_column_names(path="./data/census-income.data.html"):
    page = pq(filename=path)
  
    column = page("PRE").eq(2).text()
    column = column.splitlines()

    column_names = []
    for c in column:
        column_names.append(c.split('\t')[0])
    
    return column_names
def get_census_dataset():
    zip_f = "data/census-income-data-combined.zip"
    data_folder_path ="data"
    dataset_path = "data/census-income-data-combined.csv"
    unzip_data(zip_f,data_folder_path)
    column_names = get_census_column_names()
    df = pd.read_csv(dataset_path, names=column_names)
    return df


# wget.download("https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#")

# "https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#"