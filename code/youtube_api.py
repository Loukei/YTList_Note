from typing import Optional
import requests

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
    reply = get_playlistItems(apikey="",playlistId=playlistid_1)
    print(reply.text)
    pass