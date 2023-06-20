# ChatGPT-Share → Markdown
ChatGPTをShareした際に作成されるURLからデータを抽出し、Markdownファイルとして保存するPythonスクリプトです。
`requests`、`BeautifulSoup`、`markdownify`、`os`、`re`、`argparse`、および`tkinter`ライブラリを使用しています。

## 前提条件

スクリプトを実行する前に、以下の依存関係がインストールされていることを確認してください：

- requests
- BeautifulSoup
- markdownify
- tkinter

`pip`を使用してこれらの依存関係をインストールできます：

```
pip install requests beautifulsoup4 markdownify
```

## 使用方法

スクリプトを実行するには、次のコマンドを実行してください：

```
python script.py [-u URL] [-f FOLDER_PATH] [-g]
```

スクリプトは次のコマンドライン引数をサポートしています：

- `-u, --url URL`：スクレイピングするURLです。
- `-f, --folder_path FOLDER_PATH`：ファイルを保存するフォルダのパスです。
- `-g, --gui`：GUIを使用してフォルダのパスを入力します。

URLやフォルダのパスが引数として指定されていない場合、スクリプトはコマンドラインインターフェースまたはグラフィカルユーザーインターフェース（GUI）を使用して入力を求めます（`-g`フラグによって切り替えます）。

## スクリプトの概要

このスクリプトは以下の手順を実行します：

1. コマンドライン引数を解析して、URLとフォルダのパスを取得します。
2. URLやフォルダのパスが指定されていない場合、コマンドラインまたはGUIを介してユーザーに入力を求めます。
3. 指定されたURLからHTMLコンテンツを取得するためのHTTPリクエストを送信します。
4. BeautifulSoupを使用してHTMLをパースします。
5. `h1`タグの内容をファイル名として抽出し、無効な文字を削除します。
6. Markdownファイル名を".md"で追加し、保存フォルダのパスと結合します。
7. "group"というクラス名を持つ要素をすべて検索し、その内容を抽出します。
8. 抽出された内容をMarkdownファイルに書き込みます。グループごとに "User" と "ChatGPT" のラベルで区切ります。
9. 抽出したMarkdownテキストから不要な文字列や文字をクリーンアップします。
10. 抽出されたコンテンツを含むMarkdownファイルを指定したフォルダパスに保存します。