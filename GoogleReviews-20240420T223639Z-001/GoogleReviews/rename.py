import os
import pandas as pd

def rename_files_with_park_names(directory, excel_path):
    # Read the Excel file into a DataFrame
    parks_df = pd.read_excel(excel_path)
    park_id_name_map = dict(zip(parks_df['Google ID'], parks_df['Park Name']))
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Rename each file
    for file in files:
        file_path = os.path.join(directory, file)
        
        # Extract the Google ID from the filename
        google_id = file.split('_')[0]
        
        # Find the correct park name using the Google ID
        if google_id in park_id_name_map:
            new_name = "{}~~~{}.xls".format(google_id, park_id_name_map[google_id])
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print("Renamed '{}' to '{}'".format(file, new_name))
        else:
            print("No matching park name found for '{}'".format(file))

# Example usage:
directory = 'C:\\Users\\edelmel1\\Dropbox (UNC Charlotte)\\VUB\\parkReviews\\GoogleReviews'
excel_path = 'C:\\Users\\edelmel1\\Dropbox (UNC Charlotte)\\VUB\\parkReviews\\GoogleReviews\\listParks.xls'
rename_files_with_park_names(directory, excel_path)
