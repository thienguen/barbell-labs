import pdb
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

authors = {}
filenames = []
marker_size = 10

with open('data/scatterplot_data.json', 'r') as f:
    scatterplot_data = json.loads(f.read())

for filename, author_data in scatterplot_data.items():
    if filename not in filenames:
        filenames.append(filename)

    filename_i = filenames.index(filename)

    for author, weeks in author_data.items():
        if author not in authors:
            color = (np.round(np.random.rand(),1),
                    np.round(np.random.rand(),1),
                    np.round(np.random.rand(),1))
            authors[author] = color
        
        for week in weeks:
            plt.scatter(filename_i, week, color=authors[author], s=marker_size)

plt.legend = [mpatches.Patch(color=color, label=author) for author, color in authors.items()]
plt.xlabel('file')
plt.ylabel('weeks')
plt.show()

plot_filename = 'data/rootbeer_plot.png'
print('saving plot to file: ' + plot_filename)
plt.savefig(plot_filename)

