import json


icon = []
cover = []
assets = []

class Json_Process():

    def __init__(self):
        self.json_file = json.load(open('/Users/tq/Desktop/BYSJ/json1/icon.json'))  # json 配置文件路径（1）

    def first_key(self):

        for i in self.json_file:
            self.second_key(self.json_file.get(i))

    def second_key(self,js):

        for j in js:
            if type(js.get(j)) is list:         # 当value为list型时，迭代list
                for i in js.get(j):
                    if type(i) is dict:         # 当value为dict型时，迭代json文件
                        self.second_key(i)
            elif type(js.get(j)) is dict:       # 当value为dict型时，迭代json文件
                self.second_key(js.get(j))      # 迭代json文件
            elif type(js.get(j)) is str:        # 当迭代到value为字符串类型时，停止迭代
                if j == 'cover':
                    if js.get(j) == '':  # 当value值为空时，排除该字典项
                        pass
                    else:
                        cover.append({'title':js.get(j),'cover':js.get(j)})
                        # print(j + ":" + js.get(j))  # 输出cover值
                elif j == 'assets':
                    assets.append(js.get(j))
                    print(j + ":" + js.get(j))
                elif j == 'icon':
                    icon_name = js.get('title')
                    icon_title_list = []
                    for i in icon:
                        icon_title_list.append(i.get('title'))
                    if icon_name in icon_title_list:
                        icon_name = str(icon_name) + "_another"
                    icon.append({'title': icon_name, 'icon': js.get(j)})
                    # print(js.get('title'), j + ":", js.get(j))




# Json_Process().first_key()
