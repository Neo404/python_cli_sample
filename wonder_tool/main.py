#-*- coding: utf-8 -*-
import sys
import urllib.parse
import urllib.request
import json
import requests as rq

def proofreading(check_message):
    APIKEY = ""

    url = "https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo?"

    sentence=check_message

    params = urllib.parse.urlencode(
                {'apikey': APIKEY,
                'sentence': sentence})
    response = rq.get(url+params)

    data = json.loads(response.text)
    return data


def wonder_main(argv=sys.argv[1:]):
    print("What a wonder!")
    if len(argv) == 1:
        data = proofreading(argv)
        print("InputSentence: " + data["inputSentence"])
        print("CheckSentence: "data["checkedSentence"])

if __name__ == "__main__":
    wonder_main()
