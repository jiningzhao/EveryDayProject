import requests
import json
def fanyi(word=None):
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    Form_data={"i": word,
               "from": "AUTO",
               "to": "AUTO",
               "smartresult": "dict",
               "client": "fanyideskweb",
               "salt": "15646700814688",
               "sign": "79a694c097070997233b2284aadb1420",
               "ts": "1564670081468",
               "bv": "316dd52438d41a1d675c1d848edf4877",
               "doctype": "json",
               "version": "2.1",
               "keyfrom": "fanyi.web",
               "action": "FY_BY_REALTlME"
               }
    return url,headers,Form_data
if __name__ == '__main__':
    # word="我爱你"
    word=str(input("请输入你要翻译的句子："))
    url,headers,Form_data=fanyi(word)
    html=requests.post(url,data=Form_data,headers=headers)
    # print(html.content)
    content=json.loads(html.text)
    print(content['translateResult'][0][0]['tgt'])

