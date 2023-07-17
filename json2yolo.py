import os
import json

# labelme标注的json标签文件目录和保存生成的txt标签的文件夹
dir_json = r'D:\duanyongping\project\deepLearn\airplanepic/'
dir_txt = r'D:\duanyongping\project\deepLearn\airplanepic\label/' # txt存储目录
os.mkdir(dir_txt)

def json2txt(path_json, path_txt):  # 可修改生成格式
    with open(path_json, 'r',encoding='utf-8') as path_json:
        jsonx = json.load(path_json)
        with open(path_txt, 'w+') as ftxt:
            shapes = jsonx['shapes']
            #获取图片长和宽
            width=jsonx['imageWidth']
            height=jsonx['imageHeight']
            for shape in shapes:
               #获取矩形框两个角点坐标
                x1 = shape['points'][0][0]
                y1 = shape['points'][0][1]
                x2 = shape['points'][1][0]
                y2 = shape['points'][1][1]
                if shape['label']=='anniu': # 对应类别转为数字代号
                    cat=80
                elif shape['label']=='kaiguan':
                    cat=81
                elif shape['label']=='xuanniu':
                    cat=82
                elif shape['label']=='xianshi':
                    cat=83
                else:
                    cat=84
                                 
                #对结果进行归一化
                dw = 1. / width
                dh = 1. / height
                x=dw *(x1+x2)/2
                y=dh *(y1+y2)/2
                w=dw *abs(x2-x1)
                h = dh * abs(y2 - y1)
                yolo = f"{cat} {x} {y} {w} {h} \n"
                ftxt.writelines(yolo)

list_json = os.listdir(dir_json)
for cnt, json_name in enumerate(list_json):
    if os.path.splitext(json_name)[-1] == ".json":
        path_json = dir_json + json_name
        path_txt = json_name.replace('.json', '.txt')
        json2txt(path_json, path_txt)
