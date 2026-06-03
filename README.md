# Task Manager

FlaskとSQLiteを用いて開発したタスク管理Webアプリです。

## URL
[https://xxxxx.onrender.com](https://crud-taskmanager.onrender.com/)

## テストアカウント

- ユーザーname: arr
- パスワード: arrarr

## 概要

本アプリは、日々のタスクを効率的に管理するためのWebアプリケーションです。

ユーザー登録・ログイン機能を実装しており、ユーザーごとにタスクを管理できます。タスクにはカテゴリ（Main / Sub）と実行時間を設定でき、優先度や用途に応じて整理できます。

### 特徴

- ユーザー認証機能
- タスクの追加・閲覧・削除
- Main / Sub によるカテゴリ分け
- タスク実行時間の設定
- レスポンシブデザイン対応

---

## 使用技術

### フロントエンド

- HTML
- CSS
- JavaScript

### バックエンド

- Python 3
- Flask

### データベース

- SQLite3

### デプロイ

- Gunicorn
- Render

---

## 機能

### ユーザー認証

- ユーザー登録
- ログイン
- ログアウト

### タスク管理

- タスク追加
- タスク一覧表示
- タスク削除
- カテゴリ管理（Main / Sub）
- 時間設定

---

## ユーザーができること

### アカウント作成

ユーザー登録を行い、自分専用のタスクを管理できます。

### タスク管理

例えば以下のような利用が可能です。

#### Main

- レポート作成
- 就職活動
- 卒業研究

#### Sub

- 読書
- 筋トレ
- 趣味

### タスク削除

不要になったタスクを削除できます。

---

## システム構成

```text
ユーザー登録
      ↓
ログイン
      ↓
セッション発行
      ↓
ホーム画面表示
      ↓
タスク追加
      ↓
SQLiteへ保存
      ↓
タスク一覧表示
      ↓
タスク削除
```

---

## データベース設計

### users

| カラム名 | 型 | 説明 |
|----------|----|------|
| id | INTEGER | ユーザーID |
| name | TEXT | ユーザー名 |
| password | TEXT | パスワード |

### tasks

| カラム名 | 型 | 説明 |
|----------|----|------|
| id | INTEGER | タスクID |
| user_id | INTEGER | ユーザーID |
| title | TEXT | タスク名 |
| category | TEXT | Main / Sub |
| task_time | TEXT | 実行時間 |

---

## ディレクトリ構成

```text
task-manager/
│
├── server.py
├── database.py
├── task.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── home.html
│
├── static/
│   └── style.css
│
└── README.md
```

---


## 今後の改善点

現在、以下の機能追加を検討しています。

- タスク編集機能
- タスク完了機能
- タスク件数表示
- 達成率表示
- 締切日設定
- 優先度設定
- PostgreSQL対応
- Docker対応
- パスワードのハッシュ化
- ダークモード切替

---

## デモ

### ログイン画面

<img width="1139" height="838" alt="スクリーンショット 2026-06-03 12 19 10" src="https://github.com/user-attachments/assets/77be6d0d-f441-4ab0-9ceb-abeab482a221" />

### 新規登録画面<img width="970" height="814" alt="スクリーンショット 2026-06-03 12 19 20" src="https://github.com/user-attachments/assets/4f5c766b-aac5-4049-9922-1ef28b164cf5" />

### ホーム画面(メイン)

<img width="1026" height="762" alt="スクリーンショット 2026-06-03 12 18 58" src="https://github.com/user-attachments/assets/ebd7963d-dd29-4513-99fd-98ad2561125b" />

---
