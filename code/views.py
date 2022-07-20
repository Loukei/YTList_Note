import dotenv, os # read environment settings in .env
from youtube_api import get_videoInfo, get_playlistItems
import requests
import json
from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound

def set_Jinja2_Env() -> Environment:
    """Set environment with filesystem

    Returns:
        Environment: _description_
    """
    template_path:str = './templates'
    env = Environment(loader=FileSystemLoader(template_path))
    return env

def render_playlist(playlistId:str, key:str, template:str, output:str):
    """request playlist info, render it to course note(playlist) #TODO
        
    Args:
        playlistId (str): _description_
        key (str): _description_
        template (str): _description_
        output (str): _description_
    """
    env:Environment = set_Jinja2_Env()
    t:Template = env.get_template(template)
    res:requests.Response = get_playlistItems(apikey=key, playlistId=playlistId)
    if(res.status_code == requests.codes.ok):
        jsonobj = json.loads(res.text)
        print(jsonobj)
        # request playlistitems
        #  if resultsPerPage < totalResults, then call next page for more listitems
        resultsPerPage:int = jsonobj["pageInfo"]["resultsPerPage"]
        totalResults:int = jsonobj["pageInfo"]["totalResults"]
        print(resultsPerPage)
        print(totalResults)
    else:
        print("Error:" + res.status_code)
        res.raise_for_status()
    pass

def render_video(vid:str, key:str, template:str, output:str):
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
        jsonobj = json.loads(res.text)["items"][0]
        with open(output,mode='w',encoding='utf8') as file:
            file.write(t.render(video = jsonobj))
    else:
        res.raise_for_status()
    pass

if __name__ == "__main__":
    """
    get video than turn into markdown notes
    """
    try:
        dotenv.load_dotenv()
        apikey:str = os.getenv("YTAPI_KEY")
        # render_video(vid = "bC7o8P_Ste4", key = apikey,template="VideoClassNote.md",output="./output/test.md")
        render_playlist(playlistId= "PLhOoxQxz2yFOcJoLoPRyYzjqCbddeOjP4", key = apikey, template = "PlaylistClassNote.md", output = "")
    except TemplateNotFound as te:
        print(f"Template not found error: {str(te)}")
    except Exception as e:
        print(f"Error:{str(e)}")
    pass
