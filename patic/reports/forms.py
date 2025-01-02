from django import forms


class ReportsForm(forms.Form):
    planilha_de_acao = forms.FileField()
