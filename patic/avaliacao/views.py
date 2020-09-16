from django.shortcuts import render

def avaliacao(request):
    return render(request, 'avaliacao/ficha_avaliacao.html')
