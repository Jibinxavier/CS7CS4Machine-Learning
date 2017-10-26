import os
import zipfile
import urllib.request 
import pandas as pd
import reverse_geocoder as rg
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

 

def get_news_dataset():
    zip_f = "data/OnlineNewsPopularity.zip"
    data_folder_path ="data"
    dataset_path = "data/OnlineNewsPopularity/OnlineNewsPopularity.csv"
    if not os.path.exists(dataset_path):
        unzip_data(zip_f,data_folder_path)
        os.remove(zip_f)
    
    df = pd.read_csv(dataset_path)
    return df

def create_classes(row):
    """

    """

  

    if(row[' shares'] <= 140550):
        
        return 0
    elif( row[' shares'] > 140550 and row[' shares'] <= 281101  ):
        print("hewr")
        return 1
    elif( row[' shares'] > 281101 and row[' shares'] <= 421651  ):
         
        return 2
    elif( row[' shares'] > 421651 and row[' shares'] <= 562202  ):
         
        return 3

    elif( row[' shares'] > 562202 and row[' shares'] <= 702752  ):
         
        return 4
    else:
        
        return 5


 
# wget.download("https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#")

# "https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#"