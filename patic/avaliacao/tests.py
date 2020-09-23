from django.test import TestCase
from patic.avaliacao.forms import AvaliacaoForm

class AvaliacaoTest(TestCase):
    '''Cenário:
Dado q temos um visitante no site
Quando clica em 'avaliacao'
Então ele vê a página de Ficha de Avaliação
e a página possui um formulário
e o formulario possui 1 campo
e o campo é upload de Planilha de Ações
e o formulário possui um botão para gerar ficha de avaliação
e a página exibe a Ficha e Avaliação preenchida com os dados da Planilha de Ações
e a página exibe um botão para imprimir a Ficha de Avaliação'''

    def setUp(self):
        self.resp = self.client.get('/avaliacao/')

    def test_get(self):
        """Get /avaliacao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use avaliacao/form_avaliacao.html"""
        self.assertTemplateUsed(self.resp, 'avaliacao/form_avaliacao.html')

    def test_html(self):
        """Html must contain some tags"""
        self.assertContains(self.resp, '<title>Ficha de Avaliação')
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, AvaliacaoForm)

    def test_form_has_fields(self):
        """Form must have 1 field"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['planilha_de_acao'], list(form.fields))
