from django import forms


class ImportForm(forms.Form):
    planilha_de_acao = forms.FileField()
    ano = forms.CharField(max_length=4)
    orgao = forms.CharField(max_length=100)