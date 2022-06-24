from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

def set_Jinja2_Env() -> Environment:
    template_path:str = './code/templates'
    env = Environment(loader=FileSystemLoader(template_path))
    return env

def test_index_data() -> dict:
    d:dict = {
        "list":[
            {'title': "title1"},{'title': "title2"},{'title': "title3"}
        ]
    }
    return d

def main():
    print('--- Main ---')
    env = set_Jinja2_Env()
    template = env.get_template('TestNote.md')
    print(template.render(data = test_index_data()))
    pass

if __name__ == '__main__':
    main()