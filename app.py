from asyncio import run

import pip
from pip._internal.vcs import git

pip install Flask
pip install flask

flask --version
flask run
python -m flask run
python -m flask run

python -m nenv myenv
myenv\Scripts\activate
python -m nenv myenv\Scripts\activate

from flask import Flask
app = Flask(__app.py__)
@app.route('/api/data', methods=['GET'])
def get_data():
    return 'This is a GET request'

@app.route('/api/data', methods=['POST'])
def post_data():
    return 'This is a POST request'
if __name__ == '__main__':
    app.run(debug=True)


python app.py
flask run

python app.py
curl -X POST http://127.0.0.1:5000/data

my_flask_api

app.py
requirements.txt
README.md
requirements_dev.txt
README.md

git init

# Virtual environment
venv/

#Byte-compiled / optimized files
__pycache__/
*.pyc

# IDE-specific files
.vscode/

git add .
git commit -m "Initial commit: Setting up Flask API"

git push origin master
