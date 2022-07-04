from urllib.parse import ParseResult, urlparse, urldefrag, urlsplit
import views

def url_routing(url:str):
    """route url to different views function
    # TODO: need router lib like django.url
    Args:
        url (str): _description_
    """
    r:ParseResult = urlparse(url=url)
    none_query_url:str = r._replace(query=None).geturl()
    if(none_query_url == 'https://www.youtube.com/watch' and r.query["v"]): return f"send to YTvideo {r.query['v']}" # views.video_with_chapter()
    # if(none_query_url == "https://youtu.be/8k0QPEQxr24")
    pass

def main():
    print('--- Main ---')
    # url_1:str = "https://www.youtube.com/watch?v=5AJaW5HoztQ"
    # url_routing(url_1)
    f = open('code\output\bC7o8P_Ste4.json',mode='r',encoding='utf8')
    print(type(f))
    f.close()
    pass

if __name__ == '__main__':
    main()