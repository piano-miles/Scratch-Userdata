import os # Operating Systemß
import requests # Getting API requests
import json # Reading JSON data

print("----------------")

def jdump(obj):
    # Create a formatted string of the Python JSON object
    return json.dumps(obj, sort_keys=True, indent=4)

try:
    # Featured
    response = requests.get("https://api.scratch.mit.edu/proxy/featured")

    # Trending explore
    "https://api.scratch.mit.edu/explore/projects?q=games&mode=trending&language=en"

except:
        print("Failed GET request.")
else:
    sc = response.status_code
    print("Status: " + str(sc))
    if sc == 200:
        print("Result returned successfully.")
        #print(response.json())
        #print(jdump(response.json()))
        if True:    
            for p in response.json()['community_featured_projects']:
                if p['type'] == "project":
                    creator = p['creator']
                    project_id = p['id']
                    project_title = p['title']
                    loves = p['love_count']
                    
                    # Creator info
                    #"https://api.scratch.mit.edu/users/"+creator

                    # Favorited projects
                    #"https://api.scratch.mit.edu/users/"+creator+"/favorites"

                    # Followers
                    #"https://api.scratch.mit.edu/users/"+creator+"/followers"

                    # Following
                    #"https://api.scratch.mit.edu/users/"+creator+"/following"

                    # Unread messages
                    #"https://api.scratch.mit.edu/users/"+creator+"/messages/count"

                    # Projects
                    #"https://api.scratch.mit.edu/users/"+creator+"/projects"

                        # Project Info
                        #"https://api.scratch.mit.edu/users/"+creator+"/projects/"+project_id

                        # Project Comments
                        #"https://api.scratch.mit.edu/users/"+creator+"/projects/"+project_id+"/comments"

                    print(creator)
                    response = requests.get("https://api.scratch.mit.edu/users/"+creator)


                    quit()

            #print(jdump(pass_times))
        if sc == 301:
            print("The server is redirecting you to a different endpoint.")
        if sc == 400:
            print("The server thinks you made a bad request. Incorrect credentials.")
        if sc == 401:
            print("The server thinks you’re not authenticated.")
        if sc == 403:
            print("The resource you’re trying to access is forbidden. You do not have the right permissions.")
        if sc == 404:
            print("The resource you tried to access wasn’t found on the server.")
        if sc == 503:
            print("The server is not ready to handle the request.")