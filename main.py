import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import re
import argparse
import tkinter as tk
from tkinter import filedialog, simpledialog

def ask_question():
    response = input('Please provide a URL: ')
    return response

def ask_question_gui():
    root = tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    response = simpledialog.askstring('URL', 'Please provide a URL')
    return response

def ask_folder():
    folder_selected = input('Please provide a folder path: ')
    return folder_selected

def ask_folder_gui():
    root = tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    folder_selected = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
    return folder_selected

def main():
    parser = argparse.ArgumentParser(description="Web scraper")
    parser.add_argument('-u', '--url', type=str, help='The URL to scrape')
    parser.add_argument('-f', '--folder_path', type=str, help='The folder path to save the file')
    parser.add_argument('-g', '--gui', action='store_true', help='Use GUI to ask for folder path')
    args = parser.parse_args()

    url = args.url
    save_folder_path = args.folder_path

    if url is None:
        if args.gui:
            url = ask_question_gui()
        else:
            url = ask_question()

    if save_folder_path is None:
        if args.gui:
            save_folder_path = ask_folder_gui()
        else:
            save_folder_path = ask_folder()

    # URLからHTMLを取得します
    response = requests.get(url)

    # BeautifulSoupを使用してHTMLをパースします
    soup = BeautifulSoup(response.text, 'html.parser')

    # h1タグの内容を取得し、不適切な文字を取り除きます
    file_name = soup.find('h1').text
    file_name = re.sub(r'[\\/:"*?<>|]', '', file_name) # ファイル名として使用できない文字を取り除く

    # ファイル名に.mdを追加します
    file_name = file_name + '.md'
    file_name = os.path.join(save_folder_path, file_name)

    # groupクラスの内容を取得します
    groups = soup.find_all(class_='group')

    # Markdownファイルに保存します
    with open(file_name, 'w', encoding='utf-8') as f:
        # h1タグの内容を書き込みます
        f.write('# ' + os.path.basename(file_name).replace('.md', '') + '\n\n')
        
        # groupクラスの内容を書き込みます
        for i, group in enumerate(groups):
            if i % 2 == 0:
                f.write('User:\n')
            else:
                f.write('ChatGPT:\n')
            markdown_text = md(str(group))
            
            # 不要な文字列を削除します
            markdown_text = re.sub(r'【\d+†source】', '', markdown_text)
            
            # ゼロ幅スペースを削除します
            markdown_text = markdown_text.replace('&#8203;', '')

            f.write(markdown_text + '\n\n')

if __name__ == "__main__":
    main()