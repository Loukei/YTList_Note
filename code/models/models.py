"""
Define the models for Youtube Video and Youtube Playlist
"""
from base64 import decode
from typing import List
from datetime import timedelta
from dataclasses import dataclass

import ytvideos
import json

# @dataclass
# class YTVideoChapter:
#     """VideoChapter records the chapter info in the video

#     Args:
#         TypedDict (_type_): _description_
#     """
#     start_time:timedelta
#     title:str

# @dataclass
# class YTVideo:
#     id:str
#     title:str
#     duration:timedelta
#     description:str
#     chapters:List[YTVideoChapter]

def test_model():
    fp:str = "./code/output/bC7o8P_Ste4.json"
    f = open(fp, 'r', 'utf8')
    data = json.load(f)
    # with open(file=fp,mode='r',encoding='utf8') as file:
    #     d:dict = json.load(fp=file) # TODO: JSONDecodeError
    #     video:ytvideos.YTVideo = ytvideos.yt_video_from_dict(d)
    #     print(video.id)
    pass

if __name__ == "__main__":
    test_model()
    pass