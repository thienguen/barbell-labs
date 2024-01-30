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

# @files, List of file names
# @dictAuth, empty dictionary of Authors
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(files, dictAuth, lsttokens, repo):
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
            # iterate through the list of commits in spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                
                filesjson = shaDetails['files']
                author = shaDetails['commit']['author']['name']
                date = shaDetails['commit']['author']['date']
                
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    if filename in files:
                        if filename.endswith('.java'):
                            dictAuth.append({'file': filename, 'author': author, 'date': date})
                        print(author,date)
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
        
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'

# token
lstTokens = ["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", "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", "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 "]

dictAuth = [] #Authors + Dates
files = [] #File data
data = repo.split('/')[1]
with open('data/file_'+ data + '.csv') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        files.append(row['Filename'])
  
countfiles(files, dictAuth, lstTokens, repo)
print('Total number of commits: ' + str(len(dictAuth)))

# change this to the path of your file
fileOutput = 'data/authors_' + data + '.csv'
rows = ["Filename", "Author", "Date"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for i in dictAuth:
    rows = [i['file'],i['author'],i['date']]
    writer.writerow(rows)
fileCSV.close()