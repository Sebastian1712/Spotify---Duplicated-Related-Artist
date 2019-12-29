import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
# print(json.dumps(user, sort_keys=True, indent=4))
# Get users followed artist
# usersFollowedArtistResult = spotifyObject.current_user_followed_artists(limit=2, after=None)
# usersFollowedArtistResult = usersFollowedArtistResult['artists']

# Compare the 50 artist to related artists these are the keys for after
# The program is running EXTREMELY SLOW due to the amount of iterations and for loops
# 3EnbnmqrrvApHJs6FMvYik
# 67nwj3Y5sZQLl72VNUHEYE

def compare_artist(relatedArtist):

    spotifyObject = spotipy.Spotify(auth=token)
    usersFollowedArtist = spotifyObject.current_user_followed_artists(limit=50,after=None)
    usersFollowedArtist = usersFollowedArtist['artists']

    for artist in usersFollowedArtist['items']:
                   
        if artist['name'] == relatedArtist:
            return False

        else:
            continue

    return True

def compare_artist_two(relatedArtist):

    spotifyObject = spotipy.Spotify(auth=token)
    usersFollowedArtist = spotifyObject.current_user_followed_artists(limit=50,after='3EnbnmqrrvApHJs6FMvYik')
    usersFollowedArtist = usersFollowedArtist['artists']

    for artist in usersFollowedArtist['items']:
                   
        if artist['name'] == relatedArtist:
            return False

        else:
            continue

    return True

def compare_artist_three(relatedArtist):

    spotifyObject = spotipy.Spotify(auth=token)
    usersFollowedArtist = spotifyObject.current_user_followed_artists(limit=50,after='67nwj3Y5sZQLl72VNUHEYE')
    usersFollowedArtist = usersFollowedArtist['artists']

    for artist in usersFollowedArtist['items']:
                   
        if artist['name'] == relatedArtist:
            return False

        else:
            continue

    return True

# Let's get the username from the terminal
username = sys.argv[1]
scope = 'user-follow-read'

# util.prompt_for_user_token(username,scope,client_id='369a9e8f686d4366bf14799d12a6b27e',client_secret='cf68d7b60ea84319b02e68b15e8906b4',redirect_uri='http://google.com/')
# Erase cache and prompt for user permission
try:
    # token = util.prompt_for_user_token(username)
    token = util.prompt_for_user_token(username,scope,client_id='369a9e8f686d4366bf14799d12a6b27e',client_secret='cf68d7b60ea84319b02e68b15e8906b4',redirect_uri='http://google.com/')

except:
    # os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotify object
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()

while True:

    # Menu details
    print()
    print("Welcome to Spotify Sebastian!")
    print()
    print("0 - Search for an artist")
    print("1 - Exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQ = input("Artist to look for: ")
        print()

        # Obtain artist from API
        searchResults = spotifyObject.search(searchQ, 1, 0, "artist")
        artist = searchResults['artists']['items'][0]
        artistID = artist['id']

        print(artist['name'] + " is related to: ")

        # Get related artist
        relatedArtistResult = spotifyObject.artist_related_artists(artistID)
        relatedArtistResult = relatedArtistResult['artists']

        for relatedArtist in relatedArtistResult:

                if compare_artist(relatedArtist['name']) == False or compare_artist_two(relatedArtist['name']) == False or compare_artist_three(relatedArtist['name']) == False:
                    # print("Already followed: " + relatedArtist['name'])
                    continue

                else:
                    print()
                    print("Related Artist: " + relatedArtist['name'])
                    print()

    if choice =="1":
        break
