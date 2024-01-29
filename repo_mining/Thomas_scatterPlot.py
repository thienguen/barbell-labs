import matplotlib
import matplotlib.pyplot as pyplot
import matplotlib.colors as colors
import numpy as np
import csv
import datetime

# Read in the data from "commits_rootbeer.csv" file
files = []
authors = []
date_string = []
with open('data/commits_rootbeer.csv') as rootbeer:
    csv_file = csv.DictReader(rootbeer)
    for row in csv_file:
        files.append(row['Filename'])
        authors.append(row['Author'])
        date_string.append(row['Date'])

# Create array of dates
dates = []
init_date = datetime.date(datetime.MAXYEAR, 12, 31)
for tmp_date in date_string:
    if tmp_date:
        ref_date = tmp_date[:10].split('-')
        ref_date = [int(i) for i in ref_date]
        date = datetime.date(ref_date[0], ref_date[1], ref_date[2])
        if (date < init_date):
            init_date = date
        dates.append(date)

weeks = []
for tmp_date in dates:
    datedelta = tmp_date - init_date
    weeks.append(datedelta.days / 7)

# Create array of authors
authors_uniq = []
for tmp_auth in authors:
    if tmp_auth not in authors_uniq:
        authors_uniq.append(tmp_auth)

cmap = matplotlib.pyplot.get_cmap('tab20')
colors_list = []
norm = colors.Normalize(0, len(authors_uniq) - 1)
for tmp_auth in authors:
    val = norm(authors_uniq.index(tmp_auth))
    colors_list.append(cmap(val))

# Create array of colors
colors_uniq = []
for tmp_colors in colors_list:
    if tmp_colors not in colors_uniq:
        colors_uniq.append(tmp_colors)

files_uniq = []
for tmp_file in files:
    if tmp_file not in files_uniq:
        files_uniq.append(tmp_file)

file_ID = [files_uniq.index(tmp_file) + 1 for tmp_file in files]

#  Create a dictionary showing authors, files, and weeks
dcty = dict()
for tmp_file, tmp_weeks, tmp_colors, tmp_auth in zip(file_ID, weeks, colors_list, authors):
    dcty[tmp_auth] = dcty.get(tmp_auth, {'files': [], 'week': [], 'color': tmp_colors})
    dcty[tmp_auth]['files'].append(tmp_file)
    dcty[tmp_auth]['week'].append(tmp_weeks)


# Display graph with information
pyplot.figure(figsize=(20, 20))
fig, plot = pyplot.subplots()
max_week = max([max(dcty[auth]['week']) for auth in dcty])
for tmp_auth in authors_uniq:
    plot.scatter(dcty[tmp_auth]['files'], dcty[tmp_auth]['week'], color=dcty[tmp_auth]['color'], label=tmp_auth)
plot.legend(loc='upper left', title='Authors', bbox_to_anchor=(1, 1))
plot.grid(True)
x_ticks = np.arange(1, np.max(file_ID)+1, 1)
plot.set_xticks(x_ticks)
y_ticks = np.arange(0, max_week+1, 25)
plot.set_yticks(y_ticks)
plot.set_xlabel('Files (By ID Number)')
plot.set_ylabel('Times Worked (By Week Number)')
pyplot.show()