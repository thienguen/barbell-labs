# Elliot Wesoff
# 1008247148
# CS 472 - Git and Gitlab
# elliot_authorFilesTouches.py

# we want to aggregate the data by file => author => dates.
# maybe something like:
# {
#       'author1': [date1, date2, ...],
#       'author2': [date3, date4, ...],
#       ...
# }
#
# with this format, we can (somewhat) easily write a csv or json
# file, which will be read by elliot_scatterplot.py, and then
# read, parse, and process the data to the plotting library.

# example scatterplot: https://stackoverflow.com/questions/8202605/matplotlib-scatterplot-color-as-a-function-of-a-third-variable

import json
from datetime import datetime
from math import floor


data = {}
authors = []
timestamps = []

with open('data/commits_rootbeer.csv', 'r') as f:
    rootbeer_commits = f.read()

commits_lines = rootbeer_commits.split('\n')
commits_lines = commits_lines[2:]
filtered_commits = list(filter(lambda s: s != '\t\t', commits_lines))

for line in filtered_commits:
    (filename, author, date) = line.split('\t')
    authors.append(author)
    timestamps.append(datetime.fromisoformat(date))

timestamps.sort()
earliest_commit = timestamps[0]

for line in filtered_commits:
    (filename, author, date) = line.split('\t')
    dt = datetime.fromisoformat(date)
    week = floor((dt - earliest_commit).days / 7)
    if filename in data:
        if author in data[filename]:
            data[filename][author].append(week)
        else:
            data[filename][author] = [week]
    else:
        data[filename] = {}

with open('data/scatterplot_data.json', 'w') as f:
    f.write(json.dumps(data))

