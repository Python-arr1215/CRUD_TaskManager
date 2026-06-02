# database.py

import sqlite3

DB_NAME = "task.db"


# DB接続
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# テーブル作成
def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    # 【重要】外部キー制約を有効にする
    cur.execute("PRAGMA foreign_keys = ON;")

    # usersテーブル
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # tasksテーブル
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        task_time TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


# ユーザー登録
def register_user(name, password):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, password) VALUES (?, ?)",
        (name, password)
    )

    conn.commit()
    conn.close()


# ログイン確認
def login_user(name, password):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE name=? AND password=?",
        (name, password)
    )

    user = cur.fetchone()
    conn.close()
    return user


# 主なCRUD機能

# タスク追加
def Create(user_id, title, category, task_time):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (user_id, title, category, task_time) VALUES (?, ?, ?, ?)",
        (user_id, title, category, task_time)
    )

    conn.commit()
    conn.close()


# タスク取得
def Read(user_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE user_id=? ORDER BY task_time DESC",
        (user_id,)
    )

    tasks = cur.fetchall()

    conn.close()

    return tasks


# 更新
def Update(task_id, user_id, new_title):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE tasks SET title = ? WHERE id = ? AND user_id = ?",
        (new_title, task_id, user_id)
    )

    conn.commit()
    conn.close()


# 削除
def Delete(task_id, user_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?",
                (task_id, user_id)
                )
    conn.commit()
    conn.close()