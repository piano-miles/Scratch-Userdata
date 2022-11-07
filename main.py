import os  # Operating System
import requests  # Handle API requests
import json  # Read JSON data
import pprint  # Prints the json in a more friendly fashion

print("\n"*5+"----------------")


def printl(label, data):
    print("\n"+label+":")
    print(data)


def jdump(obj):
    # Create a formatted string of the Python JSON object
    return json.dumps(obj, sort_keys=True, indent=4)


def jget(url, log):
    try:
        response = requests.get(url)
    except:
        print("Failed GET request.")
        quit()
    else:
        sc = response.status_code
        if log:
            print("Status: " + str(sc))
        if sc == 200:
            if log:
                print("Result returned successfully.")
            return json.loads(jdump(response.json()))
        elif log:
            if sc == 301:
                print("The server is redirecting you to a different endpoint.")
            elif sc == 400:
                print("The server thinks you made a bad request. Incorrect credentials.")
            elif sc == 401:
                print("The server thinks you’re not authenticated.")
            elif sc == 403:
                print(
                    "The resource you’re trying to access is forbidden. You do not have the right permissions.")
            elif sc == 404:
                print("The resource you tried to access wasn’t found on the server.")
            elif sc == 503:
                print("The server is not ready to handle the request.")
            else:
                print("Unknown error type.")
            quit()


# featured = jget("https://api.scratch.mit.edu/proxy/featured", True)  # Featured
# explore = jget("https://api.scratch.mit.edu/explore/projects?q=games&mode=trending&language=en", True) #Trending explore

# print(response.json())
# print(jdump(response.json()))

header = "User,Project,,Stats,,,Remix Tree,,,Other,,,,\nUsername,Title,Project ID,Views,Loves,Favorites,Remixes,Parent,Root,Public,Published,Visible,Creation Date,Commentable"

# https://api.scratch.mit.edu/users/mres/messages/count
# https://api.scratch.mit.edu/users/mres/projects

username = "mres"

sample = jget("https://api.scratch.mit.edu/users/" +
              username+"/projects", True)  # A user

i = 0
project = sample[i]

title = project["title"]
projectID = project["id"]
views = project["stats"]["views"]
loves = project["stats"]["loves"]
favorites = project["stats"]["favorites"]
remixes = project["stats"]["remixes"]
parent = project["remix"]["parent"]
root = project["remix"]["root"]
public = project["public"]
published = project["is_published"]
visible = project["visibility"]
creationDate = project["history"]["created"]
commentable = project["comments_allowed"]

print(i)
print(username)
print(title)
print(projectID)
print(views)
print(loves)
print(favorites)
print(remixes)
print(parent)
print(root)
print(public)
print(published)
print(visible)
print(creationDate)
print(commentable)

# pprint.pprint(sample)

if (False):
    for p in featured['community_featured_projects']:
        if p['type'] == "project":
            creator = p['creator']
            project_id = p['id']
            project_title = p['title']
            loves = p['love_count']

            printl("creator",       creator)
            printl("project_id",    project_id)
            printl("project_title", project_title)
            printl("loves",         loves)

            # Creator info
            q = "https://api.scratch.mit.edu/users/"+creator
            printl("user_info <- GET", q)
            user_info = jget(q, False)
            printl("user_info", user_info)

            # Favorited projects
            # "https://api.scratch.mit.edu/users/"+creator+"/favorites"

            # Followers
            q = "https://api.scratch.mit.edu/users/"+creator+"/followers"
            printl("followers <- GET", q)
            followers = jget(q, False)
            printl("followers", followers)

            # Following
            # "https://api.scratch.mit.edu/users/"+creator+"/following"

            # Unread messages
            # "https://api.scratch.mit.edu/users/"+creator+"/messages/count"

            # Projects
            # "https://api.scratch.mit.edu/users/"+creator+"/projects"

            # Project Info
            # "https://api.scratch.mit.edu/users/"+creator+"/projects/"+project_id

            # Project Comments
            # "https://api.scratch.mit.edu/users/"+creator+"/projects/"+project_id+"/comments"

            quit()

        # print(jdump(pass_times))
