import os
import markdown
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    with open(os.path(app.root_path) + '/README.md', 'r') as markdown:
        content = markdown.read()
        return markdown.markdown(content) 
