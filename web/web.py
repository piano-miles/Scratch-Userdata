import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.request import urlopen
import json
import time
from tqdm import tqdm
import threading
import os
from sys import platform

session = requests.Session()
C = Retry(connect=3, backoff_factor=0.5)
B = HTTPAdapter(max_retries=C)
session.mount('http://', B)
session.mount('https://', B)


def jdump(obj):
    return json.dumps(obj, sort_keys=True, indent=4)


def jget(url, i):
    response = ''
    try:
        response = session.get(url)

    except Exception as e:
        print('ERR: jget session.get failed.')
        print(
            'If you are using an internet connection provided by a school or organization with heavy internet traffic control, that may be why. :)'
        )
        print('Exception: ' + str(e))
        print('Attmpt ' + str(i))
        print('url: ' + url)
        quit()

    else:
        if response.status_code == 200:
            return json.loads(jdump(response.json()))

        elif i < 10:
            print(
                str(response.status_code) +
                '; Failed to fetch data, trying again in one second.')
            time.sleep(1)
            jget(url, i + 1)

        else:
            sc = response.status_code
            print('Attempted to get data 10 times, failed.')
            print('Error code: ' + str(sc) + '.')
            if sc == 301:
                print('The server is redirecting you to a different endpoint.')
            elif sc == 400:
                print(
                    'The server thinks you made a bad request. Incorrect credentials.'
                )
            elif sc == 401:
                print('The server thinks you’re not authenticated.')
            elif sc == 403:
                print(
                    'The resource you’re trying to access is forbidden. You do not have the right permissions.'
                )
            elif sc == 404:
                print(
                    'The resource you tried to access wasn’t found on the server.'
                )
            elif sc == 503:
                print('The server is not ready to handle the request.')
            else:
                print('Unknown error type.')
            print('URL: ' + url)
            quit()


if platform == "linux" or platform == "linux2":
    print("Running on Linux.")
elif platform == "darwin":
    print("Running on MacOS.")
elif platform == "win32":
    print("Running on Windows.")

print('Initial working directory: ', os.getcwd())
os.chdir(os.path.dirname(os.path.abspath('__file__')))
print('New working directory: ', os.getcwd())

print('Reading users.json')
if False:
    f = open('./data/users.json')  # Todo: find file
    users_info = json.load(f)
    usernames = users_info['usernames']
    follows = users_info['follows']
    f.close()
url = "https://raw.githubusercontent.com/piano-miles/Scratch-Userdata/main/web/data/users.json"
response = urlopen(url)
users_info = json.load(response.read())
usernames = users_info['usernames']
follows = users_info['follows']
c = len(follows)
userData = []
sampleData = []


def col(K):
    batch = 0
    username = usernames[K]
    valid = jget(
        'https://api.scratch.mit.edu/accounts/checkusername/' + username,
        0)['msg'] == 'username exists'

    if valid:
        user = jget('https://api.scratch.mit.edu/users/' + username, 0)
        projects = 40
        off = 0

        while projects > 39:
            i = batch | K << 10
            userData.append((i, user, follows[K]))
            sample = jget(
                'https://api.scratch.mit.edu/users/' + username +
                '/projects?limit=40&offset=' + str(off), 0)
            sampleData.append((i, sample))
            projects = len(sample)
            off += 40
            batch += 1


print('Creating ' + str(c) + ' Threads')
c = int(c * 0.1)
for L in range(10):
    print("-- Thread Batch " + str(L + 1) + "/10 --")
    threads = []
    for K in tqdm(range(c)):
        t = threading.Thread(target=col, args=(K + L * c, ))
        t.start()
        threads.append(t)

    print('Joining Threads')
    for t in tqdm(threads):
        t.join()

print('Data Collected.')

userData = sorted(userData, key=lambda D: D[0])
sampleData = sorted(sampleData, key=lambda D: D[0])
for K in range(len(userData)):
    userData[K] = userData[K][1], userData[K][2]
for K in range(len(sampleData)):
    sampleData[K] = sampleData[K][1]
print('Sorted Threads')

data = 'User,,,,Average Project Statistics,,,,,,,\nUsername,Followers,Country,Join Date,Views,Loves,Favorites,Remixes,Public,Published,Visible,Commentable,Projects\n'

print('--  Parsing data  --')
user = []
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
username = userData[0][0]['username']
pusr = username
country = ''
joinDate = ''

samples = len(userData)
for K in tqdm(range(samples + 1)):
    if K < samples:
        user = userData[K][0]
        pusr = username
        username = user['username']
        sample = sampleData[K]

    else:
        username = pusr + 'a'

    if not pusr == username:
        views = str(views)
        loves = str(loves)
        favorites = str(favorites)
        remixes = str(remixes)
        public = str(public)
        published = str(published)
        visible = str(visible)
        commentable = str(commentable)

        if country is None:
            country = ''
        data += pusr+','+str(userData[K-1][1])+','+country+','+joinDate+','+views+','+loves+',' + \
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
        public += 1 if project['public'] else 0
        published += 1 if project['is_published'] else 0
        visible += 1 if project['visibility'] == 'visible' else 0
        commentable += 1 if project['comments_allowed'] else 0

        if project['public'] and project['is_published'] and project[
                'visibility'] == 'visible':
            count += 1

    projects = str(count)

f = open('dataset.csv', 'w')
f.write(data)
f.close()
print('File written to dataset.csv.\nDone.')
