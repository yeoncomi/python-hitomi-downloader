import json
import requests
import urllib
from multiprocessing import Process
import shutil

hitomi_number = input("히토미 번호를 입력해주세요: ")
Hitomi_request = requests.get('https://hitomi.la/galleries/'+hitomi_number+'.js')
Hitomi_js = Hitomi_request.text.replace("var galleryinfo = ","")
Hitomi_list = json.loads(Hitomi_js)

def request():
    for x in Hitomi_list:
        urllib.request.urlretrieve("https://0a.hitomi.la/galleries/"+str(hitomi_number)+"/"+str(x["name"]), "download/"+str(x["name"]))

procs = []
for x in Hitomi_list:
    proc = Process(target=request)
    procs.append(proc)
    proc.start()
    print("process",x["name"],"started")
for proc in procs:
    proc.join()
    print("process",proc,"dead")
shutil.make_archive(str(hitomi_number), 'zip', 'download')
