from unittest import TestCase

from patic.core.models import moeda, filepath


class ConvertMoeda(TestCase):

    def test_moeda_1000(self):
        return self.assertIn(moeda(1000), ['1.000,00', '1,000.00'])

    def test_moeda_1(self):
        return self.assertIn(moeda(1), ['1,00', '1.00'])

    def test_moeda_05(self):
        return self.assertIn(moeda(0.5), ['0,50', '0.50'])

    def test_moeda_1_str(self):
        return self.assertIn(moeda('1'), ['1,00', '1.00'])

    def test_moeda_1_espaco_str(self):
        return self.assertIn(moeda('\xa0R$ 1'), ['1,00', '1.00'])


class FilePathAcao(TestCase):
    def test_path_contain_xlsx(self):
        return self.assertIn('.xlsx', filepath('Ação'))


class FilePathExecucao(TestCase):
    def test_path_contain_xlsx(self):
        return self.assertIn('.xlsx', filepath('Execução'))

