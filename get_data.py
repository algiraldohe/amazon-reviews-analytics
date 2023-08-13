import kaggle
import configparser
import os


# Create a ConfigParser object
config = configparser.ConfigParser()

# Load the configuration file
config.read('parameters.config')

# Get dataset name from the configuration file
download_path = config.get('DATA', 'download_path')

# Check if the folder exists
if not os.path.exists(download_path):

    # Get dataset name from the configuration file
    dataset_name = config.get('DATA', 'dataset_name')

    # Set up the Kaggle API
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path="./data", unzip=True)
    print("Data Downloaded")

print(f"Data Already Exists in {download_path}")













