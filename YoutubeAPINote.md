
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

- [youtube api - videos:list](https://developers.google.com/youtube/v3/docs/videos/list?apix_params=%7B%22part%22%3A%5B%22snippet%22%5D%2C%22id%22%3A%5B%22rfscVS0vtbw%22%5D%7D)


### 從YT影片網址抓取內部的章節(Chapter)的段落名稱、時間點

- [How do I get info about a Youtube video's chapters from the API?](https://stackoverflow.com/questions/63821605/how-do-i-get-info-about-a-youtube-videos-chapters-from-the-api)