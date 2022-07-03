"""
Define the models for Youtube Video and Youtube Playlist
"""

import json
from ytvideo import YTVideo, yt_video_from_dict

def test_video_model(file_path:str):
    print(f'path = {file_path}')
    with open(file = file_path, mode='r', encoding='utf8') as file:
        video:YTVideo = yt_video_from_dict(json.load(file)["items"][0])
        # print(video)
        print(video.id)
        print(video.content_details.duration)
    pass

if __name__ == "__main__":
    test_fp:str = "./code/output/bC7o8P_Ste4.json"
    test_video_model(file_path = test_fp)
    pass