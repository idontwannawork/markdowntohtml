import markdown
import re
import os
import glob

# Markdown拡張
mdextensions = ["tables"]


# ディレクトリ全探索
def find_all(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


# カレントディレクトリから１番最初に見つかるファイル相対PATHを取得
def onefind_path(filename):
    for path in find_all('.'):
        if re.search(filename + '$', path):
            return path


# mdファイルの変換
def convertHtml(mdpath, htmlpath, style):
    with open(mdpath, 'rt', encoding="utf-8") as f:
        text = f.read()
        # Markdown の import 文を除去
        text = re.sub('@import ".+"\n', '', text)
        # HTMLに変換
        body = markdown.Markdown(extensions=mdextensions).convert(text)

        html = '<html lang="ja"><meta charset="utf-8">'
        html += '<style>' + style + '</style>'
        html += '<body>' + body + '</body></html>'

        # HTMLで出力
        with open((htmlpath), "w", encoding="utf-8") as g:
            g.write(html)


if __name__ == '__main__':

    # スタイルは、style.cssを参照する
    with open(onefind_path('style.css'), 'rt', encoding="utf-8") as f:
        style = f.read()
        for mdfile in glob.glob("*.md"):
            print("%s の変換を開始します" % mdfile)
            htmlname = re.sub(r'.md$', '.html', mdfile)
            convertHtml(mdfile, htmlname, style)
            print("-----------------------------------")
            print("%s を %s へ変換しました" % (mdfile, htmlname))
