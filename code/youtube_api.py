import requests


def get_playlist_Info(apikey:str,video_id:str):
    """
    #TODO
    """
    pass

def get_videoInfo(apikey:str,video_id:str) -> requests.Response:
    """ get YT video info
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
    # test here
    pass