import requests

def get_playlistItems(apikey:str,playlistId:str):
    """ get playlistItem info 
    - [PlaylistItems](https://developers.google.com/youtube/v3/docs/playlistItems)
    """
    url:str = "https://youtube.googleapis.com/youtube/v3/playlistItems"
    payload:dict = {
        "part": "snippet",
        "playlistId": playlistId,
        "key": apikey,
        "Accept": "application/json",
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
    }
    return requests.get(url, params=payload)

if __name__ == "__main__":
    "test here"
    playlistid_1:str = "PLQgT9G4SVR-LQfix29B8zYvM-Pk-adPG_" # "freeCodeCamp C++ courses"
    reply = get_playlistItems(apikey="",playlistId=playlistid_1)
    print(reply.text)
    pass