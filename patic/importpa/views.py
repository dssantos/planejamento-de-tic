from django.shortcuts import render

from patic.importpa.forms import ImportForm

def importpa(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            context = {
                'ano': form.cleaned_data['ano'], 
                'orgao': form.cleaned_data['orgao'],
                'planilha_de_acao': form.cleaned_data['planilha_de_acao'],
                }
            return render(request, 'importsuccess.html', context)
        else:
            return render(request, 'importerror.html')
    form = ImportForm()
    return render(request, 'importpa.html', {'form': form})
