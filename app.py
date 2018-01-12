import json
import requests
import urllib
import threading
import sys
import os

def croll(data, hitomi_no):
    print("https://0a.hitomi.la/galleries/" + hitomi_no + "/" + data)
    urllib.request.urlretrieve("https://0a.hitomi.la/galleries/" + hitomi_no + "/" + data, "download/" + data)

if(__name__ == '__main__'):
    hitomi_no = str(input("Enter the hitomi(exthntai) number: "))
    Hitomi_request = requests.get('https://hitomi.la/galleries/' + hitomi_no + '.js')
    Hitomi_js = Hitomi_request.text.replace("var galleryinfo = ","")
    Hitomi_list = json.loads(Hitomi_js)

    if(not os.path.exists('download')):
        os.makedirs('download')

    for data in Hitomi_list:
        print(data["name"] + ' / ' + hitomi_no)
        threading.Thread(target = croll, args = [data["name"], hitomi_no]).start()
        print("process " + data["name"] + " started")
print("Download Done")
sys.exit(1)
