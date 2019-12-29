import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Let's get the username from the terminal
# User ID: locuras1712?si=EBuu12n6TOm3FlWQjNdYfA
username = sys.argv[1]

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotify object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
userFollowers = user['followers']['total']

while True:
    # Menu
    print()
    print("Welcome to Spotify " + displayName + "!")
    print(">>> You have " + str(userFollowers) + "followers")
    print()
    print("0 - Search for an artist")
    print("1 - Exit")
    print()
    choice = input("Your choice: ")

    # Search for artist
    if choice == "0":
        print()
        searchQuery = input("Artist's name: ")
        print()
    
        # Get the search results
        searchResults = spotifyObject.search(searchQuery, 1, 0,"artist")

        # Artist's details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + "followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album track details
        trackURIs = []
        trackArt = []
        i = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("Album: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data 
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(i) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                i+=1
                print()
        
        while True:
            songSelection = input("Enter a song number (x to exit)")
            
            if songSelection == "x":
                break
            webbrowser.open(trackArt[int(songSelection)])


    # End of the program
    if choice == "1":
        break

# print json.dumps(VARIABLE, sort_keys=True, indent=4))

