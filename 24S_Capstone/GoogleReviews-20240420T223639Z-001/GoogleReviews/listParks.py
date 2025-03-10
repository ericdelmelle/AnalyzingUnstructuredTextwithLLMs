import os

# Set the directory you want to start from
dir_path = 'C:\\Users\\edelmel1\\Dropbox (UNC Charlotte)\\VUB\\parkReviews\\GoogleReviews'
output_file = 'C:\\Users\\edelmel1\\Dropbox (UNC Charlotte)\\VUB\\parkReviews\\GoogleReviews\\listParks.txt'

# Create a list to hold the file names
csv_files = []

# Loop through the directory
for file in os.listdir(dir_path):
    if file.endswith(".csv"):
        csv_files.append(file)

# Write the list to a text file
with open(output_file, 'w') as f:
    for item in csv_files:
        f.write("%s\n" % item)

print("CSV file names have been saved to", output_file)
