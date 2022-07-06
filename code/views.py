
from dotenv import load_dotenv
import os

from youtube_api import get_videoInfo
import requests

import json
from models.ytvideo import YTVideo, yt_video_from_dict
from jinja2 import Environment, FileSystemLoader, Template

def set_Jinja2_Env() -> Environment:
    """Set environment with filesystem

    Returns:
        Environment: _description_
    """
    template_path:str = './templates'
    env = Environment(loader=FileSystemLoader(template_path))
    return env

def test_video_data() -> YTVideo:
    "Load test data from previous request data file"
    test_fp:str = "./testdata/bC7o8P_Ste4.json"
    with open(file = test_fp, mode='r', encoding='utf8') as file:
        video:YTVideo = yt_video_from_dict(json.load(file)["items"][0])
    return video

def video(vid:str, key:str, template:str, output:str):
    """Request Youtube info from {vid} and {key}, use {template} to render, then save data to {output} location
    Args:
        vid (str): youtube video id
        key (str): youtube api key
        template (str): used template file
        output (str): template render file
    """
    env:Environment = set_Jinja2_Env()
    t:Template = env.get_template(template)
    res:requests.Response = get_videoInfo(apikey = key,video_id = vid)
    if(res.status_code == requests.codes.ok):
        v:YTVideo = yt_video_from_dict(json.loads(res.text)["items"][0]) # video resource is under "items" list
        with open(output,mode='w',encoding='utf8') as file:
            file.write(t.render(video = v))
    else:
        res.raise_for_status()
    pass

if __name__ == "__main__":
    """
    get video than turn into markdown notes
    """
    try:
        load_dotenv()
        video(vid = "bC7o8P_Ste4", key = os.getenv("YTAPI_KEY"),template="TestNote.md",output="./output/test.md")
    except Exception as e:
        print(e)
    pass
