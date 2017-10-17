import os
import zipfile
import urllib.request
def unzip_data(zip_f):
    """
        unzips files into data folder
    """
    data_folder_path = "data"

    with zipfile.ZipFile(zip_f,"r") as zip_ref:
            zip_ref.extractall(data_folder_path)
             
def download(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()
 
    with open("test_file.zip", "wb") as f :
        f.write(data)


def get_data(urls):
    data_folder_path = "data"

    
    if not os.path.exists(data_folder_path):

        os.makedirs(data_folder_path) # create a data folder

        for url in urls:  # download files from dropbox one by one
            download(url)
            unzip_data("test_file.zip")
        os.remove("test_file.zip")
# wget.download("https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#")

# "https://www.dropbox.com/sh/euppz607r6gsen2/AABABUTdx7YqCeBquA1Ky7z8a/The%20SUM%20dataset?dl=1#"