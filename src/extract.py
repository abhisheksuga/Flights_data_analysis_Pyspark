from kaggle.api.kaggle_api_extended import KaggleApi
from config import *
# Function to download desired dataset from kaggle using kaggle api 
def download_kaggle_dataset(dataset_name ,data_path,unzip=False) :
    try:  
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(dataset_name, data_path, unzip=unzip)
        print (f"dataset download success! find the files in {data_path} folder")
    except Exception as e:
        print (f"error while downloading: {e}")



download_kaggle_dataset('chiyucheng/flight-parquet', data_path='/Users/abhisheksuga/Documents/Edu/projects/flights_data_analysis/Flights_data_analysis_Pyspark/data', unzip=True) 
