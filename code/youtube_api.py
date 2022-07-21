from typing import Optional
import requests

def get_playlists(apikey:str,playlistId:str):
    url:str = "https://www.googleapis.com/youtube/v3/playlists"
    payload:dict = {
        "part": "snippet",
        "id": playlistId,
        "key": apikey,
        "Accept": "application/json",
        "fields": "items(snippet(publishedAt,title,description,channelTitle,defaultLanguage,localized))"
    }
    return requests.get(url, params=payload)

def get_playlistItems(apikey:str,playlistId:str,pageToken:Optional[str] = None):
    """ get playlistItem info 
    - [PlaylistItems](https://developers.google.com/youtube/v3/docs/playlistItems)
    """
    url:str = "https://youtube.googleapis.com/youtube/v3/playlistItems"
    payload:dict = {
        "part": "snippet",
        "playlistId": playlistId,
        "key": apikey,
        "pageToken": pageToken,
        "Accept": "application/json",
        "fields": "nextPageToken,items(snippet(publishedAt,title,description,channelTitle,position)),pageInfo"
    }
    return requests.get(url, params=payload)

def get_videoInfo(apikey:str,video_id:str) -> requests.Response:
    """ get YT video info
    - [Videos: list](https://developers.google.com/youtube/v3/docs/videos/list)
    """
    url:str = "https://www.googleapis.com/youtube/v3/videos"
    payload:dict = {
        "part": ["snippet","contentDetails"],
        "id": video_id,
        "key": apikey,
        "Accept": "application/json",
        "fields": "items(id,snippet(publishedAt,title,description,channelTitle,defaultLanguage,localized(title,description)),contentDetails(duration,caption))"
    }
    return requests.get(url, params=payload)

if __name__ == "__main__":
    "test here"
    playlistid_1:str = "PLQgT9G4SVR-LQfix29B8zYvM-Pk-adPG_" # "freeCodeCamp C++ courses"
    playlistid_2:str = "PLhOoxQxz2yFOcJoLoPRyYzjqCbddeOjP4" # "Dimension 20: Fantasy High"
    apikey:str = ""
    reply = get_playlists(apikey=apikey,playlistId=playlistid_1)
    print(reply.text) 
    reply = get_playlists(apikey=apikey,playlistId=playlistid_2)
    print(reply.text)
    pass