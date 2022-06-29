"""
Define the models for Youtube Video and Youtube Playlist
"""

from typing import List
from datetime import timedelta
from dataclasses import dataclass

@dataclass
class YTVideoChapter:
    """VideoChapter records the chapter info in the video

    Args:
        TypedDict (_type_): _description_
    """
    start_time:timedelta
    title:str

@dataclass
class YTVideo:
    id:str
    title:str
    duration:timedelta
    description:str
    chapters:List[YTVideoChapter]

@dataclass
class YTPlaylist:
    """_summary_
    #TODO
    """
    pass

def test_model():
    # va:YTVideo = YTVideo(
    #     id = "bC7o8P_Ste4",
    #     title = "Greedy Algorithms Tutorial – Solve Coding Challenges",
    #     duration =  timedelta(hours=1,minutes=53,seconds=8),
    #     description = "Learn how to use greedy algorithms to solve coding challenges")
    # print(va)
    # print(va.__dict__)

    # d = {"duration": timedelta(hours=1,minutes=53,seconds=8)}
    # print(d)

    # td = timedelta(hours=1,minutes=53,seconds=8)
    # print(td.str)

    td2 = timedelta('00:00')
    print(td2)
    pass

if __name__ == "__main__":
    test_model()