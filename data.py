import requests

# setup owner name , access_token, and headers 
owner='bethanyjep'
access_token='' 
headers = {'Authorization':"Token "+access_token}

# loop through all pages to obtain all the repos' information
repos=[]
for page_num in range(1,300):
    try:
    # to find all the repos' names from each page
        url=f"https://api.github.com/users/{owner}/repos?page={page_num}" 
        repo=requests.get(url,headers=headers).json()
        repos.append(repo)
    except:
        repos.append(None)

print(repos)