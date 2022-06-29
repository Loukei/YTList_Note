import requests
import os
import dotenv

def get_videoInfo(apikey:str,video_id:str):
    """ get YT video info: title, length, discription, chapter(start_time,title)
    """
    url:str = "https://www.googleapis.com/youtube/v3/videos"
    payload:dict = {
        "part": ["snippet","contentDetails"],
        "id": video_id,
        "key": apikey,
        "Accept": "application/json",
    }
    r:requests.Response = requests.get(url, params=payload)
    print(r.text)
    pass

def main():
    try:
        dotenv.load_dotenv()
        get_videoInfo(apikey=os.getenv("YTAPI_KEY"), video_id="bC7o8P_Ste4")
    except Exception as e:
        print(e)
    pass

if __name__ == "__main__":
    main()
    pass