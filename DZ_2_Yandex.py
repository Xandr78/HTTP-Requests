from pprint import pprint
import requests
TOKEN = ""

class YaUploader:
    def __init__(self, token):
        self.token = token
        self.yandex_url = "https://cloud-api.yandex.net/"
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
#Загрузка файла на Яндекс Диск
    def get_upload_link(self, disk_file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href")
        files = {"file": open(filename, 'rb')}
        response = requests.put(href, files=files)
        if response.ok:
            print("OK!")
if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    filename = input("Введите название файла: ")
    ya.get_upload_link(f"Загрузки/{filename}", f'{filename}')
