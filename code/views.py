import json
from typing import Dict
from models.ytvideo import YTVideo, yt_video_from_dict
from jinja2 import Environment, FileSystemLoader, Template

def set_Jinja2_Env() -> Environment:
    """Set environment with filesystem

    Returns:
        Environment: _description_
    """
    template_path:str = './code/templates'
    env = Environment(loader=FileSystemLoader(template_path))
    return env

def render_to_file(template_path:str,data:Dict,output_path:str):
    env:Environment = set_Jinja2_Env()
    t:Template = env.get_template(template_path)
    t.stream(data).dump(output_path,encoding = 'utf8')
    pass

def test_video_data() -> YTVideo:
    "Load test video data from file"
    test_fp:str = "./code/output/bC7o8P_Ste4.json"
    with open(file = test_fp, mode='r', encoding='utf8') as file:
        video:YTVideo = yt_video_from_dict(json.load(file)["items"][0])
        return video

def video_with_chapter():
    env:Environment = set_Jinja2_Env()
    t:Template = env.get_template('TestNote.md')
    v:YTVideo = test_video_data()
    # TODO: make template render on out file, check render_to_file()
    print(t.render(video = v))
    pass

if __name__ == "__main__":
    """
    get video than turn into markdown notes
    """
    video_with_chapter()
    pass
