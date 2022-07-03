"""
Define the models for Youtube Video and Youtube Playlist
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Any
import json

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False

# def from_datetime(x: Any) -> datetime:
#     return dateutil.parser.parse(x)

@dataclass
class Chapter:
    start_time:timedelta
    description:str

@dataclass
class Video():
    id:str  
    poublishedAt:datetime       # snippet.publishedAt
    duration:timedelta          # contentDetails.duration
    channelTitle:str            # snippet.channelTitle
    caption:bool                # contentDetails.caption
    #--- Language ralated content ---#
    defaultLanguage:str         # snippet.defaultLanguage
    title:str                   # snippet.title
    description:str             # snippet.description
    localized_title:str         # snippet.localized.title
    localized_description:str   # snippet.localized.description
    #--- Non offcial content ---#
    chapters:List[Chapter]

    @staticmethod
    def from_dict(obj:Dict) -> 'Video':
        assert isinstance(obj, dict)
        snippet:dict = obj.get("snippet")
        contentDetails:dict = obj.get("contentDetails")

        id:str = from_str(obj.get('id'))
        # poublishedAt:datetime = from_datetime(obj.get('poublishedAt').)
        # duration:timedelta          
        channelTitle:str = from_str(snippet.get("channelTitle"))
        caption:bool = from_stringified_bool(contentDetails.get(''))
        defaultLanguage:str         
        title:str                   
        description:str             
        localized_title:str         
        localized_description:str   
        chapters:List[Chapter]
        return Video

    @staticmethod
    def get_fullurl(id:str) -> str:
        return f"https://youtu.be/{id}"

def test_video_model(file_path:str):
    print(file_path)
    with open(file = file_path, mode='r', encoding='utf8') as file:
        d:dict = json.load(file)
        video_date:dict = d["items"][0]
        id:str = from_str(video_date.get('id'))
        print(id)
    pass

if __name__ == "__main__":
    test_fp:str = "./code/output/bC7o8P_Ste4.json"
    test_video_model(file_path = test_fp)
    pass