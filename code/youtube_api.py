import requests
import os
import dotenv
import json
# import models

def get_playlist_Info(apikey:str,video_id:str):
    """
    #TODO
    """
    pass

def get_videoInfo(apikey:str,video_id:str) -> requests.Response:
    """ get YT video info: title, length, discription, chapter(start_time,title)
    """
    url:str = "https://www.googleapis.com/youtube/v3/videos"
    payload:dict = {
        "part": ["snippet","contentDetails"],
        "id": video_id,
        "key": apikey,
        "Accept": "application/json",
    }
    return requests.get(url, params=payload)

def main():
    try:
        dotenv.load_dotenv()
        vid:str = "bC7o8P_Ste4" 
        # reply:requests.Response = get_videoInfo(apikey=os.getenv("YTAPI_KEY"), video_id=vid)
        # save reply to file so we can focus on scrape data
        with open(file=f'code/output/{vid}.json',mode='w+',encoding='utf8') as outfile:
            outfile.write("{'a':1}")
        
    except Exception as e:
        print(e)
    pass

if __name__ == "__main__":
    main()
    pass