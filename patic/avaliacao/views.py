from django.shortcuts import render
from django.forms import formset_factory

from patic.avaliacao.forms import AvaliacaoForm, PrintAvaliacaoForm
from patic.avaliacao.models import ficha_avaliacao_context


def avaliacao(request):
    if request.method == 'POST' and 'btn_upload' in request.POST:
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            context = ficha_avaliacao_context(request.FILES['planilha_de_acao'])
            context['orgao'] = form.cleaned_data['orgao']
            context['doc_rel_acoes'] = form.cleaned_data['doc_rel_acoes']
            context['avaliador1'] = form.cleaned_data['avaliador1']
            context['orgao_avaliador1'] = form.cleaned_data['orgao_avaliador1']
            context['avaliador2'] = form.cleaned_data['avaliador2']
            context['orgao_avaliador2'] = form.cleaned_data['orgao_avaliador2']
            context['representante_sgi'] = form.cleaned_data['representante_sgi']
            context['representante_prodeb'] = form.cleaned_data['representante_prodeb']
            context['consideracoes_avaliador'] = form.cleaned_data['consideracoes_avaliador']
            PrintAvaliacaoFormSet = formset_factory(PrintAvaliacaoForm, extra=len(context['acoes']))
            formset = PrintAvaliacaoFormSet()
            for form, acao in zip(formset, context['acoes']):
                acao['indicacao'] = form
            
            

            return render(request, 'avaliacao/ficha_avaliacao.html', context=context)

    if request.method == 'POST' and 'btn_print' in request.POST:
        return render(request, 'avaliacao/print_avaliacao.html')
        
    else:
        form = AvaliacaoForm()
        return render(request, 'avaliacao/form_avaliacao.html', {'form': form})
