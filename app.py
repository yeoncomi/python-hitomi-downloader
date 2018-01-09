import json
import requests
import urllib
hitomi_number = input("히토미 번호를 입력해주세요: ")
Hitomi_request = requests.get('https://hitomi.la/galleries/'+hitomi_number+'.js')
Hitomi_js = Hitomi_request.text.replace("var galleryinfo = ","")
Hitomi_list = json.loads(Hitomi_js)
for x in Hitomi_list:
    print(x["name"])
    urllib.request.urlretrieve("https://0a.hitomi.la/galleries/"+str(hitomi_number)+"/"+str(x["name"]), "download/"+str(x["name"]))
