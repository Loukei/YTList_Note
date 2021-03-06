# Youtube Data API note

## 目標

### 從YT playlist 網址抓取裡面的內容

Playlist 網址範例:
- [Popular Programming Courses](https://www.youtube.com/playlist?list=PLWKjhJtqVAblfum5WiQblKPwIbqYXkDoC)

抓取的內容包含:
- Playlist
  - 名稱
  - 說明
  - 底下的影片
    - 影片標題
    - 時長
    - 發布時間
    - 在playlist的順序

- 要收集以上資訊必須要兩種resources
  - playlists: 
    - 紀錄播放清單的**標題**、**描述**、發布時間等
  - PlaylistItems: 
    - 紀錄播放清單內的影片資訊，包含標題、時長、在影片內的順序等

## 抓取單一(教學)影片課程大綱

- 需要的資料:
  - title:                影片名稱
  - duration:             影片時長
  - description:          影片敘述
  - chapters:             影片的各個章節，這是YT的一種功能，可以把影片根據起始時間分段
    - chapter_start       章節開始時間
    - chapter_description 章節敘述

### 方法

- [Videos: list](https://developers.google.com/youtube/v3/docs/videos/list?apix_params=%7B%22part%22%3A%5B%22snippet%22%5D%2C%22id%22%3A%5B%22bC7o8P_Ste4%22%5D%7D)
  - 用來取得影片的資料

#### Request

`GET https://www.googleapis.com/youtube/v3/videos`

需要以下參數
- part: 
  - 用來指名需要video的那些資訊，以需求而言固定會是"snippet"
- id: 
  - 影片的id，可以從分享網址裡面取得，比如"https://youtu.be/8YDf5qfoRYI"的id為"8YDf5qfoRYI"
- key: 
  - 開發者申請的Youtube Data API V3的金鑰
- Accept:
  - 指定的資料回傳格式"application/json"
- Authorization:
  - 開發者的 API OAuth token，但是我們的需求不需要查看私人影片，所以**不用取得User同意**  

把對應的範例request轉成程式碼:
  
1. 直接點擊`use case`的HTTP sample
2. 把Sample複製到Postman裡面貼上，直接從code snippet產生`requests`程式碼再稍微修改即可

``` http
GET https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=Ks-_Mh1QhMc&key=[YOUR_API_KEY] HTTP/1.1

Authorization: Bearer [YOUR_ACCESS_TOKEN] // NO NEED
Accept: application/json
```

#### Reply

- 章節的資料被包含在`["snippet"].["description"]`裡面
  - 所以可能要寫個Regex才能撈出章節資料
  - YT規定每個影片至少要有三個章節
  - 第一個章節要從 00:00 開始
- 影片的總時長要用`part=contentDetails`取得

#### Ref

- [How do I get info about a Youtube video's chapters from the API?](https://stackoverflow.com/questions/63821605/how-do-i-get-info-about-a-youtube-videos-chapters-from-the-api)
- [影片章節](https://support.google.com/youtube/answer/9884579?hl=zh-Hant)
- [How do I get video durations with YouTube API version 3?](https://stackoverflow.com/questions/15596753/how-do-i-get-video-durations-with-youtube-api-version-3)
- [Python爬蟲實例 YouTube-使用 YouTube Data API](https://blog.jiatool.com/posts/youtube_spider_api/#-%E7%88%AC%E8%9F%B2%E7%A8%8B%E5%BC%8F)

---

## 目標

### 抓取影片的資訊

有些課程會使用Youtube Chapter功能把一門課做成單一影片，因此一部影片就是一門課程

影片資訊:
- title:                影片名稱
- duration:             影片時長
- description:          影片敘述
- chapters:             影片的各個章節，這是YT的一種功能，可以把影片根據起始時間分段
  - chapter_start       章節開始時間
  - chapter_description 章節敘述

### 抓取影片清單的資訊

一門課程以播放清單的形式出現，一個章節一部影片
- 名稱
- 說明
- 底下的影片
  - 影片標題
  - 時長
  - 發布時間
  - 在playlist的順序

## 方法

### get video data

**Videos: list**

用來抓取(1到多個)影片資訊

**Request parameter**

- part: 要求YT Server提供的影片資訊細節，基本上我們需要
  - `snippet`: 標題、描述、頻道名稱、上傳時間
  - `contentDetails`: 時長
- id: 影片的資源ID，如果要一次傳回多部影片也可以使用list形式
- key: Youtube Data API key
- fields

**額外的工作**

video resource 沒有紀錄底下的Chapter資訊，相對的這些資訊記錄在影片描述裡面。
參見[How do I get info about a Youtube video's chapters from the API?](https://stackoverflow.com/questions/63821605/how-do-i-get-info-about-a-youtube-videos-chapters-from-the-api)

- [Videos: list](https://developers.google.com/youtube/v3/docs/videos/list)

---

### get playlist data

playlist比較複雜，我們需要至少2個Method

**Playlists: list**

用來提供Playlist本身資料，包含名稱、建立者、描述、發布時間

- [Playlists: list](https://developers.google.com/youtube/v3/docs/playlists/list)

**PlaylistItems: list**

用來提供Playlist底下的有那些影片以及那些影片的訊息

- [PlaylistItems: list](https://developers.google.com/youtube/v3/docs/playlistItems/list)

---

## Ref

- [Google API Client](https://github.com/googleapis/google-api-python-client)

### Related Article

- [How to get the title of a playlist from the YouTube API](https://stackoverflow.com/questions/68648806/how-to-get-the-title-of-a-playlist-from-the-youtube-api)
- [How to use the fields parameter](https://developers.google.com/youtube/v3/getting-started)
