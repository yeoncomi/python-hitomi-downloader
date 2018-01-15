#모듈 임포팅
import json
import requests
import urllib
import threading
import sys
import os

#크롤 정의
def croll(data, index):
    gallery = "https://0a.hitomi.la/galleries/"
    link = gallery + index + "/" + data

    print(link)
    urllib.request.urlretrieve(link, "download/" + data)

if __name__ == "__main__":
    if not os.path.exists("download"):
        os.makedirs("download")

    index = str(input("Enter the hitomi(exthntai) number: "))
    Hitomi_js = requests
        .get("https://hitomi.la/galleries/" + index + ".js")
        .text.replace("var galleryinfo = ", "")
    Hitomi_list = json.loads(Hitomi_js)

    for data in Hitomi_list:
        name = data["name"]

        print(name + " / " + index)
        threading.Thread(target = croll, args = [name, index]).start()
        print("process " + name + " started")

print("Download Done")
sys.exit(1)
