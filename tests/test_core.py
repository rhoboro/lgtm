import os
import unittest
from pathlib import Path

from lgtm.drawer import OUTPUT_NAME


class LgtmTest(unittest.TestCase):
    def setUP(self):
        output_path = Path(OUTPUT_NAME)
        if output_path.exists():
            output_path.unlink()

    def tearDown(self):
        output_path = Path(OUTPUT_NAME)
        output_path.unlink()

    def test_lgtm(self):
        from lgtm.core import lgtm

        path = os.path.dirname(__file__) + "/data/test_image.jpg"
        lgtm(path, "dog")

        output_path = Path(OUTPUT_NAME)
        self.assertTrue(output_path.exists())
