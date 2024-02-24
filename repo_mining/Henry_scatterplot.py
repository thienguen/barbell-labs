import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv
import datetime
import numpy as np
import random

# initialize arrays
files = []
dates = []
authors = []

# Append data to respective array
with open('data/authors_rootbeer.csv') as file:
    print()
    reader = csv.DictReader(file)
    for row in reader:
        files.append(row['Filename'])
        authors.append(row['Author'])
        dates.append(row['Date'].split('T')[0]) #Separates date into YYYY-MM-DD
    dates = [datetime.datetime.strptime(row['Date'].split('T')[0], "%Y-%m-%d") for row in reader]  

# Convert Raw Date to Weeks
weeks = []
startDate = datetime.datetime.strptime(dates[-1], "%Y-%m-%d")
for d in dates:
    date = datetime.datetime.strptime(d, "%Y-%m-%d")
    weeks_from_start = (date - startDate).days // 7
    weeks.append(weeks_from_start)
    
# Get unique authors
uniqueAuthors = list(set(authors))

# Dictionary - Key: Author Value: Color from tab20b, Converts cmap[i] to hex
cmap = plt.get_cmap('tab20b')
authcolors = {author: mcolors.to_hex(cmap(i)) for i, author in enumerate(uniqueAuthors)}

# Dictionary - Key: file Value: Number
fileNumber = {file: i for i, file in enumerate(set(files))}
fileNumberArray = [fileNumber[file] for file in files]

plt.xlabel('File')
plt.ylabel('Weeks')

for i, author in enumerate(uniqueAuthors):
    indices = [j for j, a in enumerate(authors) if a == author]
    plt.scatter(np.array(fileNumberArray)[indices], np.array(weeks)[indices], label = author, color = authcolors[author])

plt.legend(loc='upper left', fontsize='x-small', markerscale=0.4)
plt.show()