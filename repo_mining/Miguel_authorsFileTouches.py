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

# @authorData, just data of the filanmes, authors, and dates of commits
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(authorData, lsttokens, repo):
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

                # Getting author, date, and filename for each sha
                authorName = shaDetails['commit']['author']['name']
                commitDate = shaDetails['commit']['author']['date']

                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    # So just check if it's a source file, aka .java for rootbeer (look at languages used in repo to know which extensions)
                    if filename.endswith('.java'):
                        authorData.append({'filename': filename, 'author': authorName, 'date': commitDate})

                        # Just checking what info we put in
                        print(filename, authorName, commitDate)

            ipage += 1
    except:
        print("Error receiving data")
        exit(0)


# GitHub repo
repo = 'scottyab/rootbeer'
#repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["xxx"]

# Just populate it as we will use it to store info into a write file right after.
dictfiles = []
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/commit_info_' + file + '.csv'
rows = ["Filename", "Author", "Dates"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for data in dictfiles:
    rows = [data['filename'], data['author'], data['date']]
    writer.writerow(rows)

fileCSV.close()