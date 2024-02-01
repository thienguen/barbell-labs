import csv
import random
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from collections import defaultdict

# used to parse in the data of the .csv file
files, authors, dates = [], [], []

# used to further process the data of the .csv file in order to display the data in a scatterplot
number_of_weeks, single_author_appearances, single_file_appearances, single_file_mapping, color_list = [], [], [], [], []

unique_author_set = set()
unique_colors_set = set()

# parsing the .csv file and using three lists to parse in the name of the files, the name of the authors and
# the date in which the files were last touched
with open('data/commits_rootbeer.csv') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        files.append(row['File'])
        authors.append(row['Author'])
        dates.append(row['Date'])

# taking the list of files and making sure that ONLY unique file names are present
# furthermore, we are mapping the unique files to an integer to be able to represent them in the scatterplot
for current_file in files:
    if current_file not in single_file_appearances:
        single_file_appearances.append(current_file)
    single_file_mapping.append(single_file_appearances.index(current_file) + 1)

# taking the list of authors and making sure that ONLY unique author names are present by using set()
for current_element_author in authors:
    unique_author_set.add(current_element_author)
# converting the set() back to a list[]
single_author_appearances = list(unique_author_set)

# taking the first 10 characters of the current date (represented as a string) and then using '-' as
# its delimiter and then converting the string date into an integer date
dates = [datetime.date(*map(int, d[:10].split('-'))) for d in dates if d]
# finding the earliest date of the project, which represents when the project was first started
project_creation_date = min(dates, default=datetime.date(3000, 12, 31))
# calculating the number of weeks it has been from from the current file date and project creation date
for current_element_date in dates:
    number_of_weeks.append((current_element_date - project_creation_date).days / 7)

# generating random unique colors for every unique author present (this part is cool because every time the program is
# executed, a new set of colors is used to display the scatterplot on the current iteration of the program)
# we then assign the current author a random color that will be used to represent them in the scatterplot
for current_author in authors:
    while True:
        # generate a random color
        random_color = matplotlib.colors.to_hex([random.random(), random.random(), random.random()])
        # check if the current random color exists in the color set
        if random_color not in unique_colors_set:
            # if the current random color doesn't exist, add it to the set
            unique_colors_set.add(random_color)
            # add the current random color to the list of colors we are going to assign to the authors
            color_list.append(random_color)
            break

author_color_dict = dict(zip(authors, color_list))

# using three lists to help us bring all of the relevant information together for the authors and then displaying
# the information to the scatterplot
files_by_author = defaultdict(list)
weeks_by_author = defaultdict(list)
colors_by_author = dict(zip(single_author_appearances, color_list))

# accessing the files and weeks associated with each author and retrieving the associated
# information with each of the authors
for current_index in range(len(authors)):
    current_author = authors[current_index]
    current_file = single_file_mapping[current_index]
    current_weeks = number_of_weeks[current_index]

    files_by_author[current_author].append(current_file)
    weeks_by_author[current_author].append(current_weeks)

# display the contents of the above three lists in the form of a scatterplot
fig, ax = plt.subplots(figsize=(10, 10))

# giving some labels for the title, x-axis and y-axis to help interpret the scatterplot better
ax.set_title('Visual Representation of The Authors and Their Contributions')
ax.set_xlabel('File Number')
ax.set_ylabel('Number of Weeks From Project Creation Date')

# taking the associated information of the current author (files touched, weeks passed, author color) and plotting the point on the scatterplot
for current_author in single_author_appearances:
    ax.scatter(files_by_author[current_author], weeks_by_author[current_author], color=colors_by_author[current_author], label=current_author)

# displaying the list of authors who contributed and their associated plot color
ax.legend(loc='upper right', title='List of Authors')
plt.show()