import os
import requests
import xml.etree.ElementTree as ET
import sys

prefecture_dict = {
    'hokkaido': '北海道',
    'aomori': '青森県',
    'iwate': '岩手県',
    'miyagi': '宮城県',
    'akita': '秋田県',
    'yamagata': '山形県',
    'fukushima': '福島県',
    'ibaraki': '茨城県',
    'tochigi': '栃木県',
    'gunma': '群馬県',
    'saitama': '埼玉県',
    'chiba': '千葉県',
    'tokyo': '東京都',
    'kanagawa': '神奈川県',
    'neigata': '新潟県',  # 注: 正しいスペルは 'niigata' です
    'toyama': '富山県',
    'ishikawa': '石川県',
    'fukui': '福井県',
    'yamanasi': '山梨県',  # 注: 正しいスペルは 'yamanashi' です
    'nagano': '長野県',
    'gifu': '岐阜県',
    'shizuoka': '静岡県',
    'aichi': '愛知県',
    'mie': '三重県',
    'shiga': '滋賀県',
    'kyoto': '京都府',
    'osaka': '大阪府',
    'hyogo': '兵庫県',
    'nara': '奈良県',
    'wakayama': '和歌山県',
    'tottori': '鳥取県',
    'shimane': '島根県',
    'okayama': '岡山県',
    'hiroshima': '広島県',
    'yamaguchi': '山口県',
    'tokushima': '徳島県',
    'kagawa': '香川県',
    'ehime': '愛媛県',
    'kochi': '高知県',
    'fukuoka': '福岡県',
    'saga': '佐賀県',
    'nagasaki': '長崎県',
    'kumamoto': '熊本県',
    'oita': '大分県',
    'miyazaki': '宮崎県',
    'kagoshima': '鹿児島県',
    'okinawa': '沖縄県'
}

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
    