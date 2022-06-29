# YTList_Note

A script that Youtube (course) playlist on markdown note.

## 情況

學習線上課程時，按照播放清單來建立Markdown章節筆記，減少複製貼上的工作。

## 步驟

輸入:

( Youtube API playlist網址 or youtube 影片網址 ) + ( 使用者的Youtube api key ) + ( 使用者定義的Jinja 2 Markdown 模板 )

輸出: 

Markdown file

功能:

這個腳本在執行時通過讀取YT的網址，將播放清單轉換成Markdown的列表，如果使用者可以通過事先撰寫的模板換成Table等形式

## 任務

- 搞懂**Jinja2**模板基礎語法
- 使用**Jinja2**建立一個基本的markdown模板
  - 該模板建立一個章節區塊
- 查看 YT API 取得的資料欄位
  - 排行、影片標題、影片時長...

## Next step

- 嘗試YT API
  - 建立影片模型
    - 如何記錄影片時間?
      - 使用`timedelta`
        - 要特別處理字串與時間的轉換
  - 考慮使用官方API直接寫
    - 會比較肥，因為它包含了一些其他的服務
  - 如果用QuickType來用，做model會比較快
    - 要研究`json_schema`，比較能做出準確的模型
      - [json schema foramt](https://opis.io/json-schema/2.x/formats.html) 

- [模板设计者文档](http://docs.jinkan.org/docs/jinja2/templates.html)
- [jinja2.Template.render](http://docs.jinkan.org/docs/jinja2/api.html#jinja2.Template.render) 
- [jinja2.FileSystemLoader](http://docs.jinkan.org/docs/jinja2/api.html?highlight=filesystemloader#jinja2.FileSystemLoader)

## 資源

- [Playlists: list](https://developers.google.com/youtube/v3/docs/playlists/list) 
- [Jinja2](http://docs.jinkan.org/docs/jinja2/)