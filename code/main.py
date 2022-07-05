from typing import List
from urllib.parse import ParseResult, parse_qs, urlparse, urldefrag, urlsplit
import re
import views

def url_routing(url:str):
    """route url to different views function
    # TODO: need router lib like django.url
    Args:
        url (str): _description_
    """

    pass

def test_video_urls()->List[str]:
    return [
        "https://www.youtube.com/watch?v=5AJaW5HoztQ",
        "https://www.youtube.com/watch?v=zJGrxykhVUA",
        "https://youtu.be/zJGrxykhVUA"
    ]

def main():
    print('--- Main ---')
    pattern:str = "/^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*/"
    
    urls:List[str] = test_video_urls()
    for(url in urls){
        print(re.match(pattern, url))
    }
    
    pass

if __name__ == '__main__':
    main()
    pass