from django import forms


class Reports2Form(forms.Form):
    planilha_de_execucao = forms.FileField()
