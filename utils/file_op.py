import requests
import shutil
import os

download_folder = "E:/e-Books/_allitebooks/"


def download_file(url, category, file_name):
    category_path = download_folder + category + '/'
    if not os.path.isdir(category_path):
        os.makedirs(category_path)
    file_path = category_path + file_name
    stream_file = requests.get(url, stream=True)
    if os.path.isfile(file_path):
        print("Skipping existing " + category + '/' + file_name)
        return False
    print("Downloading " + category + '/' + file_name)
    with open(file_path, 'wb') as out_file:
        shutil.copyfileobj(stream_file.raw, out_file)
    del stream_file
    return True


def rm(filename):
    os.remove(filename)

def rmd(directory):
    os.rmdir(directory)
