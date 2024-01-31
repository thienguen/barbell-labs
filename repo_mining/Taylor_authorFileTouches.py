import json
import requests
import csv

import os

if not os.path.exists("data"):
 os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

def countfiles(dictAuthors, lsttokens, repo, fileNames):
    ipage = 1  # url page counter
    ct = 0  # token counter

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                author = shaDetails['commit']['author']['name']
                date = shaDetails['commit']['author']['date']

                for obj in filesjson:
                    filename = obj['filename']
                    if filename in fileNames:
                        if filename.endswith('.java'):
                            dictAuthors.append({'file': filename, 'author': author, 'date': date})
                            print(filename, author, date)
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'

# token
lstTokens = [""]

# collect data from file_rootbeer.csv
fileData = []
with open('data/file_rootbeer.csv') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        fileData.append(row['Filename'])

dictAuthors = []
countfiles(dictAuthors, lstTokens, repo, fileData)
print('Total number of commits: ' + str(len(dictAuthors)))

file = repo.split('/')[1]
fileOutput = 'data/commits_' + file + '.csv'
rows = ["Author", "File", "Date"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for x in dictAuthors:
    rows = [x['author'], x['file'], x['date']]
    writer.writerow(rows)
fileCSV.close()