# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = yt_video_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ContentDetails:
    caption: bool
    duration: str

    @staticmethod
    def from_dict(obj: Any) -> 'ContentDetails':
        assert isinstance(obj, dict)
        caption = from_stringified_bool(from_str(obj.get("caption")))
        duration = from_str(obj.get("duration"))
        return ContentDetails(caption, duration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["caption"] = from_str(str(self.caption).lower())
        result["duration"] = from_str(self.duration)
        return result


@dataclass
class Localized:
    description: str
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'Localized':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        title = from_str(obj.get("title"))
        return Localized(description, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["title"] = from_str(self.title)
        return result


@dataclass
class Snippet:
    channel_title: str
    default_language: str
    description: str
    localized: Localized
    published_at: datetime
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'Snippet':
        assert isinstance(obj, dict)
        channel_title = from_str(obj.get("channelTitle"))
        default_language = from_str(obj.get("defaultLanguage"))
        description = from_str(obj.get("description"))
        localized = Localized.from_dict(obj.get("localized"))
        published_at = from_datetime(obj.get("publishedAt"))
        title = from_str(obj.get("title"))
        return Snippet(channel_title, default_language, description, localized, published_at, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channelTitle"] = from_str(self.channel_title)
        result["defaultLanguage"] = from_str(self.default_language)
        result["description"] = from_str(self.description)
        result["localized"] = to_class(Localized, self.localized)
        result["publishedAt"] = self.published_at.isoformat()
        result["title"] = from_str(self.title)
        return result


@dataclass
class YTVideo:
    content_details: ContentDetails
    id: str
    snippet: Snippet

    @staticmethod
    def from_dict(obj: Any) -> 'YTVideo':
        assert isinstance(obj, dict)
        content_details = ContentDetails.from_dict(obj.get("contentDetails"))
        id = from_str(obj.get("id"))
        snippet = Snippet.from_dict(obj.get("snippet"))
        return YTVideo(content_details, id, snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["contentDetails"] = to_class(ContentDetails, self.content_details)
        result["id"] = from_str(self.id)
        result["snippet"] = to_class(Snippet, self.snippet)
        return result


def yt_video_from_dict(s: Any) -> YTVideo:
    return YTVideo.from_dict(s)


def yt_video_to_dict(x: YTVideo) -> Any:
    return to_class(YTVideo, x)


def test():
    try:
        fp:str = "./code/output/bC7o8P_Ste4.json"
        with open(file=fp,mode='r',encoding='utf8') as file:
            print(file.read())
    except Exception as e:
        print(e)
    pass

if __name__ == "__main__":
    test()
    pass