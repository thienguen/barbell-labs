import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

authors = {}

with open('data/scatterplot_data.json', 'r') as f:
    scatterplot_data = json.loads(f.read())

filenames = list(scatterplot_data.keys())

for i in range(len(filenames)):
    filename = filenames[i]
    author_data = scatterplot_data[filename]

    for author, weeks in author_data.items():
        if author not in authors:
            authors[author] = {}
            authors[author]['weeks'] = []
            authors[author]['files'] = []
            authors[author]['color'] = (np.round(np.random.rand(),1),
                                        np.round(np.random.rand(),1),
                                        np.round(np.random.rand(),1))

        for week in weeks:
            authors[author]['weeks'].append(week)
            authors[author]['files'].append(i)

for author, data in authors.items():
    plt.scatter(data['files'], data['weeks'], label=author, color=data['color'])

plt.legend(loc='upper left', title='Authors', bbox_to_anchor=(1, 1))
plt.xlabel('file')
plt.ylabel('weeks')
plt.show()

plot_filename = 'data/rootbeer_plot.png'
print('saving plot to file: ' + plot_filename)
plt.savefig(plot_filename)

