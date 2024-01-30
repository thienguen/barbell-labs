import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import csv
import datetime


files = []
authors = []
datesString = []
with open('data/commits_rootbeer.csv') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        files.append(row['Filename'])
        authors.append(row['Author'])
        datesString.append(row['Date'])


dates = []
init_date = datetime.date(datetime.MAXYEAR, 12, 31)
for d in datesString:
    if d:
        d_ = d[:10].split('-')
        d_ = [int(i) for i in d_]
        date = datetime.date(d_[0], d_[1], d_[2])
        if (date < init_date):
            init_date = date
        dates.append(date)

weeks = []
for d in dates:
    datedelta = d - init_date
    weeks.append(datedelta.days / 7)


authorsUnique = []
for a in authors:
    if a not in authorsUnique:
        authorsUnique.append(a)

cmap = matplotlib.pyplot.get_cmap('tab20')
colorsList = []
norm = colors.Normalize(0, len(authorsUnique) - 1)
for a in authors:
    val = norm(authorsUnique.index(a))
    colorsList.append(cmap(val))

# Create a list of unique colors
colorsUnique = []
for c in colorsList:
    if c not in colorsUnique:
        colorsUnique.append(c)

filesUnique = []
for f in files:
    if f not in filesUnique:
        filesUnique.append(f)

fileID = [filesUnique.index(f) + 1 for f in files]

#  Create a dictionary of authors and their files and weeks
touches = dict()
for f, w, c, a in zip(fileID, weeks, colorsList, authors):
    touches[a] = touches.get(a, {'files': [], 'week': [], 'color': c})
    touches[a]['files'].append(f)
    touches[a]['week'].append(w)


# Display
plt.figure(figsize=(20, 20))
fig, ax = plt.subplots()
for a in authorsUnique:
    ax.scatter(touches[a]['files'], touches[a]['week'], color=touches[a]['color'], label=a)
ax.legend(loc='upper left', title='Authors', bbox_to_anchor=(1, 1))
ax.grid(True)
plt.show()