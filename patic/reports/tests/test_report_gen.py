from unittest import TestCase

from patic.reports.models import moeda, filelist, filepath, dadospa


class ConvertMoeda(TestCase):

    def test_moeda_1000(self):
        return self.assertIn(moeda(1000), ['1.000,00', '1,000.00'])

    def test_moeda_1(self):
        return self.assertIn(moeda(1), ['1,00', '1.00'])

    def test_moeda_05(self):
        return self.assertIn(moeda(0.5), ['0,50', '0.50'])


class FileList(TestCase):
    def test_list_not_blank(self):
        return self.assertIsNot(filelist(), [])

    def test_list_len_1(self):
        return self.assertEqual(len(filelist()), 1)


class FilePath(TestCase):
    def test_path_contain_xlsx(self):
        return self.assertIn('.xlsx', filepath())


class CheckDataframe(TestCase):
    def test_dataframe_isnot_empty(self):
        return self.assertIsNotNone(dadospa())
