import requests
import os
import json
import time

os.environ['NO_PROXY'] = '127.0.0.1'


def post(text: str):
    return requests.post(
        "http://127.0.0.1:8000/faq",
        json={
            'text': text
        }
    ).json()

def checkFolder():
    if not os.path.exists('BetterQuestion'):
        os.mkdir('BetterQuestion')
        for i in os.listdir("./WithSummary"):
            os.mkdir("BetterQuestion/" + i)
    else:
        for i in os.listdir('BetterQuestion'):
            os.rmdir('BetterQuestion/' + i)
        os.rmdir('BetterQuestion')
        checkFolder()

#checkFolder()

FOLDERS = sorted([(len(os.listdir("./WithSummary/" + i)), i) for i in os.listdir("./WithSummary") if len(os.listdir("./WithSummary/" + i))])

startTime = time.time()
for _, i in FOLDERS[18:19]:
    print(f"________{i} {_} files________")
    for j in os.listdir("./WithSummary/" + i):
        try:
            print(j)
            article = {}
            with open("./WithSummary/" + i + "/" + j, 'r') as f:
                article = json.load(f)
                del article["faq"]
            article["faq"] = post(article['content'])
            with open("./BetterQuestion/" + i + "/" + j, 'w') as f:
                json.dump(article, f)
        except:
            print("Skipped file: " + j)
print(time.time() - startTime)

