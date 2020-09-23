from django import forms
class AvaliacaoForm(forms.Form):
    planilha_de_acao = forms.FileField()