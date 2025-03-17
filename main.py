from flask import Flask, make_response, request, session, render_template,redirect
import secrets

from user import User, create_user_table
from post import Post, create_post_table

create_user_table()
create_post_table()

app = Flask(__name__)
app.secret_key = secrets.token_bytes(32)
 



@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        user = User.get_user_by_username(username)
        pas_hash = User.hashed_password(password)
        if not user:
            error = "Неправильный логин или пароль"

        if pas_hash != user.password_hash:
            error = "Неправильный логин или пароль"

        if error:
            return render_template("register.html", error=error)

        session["username"] = username
        return redirect("/")

@app.route('/registration', methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        error = None

        user = User.get_user_by_username(username)
        if user:
            error = 'Такой пользовтель уже существует'

        if password != confirm_password:
            error = 'Пароли не совпадают'


        if error:
            return render_template("register.html", error=error)

        User.create(username, password)
        session["username"] = username
        return redirect("/")
    

@app.route('/logout')
def logout_page():
    username = session.get("username")
    if username:
        del session["username"]
    return redirect('/login')
    



@app.route('/profile')
def profile_page():
    return ""


app.run(host='0.0.0.0', port=8080, debug=True)
