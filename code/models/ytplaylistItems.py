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
#     result = playlist_items_from_dict(json.loads(json_string))

from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, TypeVar, Type, cast, Callable
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Snippet:
    channel_title: str
    description: str
    position: int
    published_at: datetime
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'Snippet':
        assert isinstance(obj, dict)
        channel_title = from_str(obj.get("channelTitle"))
        description = from_str(obj.get("description"))
        position = from_int(obj.get("position"))
        published_at = from_datetime(obj.get("publishedAt"))
        title = from_str(obj.get("title"))
        return Snippet(channel_title, description, position, published_at, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channelTitle"] = from_str(self.channel_title)
        result["description"] = from_str(self.description)
        result["position"] = from_int(self.position)
        result["publishedAt"] = self.published_at.isoformat()
        result["title"] = from_str(self.title)
        return result


@dataclass
class Item:
    snippet: Snippet

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        snippet = Snippet.from_dict(obj.get("snippet"))
        return Item(snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["snippet"] = to_class(Snippet, self.snippet)
        return result


@dataclass
class PageInfo:
    results_per_page: int
    total_results: int

    @staticmethod
    def from_dict(obj: Any) -> 'PageInfo':
        assert isinstance(obj, dict)
        results_per_page = from_int(obj.get("resultsPerPage"))
        total_results = from_int(obj.get("totalResults"))
        return PageInfo(results_per_page, total_results)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resultsPerPage"] = from_int(self.results_per_page)
        result["totalResults"] = from_int(self.total_results)
        return result


@dataclass
class PlaylistItems:
    items: List[Item]
    next_page_token: str
    page_info: PageInfo

    @staticmethod
    def from_dict(obj: Any) -> 'PlaylistItems':
        assert isinstance(obj, dict)
        items = from_list(Item.from_dict, obj.get("items"))
        next_page_token = from_str(obj.get("nextPageToken"))
        page_info = PageInfo.from_dict(obj.get("pageInfo"))
        return PlaylistItems(items, next_page_token, page_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        result["nextPageToken"] = from_str(self.next_page_token)
        result["pageInfo"] = to_class(PageInfo, self.page_info)
        return result


def playlist_items_from_dict(s: Any) -> PlaylistItems:
    return PlaylistItems.from_dict(s)


def playlist_items_to_dict(x: PlaylistItems) -> Any:
    return to_class(PlaylistItems, x)
