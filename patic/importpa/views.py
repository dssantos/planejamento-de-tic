import sys

from django.shortcuts import render
from xlrd import XLRDError
import pandas as pd

from patic.importpa.forms import ImportForm
from patic.importpa.models import convert_binary_xls_acoes_to_dataframe, check_actions_sheet_errors
from patic.core.models import moeda


def importpa(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        try:
            errors = check_actions_sheet_errors(request.FILES['planilha_de_acao'])
            config_errors = check_actions_sheet_errors(request.FILES['planilha_de_acao'])
            actions_dataframe = convert_binary_xls_acoes_to_dataframe(request.FILES['planilha_de_acao'])
            actions_html_table = actions_dataframe.to_html(index=False)
            qt_actions = len(actions_dataframe)
            vl_actions = actions_dataframe['valor'].sum()
        except XLRDError as err:
            errors = pd.DataFrame({'Erro':['A Planilha não possui a aba "Planejamento".'], 'Detalhes':[err]})
        except ValueError as err:
            errors = pd.DataFrame({'Erro':['A estrutura da Planilha está diferente do modelo padrão.'], 'Detalhes':[err]})
        except:
            errors = pd.DataFrame({'Erro':['Ocorreu um erro inesperado.'], 'Detalhes':[sys.exc_info()[:]]})

        if (form.is_valid()) and errors.empty:
            context = {
                'ano': form.cleaned_data['ano'], 
                'orgao': form.cleaned_data['orgao'],
                'planilha_de_acao': form.cleaned_data['planilha_de_acao'],
                'tabela_acoes': actions_html_table,
                'qt_actions':qt_actions,
                'vl_actions':moeda(vl_actions),
                }
            return render(request, 'importsuccess.html', context)
        else:
            context = {
                'errors': errors.to_html(index=False), 
                'planilha_de_acao': form.cleaned_data['planilha_de_acao']
                }
            return render(request, 'importerror.html', context)
    form = ImportForm()
    return render(request, 'importpa.html', {'form': form})
