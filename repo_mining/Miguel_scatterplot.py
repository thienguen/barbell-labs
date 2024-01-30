import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import random
import math # for floor function for generating colors
import csv
import datetime

# We NOT getting done >:)

# Make a color generator to let us plot variable colors

# Start by loading actual relevant information from the commit_info file made using authorsFileTouches

# plt.scatter info takes two args(list of x, list of corresponding)
# x axis is the file itself, make a list of files uniquely
# y axis should be the week it was touched + author correspondingly. use author info to get the color
uniqueFiles = []
uniqueAuthors = []
uniqueColors = [] # should have same amount of things as the authors
# Generate the list of unique files, iterate through the entirety of earlier generated csv file to make it work
with open('data/commit_info_rootbeer.csv') as rFile:
    count = 0
    cFile = csv.DictReader(rFile) # lets us use the entire file as a dict, take filenames
    for row in cFile:
        # Check to make sure no repeats. 
        if not row['Filename'] in uniqueFiles:
            # append to list
            uniqueFiles.append(row['Filename'])
        if not row['Author'] in uniqueAuthors:
            uniqueAuthors.append(row['Author'])

# Generate colors for all of the unique authors, just make a dictionary with values
# Just have unique files and authors at this point, can create colors for each author
for x in uniqueAuthors:
    # Just create a unique color for each author. Probably won't be too unique but meh
    print(x)


# Set the labels and axes + legend before finally plotting
plt.xlabel('file')
plt.ylabel('weeks')
plt.legend(loc='upper left', title='Authors', bbox_to_anchor=(1,1))

# Actually plot the graph now
plt.show()