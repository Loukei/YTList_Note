##

安裝
`pipenv install jinja2`

## 步驟

- 建立環境`Environment`
  - 用來指定package(可能是指類似django的Application)
  - 也可以用來指定某個本地的資料夾

``` python
from jinja2 import Environment

def set_Jinja2_Env() -> Environment:
    template_path:str = './code/templates'
    env = Environment(loader=FileSystemLoader(template_path))
    return env
```

- 在`Templates`資料夾內存放要使用的模板

``` markdown
## Title

{{ data }}
```

- 從`Environment`建立一個實體`env`，並且用`env`建立一個`Template`實體`template`
    - 建立`template`時需指定使用的模板檔案路徑

``` python
env = set_Jinja2_Env()
template = env.get_template('TestNote.md')
```

- 有兩種方式可以渲染模板

``` python
print(template.render(data = test_index_data())) // 輸出字串
template.stream(data = test_index_data()).dump('note_out.md',encoding='utf8') //經由文件流輸出到指定檔案
```

- [How do I render jinja2 output to a file in Python instead of a Browser](https://stackoverflow.com/questions/11857530/how-do-i-render-jinja2-output-to-a-file-in-python-instead-of-a-browser)
- [class jinja2.environment.TemplateStream](http://docs.jinkan.org/docs/jinja2/api.html?highlight=stream#jinja2.environment.TemplateStream)

- [模板设计者文档](http://docs.jinkan.org/docs/jinja2/templates.html)
- [jinja2.Template.render](http://docs.jinkan.org/docs/jinja2/api.html#jinja2.Template.render) 
- [jinja2.FileSystemLoader](http://docs.jinkan.org/docs/jinja2/api.html?highlight=filesystemloader#jinja2.FileSystemLoader)