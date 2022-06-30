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

- 搞懂輸出方式是否符合需求`template.py`
  - 目的
    - 學後端開發時Template多是用來傳送到網路上的`html`，能不能做成`.md`輸出到本地資料夾?
  - 步驟
    - 嘗試Jinja2的基本使用方式
      - 安裝
      - 建立簡單的模板輸出`print`
      - 能否輸出markdown檔案
      - jinja2 如何讀取本地資料夾的模板
      - 模板是如何與model互動
- 建立模型層`model.py`
  - 嘗試YT Data API v3
    - 目的
      - 搞懂API傳給我的資料模型長怎樣，是否需要一些額外工作，比如申請金鑰
    - 步驟
      - 按照官方教學申請金鑰
      - 使用`Requests`，比起安裝整包的`google-api-python-client`更小
      - 直接搜尋需要的資源`Videos`與`Playlist`並閱讀
      - 跑一下**API Explores**上的範例
      - 複製`HTTP`的範例，放到Postman上面看看是否能重現
        - 確認之前的OAuth2認證金鑰是否能用
      - 把Postman上的python程式碼複製下來看能不能用python實現呼叫
  - 用QuickType快速生成我們需要的`models.py`
    - 複製Postman上面的JSON reply存檔`videos_example.json`
    - 按照YT官方文件，除了我們感興趣的屬性以外，其餘的都刪掉
      - 如果屬性值有長字串，則可以刪掉多餘的內容，減少QuickType處裡時間
    - 將修改過後的`videos_example.json`貼到QuickType來快速製作`models.py`
    - 測試`models.py`

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

## 資源

- [Playlists: list](https://developers.google.com/youtube/v3/docs/playlists/list) 
- [Jinja2](http://docs.jinkan.org/docs/jinja2/)