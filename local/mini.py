import requests
import json
import time
from tqdm import tqdm
import threading
from math import *
def jdump(obj): return json.dumps(obj, sort_keys=True, indent=4)


def jget(url, i):
    response = ''

    try:
        response = requests.get(url)

    except Exception as e:
        print('ERR: jget requests.get failed.')
        print('If you are using an internet connection provided by a school or organization with heavy internet traffic control, that may be why. :)')
        print('Exception: '+str(e))
        print('Attmpt '+str(i))
        print('url: '+url)
        quit()

    else:
        if response.status_code == 200:
            return json.loads(jdump(response.json()))

        elif i < 10:
            print(str(response.status_code) +
                  '; Failed to fetch data, trying again in one second.')
            time.sleep(1)
            jget(url, i+1)

        else:
            sc = response.status_code
            print('Attempted to get data 10 times, failed.')
            print('Error code: '+str(sc)+'.')
            if sc == 301:
                print('The server is redirecting you to a different endpoint.')
            elif sc == 400:
                print('The server thinks you made a bad request. Incorrect credentials.')
            elif sc == 401:
                print('The server thinks you’re not authenticated.')
            elif sc == 403:
                print(
                    'The resource you’re trying to access is forbidden. You do not have the right permissions.')
            elif sc == 404:
                print('The resource you tried to access wasn’t found on the server.')
            elif sc == 503:
                print('The server is not ready to handle the request.')
            else:
                print('Unknown error type.')
            print('URL: '+url)
            quit()


f = open('../json/users.json')
users_info = json.load(f)
usernames = users_info['usernames']
follows = users_info['follows']
f.close()
userData = []
sampleData = []


def col(K):
    username = usernames[K]
    valid = jget('https://api.scratch.mit.edu/accounts/checkusername/' +
                 username, 0)['msg'] == 'username exists'
    if valid:
        user = jget('https://api.scratch.mit.edu/users/'+username, 0)
        projects = 40
        off = 0
        while projects > 39:
            userData.append(user)
            sample = jget('https://api.scratch.mit.edu/users/' +
                          username+'/projects?limit=40&offset='+str(off), 0)
            sampleData.append(sample)
            projects = len(sample)
            off += 40


c = len(follows)
for K in tqdm(range(c)):
    col(K)
print('Data collected.')

data = 'User,,,,Average Project Statistics,,,,,,,\nUsername,Followers,Country,Join Date,Views,Loves,Favorites,Remixes,Public,Published,Visible,Commentable,Projects\n'
print('--  Parsing data  --')

user = []
pusr = []
sample = []
views = 0
loves = 0
favorites = 0
remixes = 0
public = 0
published = 0
visible = 0
commentable = 0
count = 0
projects = ''
username = userData[0]['username']
country = ''
joinDate = ''
samples = len(userData)

for K in tqdm(range(samples+1)):
    if K < samples:
        user = userData[K]
        pusr = username
        username = user['username']
        sample = sampleData[K]

    else:
        username = pusr+'a'

    if not pusr == username:
        views = str(views)
        loves = str(loves)
        favorites = str(favorites)
        remixes = str(remixes)
        public = str(public)
        published = str(published)
        visible = str(visible)
        commentable = str(commentable)
        data += pusr+','+follows[K].strip()+','+country+','+joinDate+','+views+','+loves+',' + \
            favorites+','+remixes+','+public+','+published + \
            ','+visible+','+commentable+','+projects+'\n'

        views = 0
        loves = 0
        favorites = 0
        remixes = 0
        public = 0
        published = 0
        visible = 0
        commentable = 0
        count = 0

        if K == samples:
            break

    country = user['profile']['country']
    joinDate = user['history']['joined'].split('T')[0]

    for i in range(len(sample)):
        project = sample[i]
        views += project['stats']['views']
        loves += project['stats']['loves']
        favorites += project['stats']['favorites']
        remixes += project['stats']['remixes']
        public += 1 if project['public']else 0
        published += 1 if project['is_published']else 0
        visible += 1 if project['visibility'] == 'visible'else 0
        commentable += 1 if project['comments_allowed']else 0

        if project['public'] and project['is_published'] and project['visibility'] == 'visible':
            count += 1

    projects = str(count)

f = open('dataset.csv', 'w')
f.write(data)
f.close()
print('File written to dataset.csv.')
