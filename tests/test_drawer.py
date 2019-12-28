import os
import unittest
from pathlib import Path

from lgtm.drawer import OUTPUT_NAME


class SaveWithMessageTest(unittest.TestCase):
    def setUP(self):
        output_path = Path(OUTPUT_NAME)
        if output_path.exists():
            output_path.unlink()

    def tearDown(self):
        output_path = Path(OUTPUT_NAME)
        output_path.unlink()

    def test_save_with_message(self):
        from lgtm.drawer import save_with_message

        path = os.path.dirname(__file__) + "/data/test_image.jpg"
        with open(path, "rb") as f:
            save_with_message(f, "DOG")

        output_path = Path(OUTPUT_NAME)
        self.assertTrue(output_path.exists())
