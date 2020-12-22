from django import forms


class AvaliacaoForm(forms.Form):
    planilha_de_acao = forms.FileField()
    doc_rel_acoes = forms.CharField(max_length=100)
    ano = forms.CharField(max_length=4)
    orgao = forms.CharField(max_length=100)
    avaliador1 = forms.CharField(max_length=100, required=False)
    orgao_avaliador1 = forms.CharField(max_length=100, required=False)
    avaliador2 = forms.CharField(max_length=100, required=False)
    orgao_avaliador2 = forms.CharField(max_length=100, required=False)
    avaliador3 = forms.CharField(max_length=100, required=False)
    orgao_avaliador3 = forms.CharField(max_length=100, required=False)
    representante_sgi = forms.CharField(max_length=100, required=False)
    representante_prodeb = forms.CharField(max_length=100, required=False)
    consideracoes_avaliador = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}), required=False)


class PrintAvaliacaoForm(forms.Form):
    options = (('Não','Não'), ('Sim','Sim'))
    indicacao = forms.ChoiceField(choices=options)