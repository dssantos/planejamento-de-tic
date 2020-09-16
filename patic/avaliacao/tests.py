from django.test import TestCase

class AvaliacaoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/avaliacao/')

    def test_get(self):
        """Get /avaliacao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use avaliacao/ficha_avaliacao.html"""
        self.assertTemplateUsed(self.resp, 'avaliacao/ficha_avaliacao.html')

    def test_html(self):
        """Html must contain some tags"""
        self.assertContains(self.resp, '<title>Ficha de Avaliação')