from django.shortcuts import render
from django.forms import formset_factory

from patic.avaliacao.forms import AvaliacaoForm, PrintAvaliacaoForm
from patic.avaliacao.models import ficha_avaliacao_context


def avaliacao(request):
    if request.method == 'POST' and 'btn_upload' in request.POST:
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            context = ficha_avaliacao_context(request.FILES['planilha_de_acao'])
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
