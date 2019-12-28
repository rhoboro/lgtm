from io import BytesIO

import requests


class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, "rb")


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        # バイトデータをファイルオブジェクトに変換
        return BytesIO(data.content)
