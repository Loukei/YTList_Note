# YTList_Note

Turn youtube playlist or youtube video title into markdown note.

[![OSCS Status](https://www.oscs1024.com/platform/badge/Loukei/YTList_Note.svg?size=small)](https://www.oscs1024.com/project/Loukei/YTList_Note?ref=badge_small)

## 情況

學習線上課程時，按照播放清單來建立Markdown章節筆記，減少複製貼上的工作。

## 步驟

### 輸入:

``` python
( yt_url:str, yt_apikey:str, template_path:str)
```

- yt_url:         Youtube 網址，可能是**playlist網址**或**影片網址**
- yt_apikey:      使用者申請的YouTube Data v3 API key
- template_path:  使用者事先寫好的markdown模板

### 輸出: 

Markdown file

### 功能:

這個腳本在執行時通過讀取YT的網址，將播放清單依照User事先定義好的模板檔案`template_path`渲染成想要的樣子。
以播放清單為例，多數會使用列表式的清單整理成章節標題，但也有些情況下會使用表格來處理。

## TODO

- 對URL的解析，需要了解regex pattern分發機制，把網址裡的`video_id`與`playlist_id`提取出來
- 撰寫一個解析Chapter的函數來把章節資料提取出來
- 撰寫Playlist的view
  - 將`playlists`添加回`render_playlist()`函數
- 整理YT API 筆記 與 devlop log

## 資源

- Youtube API resources
  - [Playlists: list](https://developers.google.com/youtube/v3/docs/playlists/list)
  - [Videos: list](https://developers.google.com/youtube/v3/docs/videos/list)
  - [PlaylistItems: list](https://developers.google.com/youtube/v3/docs/playlistItems/list)
  - [Google API Client](https://github.com/googleapis/google-api-python-client)
- [Jinja2](http://docs.jinkan.org/docs/jinja2/)
- [YouTube Data OpenAPI SPEC file](https://apiharmony-open.mybluemix.net/public/apis/google_youtube_api#_information)