from unittest import TestCase

from patic.reports.models import dadospa


class CheckDataframe(TestCase):
    def test_dataframe_isnot_empty(self):
        return self.assertIsNotNone(dadospa())
