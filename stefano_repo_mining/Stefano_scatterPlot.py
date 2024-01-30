import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import csv

# used to parse the data of the .csv file
files, authors, dates = [], [], []

# used to further process the parsed. csv data
single_file_appearances, single_file_mapping = [], []

# parsing the .csv file data into three different lists to further process the raw data
with open('data/commits_rootbeer.csv') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        files.append(row['File'])
        authors.append(row['Author'])
        dates.append(row['Date'])

# taking the list of files and making sure that ONLY unique file names are present by using set
# furthermore, we are mapping the unique files to an integer to be able to represent them in the scatterplot
for current_file in files:
    if current_file not in single_file_appearances:
        single_file_appearances.append(current_file)
    single_file_mapping.append(single_file_appearances.index(current_file) + 1)