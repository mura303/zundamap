import os
import requests
from bs4 import BeautifulSoup

def download_images_from_irasutoya(url, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')

    for img in images:
        img_url = img.get('src')
        if img_url.endswith('.png'):
            img_name = os.path.basename(img_url)
            img_path = os.path.join(save_dir, img_name)
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Downloaded {img_name}")

if __name__ == "__main__":

    urls = """
    https://www.irasutoya.com/2015/05/blog-post_126.html
    https://www.irasutoya.com/2015/05/6.html
    https://www.irasutoya.com/2015/05/16.html
    https://www.irasutoya.com/2015/05/9.html
    https://www.irasutoya.com/2015/05/25.html
    https://www.irasutoya.com/2015/05/5.html
    https://www.irasutoya.com/2015/05/4.html
    https://www.irasutoya.com/2015/05/8.html
    """

    save_directory = "irasutoya_images"

    for u in urls.split():
        download_images_from_irasutoya(u, save_directory)
