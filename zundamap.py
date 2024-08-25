import os
import requests
import xml.etree.ElementTree as ET
import sys

JPMAPFILE = "jpmap.svg"

def get_svgmap():

    if os.path.exists(JPMAPFILE):
        return
    #url = "https://raw.githubusercontent.com/geolonia/japanese-prefectures/master/map-full.svg"
    url = "https://upload.wikimedia.org/wikipedia/commons/6/69/Blank_map_of_Japan_new.svg"
    response = requests.get(url)

    if response.status_code == 200:
        with open(JPMAPFILE, "wb") as file:
            file.write(response.content)
        print("ファイルのダウンロードが完了しました。")
    else:
        print("ファイルのダウンロードに失敗しました。ステータスコード:", response.status_code)


def extract_paths(input_file):
    # SVGファイルを解析
    tree = ET.parse(input_file)
    root = tree.getroot()

    # 名前空間を取得
    namespace = root.tag.split('}')[0] + '}'

    names = []
    for g in root.findall(f'.//{namespace}g'):
        name = g.get('name')
        if name in prefecture_dict.keys():
            print(name)
            for path in g.findall(f'.//{namespace}path'):
                print(path)
                new_root = ET.Element('svg')
                new_root.set('xmlns', 'http://www.w3.org/2000/svg')
                new_root.append(path)
                new_tree = ET.ElementTree(new_root)
                new_tree.write(name+".svg", encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    get_svgmap()
    extract_paths(JPMAPFILE)
    