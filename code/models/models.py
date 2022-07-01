"""
Define the models for Youtube Video and Youtube Playlist
"""
from model_ytvideo import YTVideo, yt_video_from_dict
import json

def test_model_ytvideo(fp:str):
    with open(file=fp,mode='r',encoding='utf8') as file:
        d:dict = json.load(fp=file)
        video:YTVideo = yt_video_from_dict(d["items"][0])

        # print(video.id)
        # # print(video.content_details)
        # print(video.content_details.duration)
        # print(video.content_details.caption)

        # # print(video.snippet)
        # print(video.snippet.title)
        # print(video.snippet.description)
    pass

if __name__ == "__main__":
    test_model_ytvideo("./code/output/bC7o8P_Ste4.json")
    pass