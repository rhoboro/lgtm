import os
import unittest
from unittest.mock import patch, Mock


class LocalImageTest(unittest.TestCase):
    def test_get_image(self):
        from lgtm.image_source import LocalImage

        path = os.path.dirname(__file__) + "/data/test_image.jpg"
        with LocalImage(path).get_image() as f:
            actual = f.read()
        with open(path, "rb") as f:
            expected = f.read()
        self.assertEqual(expected, actual)


class RemoteImageTest(unittest.TestCase):
    def test_get_image(self):
        from lgtm.image_source import RemoteImage

        url = "https://raw.githubusercontent.com/rhoboro/lgtm/master/tests/data/test_image.jpg"
        with RemoteImage(url).get_image() as f:
            actual = f.read()

        path = os.path.dirname(__file__) + "/data/test_image.jpg"
        with open(path, "rb") as f:
            expected = f.read()
        self.assertEqual(expected, actual)


class KeywordImageTest(unittest.TestCase):
    def test_get_image(self):
        from lgtm.image_source import KeywordImage

        with patch("lgtm.image_source.requests.get") as mock:
            path = os.path.dirname(__file__) + "/data/test_image.jpg"
            with open(path, "rb") as f:
                expected = f.read()
            response = Mock()
            response.content = expected
            mock.return_value = response

            with KeywordImage("dog").get_image() as f:
                actual = f.read()

            # 結果の確認
            self.assertEqual(expected, actual)
            # 取得時のURLの確認
            mock.assert_called_once_with("https://loremflickr.com/800/600/dog")


class ImageSourceTest(unittest.TestCase):
    def test_http(self):
        from lgtm.image_source import ImageSource, RemoteImage

        actual = ImageSource("http://www.example.com")
        self.assertEqual(RemoteImage, type(actual))

    def test_https(self):
        from lgtm.image_source import ImageSource, RemoteImage

        actual = ImageSource("https://www.example.com")
        self.assertEqual(RemoteImage, type(actual))

    def test_localpath(self):
        from lgtm.image_source import ImageSource, LocalImage

        path = os.path.dirname(__file__) + "/data/test_image.jpg"
        actual = ImageSource(path)
        self.assertEqual(LocalImage, type(actual))

    def test_keyword(self):
        from lgtm.image_source import ImageSource, KeywordImage

        actual = ImageSource("dog")
        self.assertEqual(KeywordImage, type(actual))


class GetImageTest(unittest.TestCase):
    def test_get_image(self):
        from lgtm.image_source import get_image

        with patch("lgtm.image_source.ImageSource") as mock:
            get_image("dog")
            mock.assert_called_once_with("dog")
