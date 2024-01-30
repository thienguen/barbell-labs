import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import csv
import datetime
import random
from datetime import date
##########################################################
def generate_random_color():
  return "#{:06x}".format(random.randint(0, 0xFFFFFF))
##########################################################
def map_author_to_color(authors):
  author_color_map = {}
  for author in set(authors):
    author_color_map[author] = generate_random_color()
  return author_color_map
##########################################################
def map_file_to_number(files):
  file_to_integer_mapping = {}
  integer_counter = 0
  for file in files:
    if file not in file_to_integer_mapping:
      file_to_integer_mapping[file] = integer_counter
      integer_counter += 1
  
  files_mapped = []

  for i in range(len(files)):
    files_mapped.append(file_to_integer_mapping[files[i]])

  return files_mapped
##########################################################
def weeks_between(d1, d2):
  d1 = date.fromisoformat(d1)
  d2 = date.fromisoformat(d2)
  days_difference = (d2 - d1).days

  return days_difference//7
##########################################################
authors = []
files = []
dates = []

with open('data/commits_rootbeer.csv') as file:
  csvFile = csv.DictReader(file)
  for row in csvFile:
    authors.append(row['Author'])
    files.append(row['File'])
    dates.append(row['Date'])

author_color_map = map_author_to_color(authors)
files_map = map_file_to_number(files)

for i in range(len(dates)):
  dates[i] = dates[i][:10]

# (weeks, file, author) format
entries = []
for i in range(len(dates)):
  weeks = weeks_between(dates[-1], dates[i])
  entries.append((weeks, files_map[i], authors[i]))
  print(entries[i])

weeks_data, files_data, authors_data = zip(*entries)

# Map authors to colors
author_colors = [author_color_map[author] for author in authors_data]

# Plotting the scatter plot
plt.scatter(files_data, weeks_data, c=author_colors, cmap='viridis', alpha=0.8, edgecolors='w')

# Adding labels and title
plt.ylabel('Weeks')
plt.xlabel('Mapped File Number')
plt.title('Scatter Plot of Weeks, Mapped File Number, and Author')

# Show the color legend
for author, color in author_color_map.items():
    plt.scatter([], [], c=color, label=author)

plt.legend(loc='upper right', title="Authors")

# Show the plot
plt.show()