# This is a sample Python script.
import requests
import json
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def api_call_fox(url_link):
    response = requests.get(url_link)
    #print(response.status_code)
    #print(response.json())
    fox_img = response.json()
    #print(fox_img['image'])

    #df = pd.json_normalize(fox_img, 'image')
    df = pd.json_normalize(fox_img)
    print(df)

def api_call_bible(url_link):
    response = requests.get(url_link)
    bible_dict = response.json()

    df = pd.json_normalize(bible_dict)
    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #api_call_fox('https://randomfox.ca/floof')
    api_call_bible('https://bible-api.com/BOOK+CHAPTER:VERSE')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
