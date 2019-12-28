import os
import unittest


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
