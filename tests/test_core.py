import unittest


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm

        self.assertIsNone(lgtm())
