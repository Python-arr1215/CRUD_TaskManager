from flask import Flask, render_template, request, redirect, session
import database

app = Flask(__name__)
app.secret_key = "7e090be815781ee60b3ae595ccd024f78fe2606595880f995d96964210a55641"

database.create_tables()

# サンプルのユーザー情報
users = {

}


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']

    user = database.login_user(username, password)

    if user:
        session["user_id"] = user["id"]
        return redirect("/home")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database.register_user(username, password)

        return redirect("/")

    return render_template('register.html')


# ダッシュボード
@app.route("/home", methods=["GET", "POST"])
def homes():
    # ログイン確認
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]

    # タスク追加
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        task_time = request.form["task_time"]
        database.Create(user_id, title, category, task_time)

    # 自分のタスク取得
    tasks = database.Read(user_id)
    

    return render_template(
        "home.html",
        tasks=tasks

    )

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):

    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]

    database.Delete(task_id, user_id)

    return redirect("/home")