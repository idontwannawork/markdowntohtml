# Convert Markdown to HTML

## 概要

PythonでMarkdownファイルをHTMLへ変換する。

## 環境

* Python ※3.x系
* Markdown

[Markdown](https://python-markdown.github.io/)は事前に`pip`しておく。

```console
pip install Markdown
```

## 詳細

### ファイル

* mdtohtml.py

    Pythonで記述された本体。実行には当ファイルを指定する。

* style.css

    CSSが書かれたファイル。生成されたHTMLファイルに`<style>`タグで記述される。スタイルの変更を行いたい場合、当ファイルを書き換えてHTMLを生成する。

### 使い方

1. 変換したいmdファイルがあるフォルダに上記の2ファイルを配置する。

    ```console
    $ ls
    README.md    iamacat.md   main.css     mdtohtml.py  style.css
    ```

1. 配置したら、そのフォルダにて下記のコマンドを実行する。

    ```console
    $ python mdtohtml.py
    iamacat.md の変換を開始します
    -----------------------------------
    iamacat.md を iamacat.html へ変換しました
    README.md の変換を開始します
    -----------------------------------
    README.md を README.html へ変換しました
    $ ls
    README.html   README.md     iamacat.html  iamacat.md    main.css      mdtohtml.py   style.css
    ```

### 処理内容

実行されたフォルダ中に存在するmdファイルを取得して、HTMLファイルに変換して同じフォルダーに出力する。mdファイルが複数ある場合は、すべてHTML化する。
