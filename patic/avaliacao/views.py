from django.shortcuts import render
from patic.avaliacao.forms import AvaliacaoForm
from patic.avaliacao.models import ficha_avaliacao_context


def avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            context = ficha_avaliacao_context(request.FILES['planilha_de_acao'])
            return render(request, 'avaliacao/ficha_avaliacao.html', context=context)
    else:
        form = AvaliacaoForm()
        return render(request, 'avaliacao/form_avaliacao.html', {'form': form})
