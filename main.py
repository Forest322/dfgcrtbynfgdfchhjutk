from flask import Flask, make_response, request, session
import secrets
from user import User, create_user_table
from post import Post, create_post_table

create_user_table()
create_post_table()

app = Flask(__name__)
app.secret_key = secrets.token_bytes(32)
print(app.secret_key) 



@app.route('/')
def index_page():
    response = make_response('<a href="/get">Посмотерь куки файлы</a>')

    session['name'] = 'efeversbrthjmnhufg'
    return response

@app.route('/get')
def get_page():
    name = session.get('name')

    return name + "<br> <a href='/'>Получить куки</a>"


app.run(host='0.0.0.0', port=8080)
