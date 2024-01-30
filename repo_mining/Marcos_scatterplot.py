import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import datetime
from collections import defaultdict
from Marcos_authorsFileTouches import mp

start_date = datetime.date(datetime.MAXYEAR, 12, 31)
file_mp = defaultdict(int)
idx_counter, color_counter = 0, 0
file_set = set()
color_mp = defaultdict(int)
color_list = ["#154570", "#290d45", "#23677c", "#3c4938", "#8547c2", "#c7c12c", "#ed0306", "#a9d6ff", "#15281c", "#d8bf9e", "#ca6e95", "#2c0bc0", "#c22c62", "#e9e601", "#000000", "#808080", "#FFA500"]

for k,v in mp.items():
    for d in v:
        date = datetime.datetime.strptime(d["date"], "%Y-%m-%dT%H:%M:%SZ").date()
        if (date < start_date):
            start_date = date
        if d["filename"] not in file_set:
          file_mp[d["filename"]] = idx_counter
          idx_counter += 1
          file_set.add(d["filename"])
    color_mp[k] = color_list[color_counter]
    color_counter += 1
    
for k,v in mp.items():
    for d in v:
        d["week"] = (datetime.datetime.strptime(d["date"], "%Y-%m-%dT%H:%M:%SZ").date() - start_date).days // 7


plt_mp = {}

for k,v in mp.items():
    for d in v:
        plt_mp[k] = plt_mp.get(k, {'files': [], 'week': [], 'color': color_mp[k]})
        plt_mp[k]['files'].append(file_mp[d["filename"]])
        plt_mp[k]['week'].append(d["week"])
    print(k, color_mp[k])
      
for k,v in plt_mp.items():
    plt.scatter(v["files"], v["week"], s=50, label=k, c=color_mp[k])
    print(k)
# ax.legend(loc='upper left', title='Authors', bbox_to_anchor=(1, 1))
plt.legend(loc='upper left', title='Authors', bbox_to_anchor=(1, 1))
plt.xlabel('File')
plt.ylabel('Weeks')
plt.show()
