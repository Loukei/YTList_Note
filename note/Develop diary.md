# Develop Diary

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

### 1. 使用 Youtube Data API v3

### 2. 使用 爬蟲

#### 打開撥放清單的網頁然後直接左鍵選取複製貼上

``` txt
6:09
現正播放
Introduction to Git | Google IT Automation with Python Certificate
Google Career Certificates

2

55:58
現正播放
Github Collaboration Tools | Google IT Automation with Python Certificate
Google Career Certificates

3

58:11
現正播放
GitHub Tutorial Beginners | Google IT Automation with Python Certificate
Google Career Certificates
```

##### 缺點: 

需要每次手動整理內容，因為格式很亂，更好一點方法是下載成`html`然後解析內容

#### 使用瀏覽器工具

- [Learning Notes Plus](https://chrome.google.com/webstore/detail/learning-notes-plus/oldidllbanodgoopjgjfnphdioefllcd?utm_source=chrome-ntp-icon)

##### 評價:

**LN+**建立在notion之上，而且目前使用起來他只是簡單的擷取影片標題與鏈結，因此課程筆記的組織方式就不是那麼有彈性，比如有些人會在筆記裡加入GUID等特定編號。

對只想立刻開始的使用者，直接用**LN+**很方便且不用太多設定

#### 直接在瀏覽器 Console 裡撰寫爬蟲

- [How to use the browser console to scrape and save data in a file with JavaScript](https://www.freecodecamp.org/news/how-to-use-the-browser-console-to-scrape-and-save-data-in-a-file-with-javascript-b40f4ded87ef/)

#### 無程式碼的抓取工具

SelectorGadget + XPath Helper

##### 評價:

使用這類工具要有一點爬蟲知識，理解網頁結構與XPath、CSS selector之類，才能很好的使用

### 3. 使用低程式碼的流程工具

- [Pipedream: Connect APIs, Remarkably Fast](https://pipedream.com/)
- [n8n](https://github.com/n8n-io/n8n)

## 任務紀錄

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
      - **(採坑)**要注意複製下來的JOSN檔案格式有沒有被破壞，不然後面會沒辦法讀檔
    - 按照YT官方文件，除了我們感興趣的屬性以外，其餘的都刪掉
      - 如果屬性值有長字串，則可以刪掉多餘的內容，減少QuickType處理時間
    - 將修改過後的`videos_example.json`貼到QuickType來快速製作`models.py`
      - 建議先把JSON轉成JSON schema，因為有些文字格式像是`email,date,address,IP`可以在schema裡面做手動修正
        - [JSON Schema - string](https://json-schema.org/understanding-json-schema/reference/string.html#dates-and-times)
      - QuickType目前不支援JSON Schema的`duration`格式
      ~~- 正在考慮不用Quick改成自己寫，一部分是因為原本的結構比較複雜，另一部分是解析章節(chapter)的部分還是要自己做~~
        ~~- 使用[轉接器模式](https://en.wikipedia.org/wiki/Adapter_pattern)，將自動產生的程式碼重新包裝成自己要的結構，比自己重新寫更好~~
    - 測試`models.py`
- 建立URL Dispatch function
  - 功能
    - User輸入任意URL，dispatch 自動擷取影片ID or Playlist ID，並且將參數傳給適合的view function
    - 具體可以參考[URL dispatcher - Django documentation](https://docs.djangoproject.com/en/4.0/topics/http/urls/)
  - 方法
    - 目前沒有看到不用框架的URL dispatch lib
    - 使用`urllib.parse`來實作
      - 實際感想
        - 使用解析url的方式簡單但是比較缺乏彈性一些
          - 舉例:
            - 同一個影片可以有`https://www.youtube.com/watch?v=8jLOx1hD3_o`與`https://youtu.be/8jLOx1hD3_o`兩種模式，前者只需取得`query`字段，後者則需要取得末尾的路徑，但兩者都會對應到同一個取得影片資訊的函數
      - 結論
        - 使用`urllib.parse`缺乏彈性，同一個匹配模式不能用在所有的情況，如果將來要擴充到其他的平台會更複雜
    - 使用Regex正則表達式代替
      - 參考網路上的答案[How do I get the YouTube video ID from a URL?](https://stackoverflow.com/questions/3452546/how-do-i-get-the-youtube-video-id-from-a-url)