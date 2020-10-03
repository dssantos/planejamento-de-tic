from django import forms


class AvaliacaoForm(forms.Form):
    planilha_de_acao = forms.FileField()


class PrintAvaliacaoForm(forms.Form):
    options = (('Não','Não'), ('Sim','Sim'))
    indicacao = forms.ChoiceField(choices=options)