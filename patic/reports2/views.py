import io
import pandas as pd

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Image

from patic.core.models import moeda, filepath
from patic.reports2.models import file_execucao_to_df
from patic.reports2.forms import Reports2Form


def report2(request):
    if request.method == 'POST':
        form = Reports2Form(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['planilha_de_execucao']
            buffer = io.BytesIO()
            buffer.name = 'report2'
            styles = getSampleStyleSheet()
            style = styles["BodyText"]

            canv = Canvas(buffer, pagesize=landscape(letter))

            filename = docfile.name[:-5]
            orgao = filename.replace('  ', ' ').replace('Execução PA ', '').replace('Execucao PA ', '').replace(' (ultimo)', '')[:-5]
            ano_value = filename.replace('  ', ' ').replace('Execução PA ', '').replace('Execucao PA ', '').replace(' (ultimo)', '')[-4:]
            df = file_execucao_to_df(docfile)
            invalido = '<font color = "red">VALOR INVÁLIDO</font>'
            for index, row in df.iterrows():

                contratada = row[9] == "Contratada/Adquirida"
                cancelada = (row[9] == "Cancelada") or (row[9] == "Suspensa")
                nomerelatorio = Paragraph("<bold><font size=20 color='white'>Relatório de Execução</font></bold>", style)
                nomeorgao = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(orgao), style)
                ano = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(ano_value), style)
                unidade = "{} - ".format(orgao) if pd.isna(row[0]) else "{} - ".format(row[0])

                acao = Paragraph('<font size=12><b>Ação:</b><br /><br />{}{}</font>'.format(unidade, row[1]), style)
                contrato = Paragraph('<font size=12><b>{}</b></font>'.format(row[6]), style)
                try:
                    quantidade = Paragraph('<font size=12><b>Quantidade Planejada:</b> {}</font>'.format(row[7]), style)
                except:
                    quantidade = Paragraph('<font size=12><b>Quantidade Planejada:</b> {}</font>'.format(invalido), style)
                try:
                    quantidade_exec = Paragraph('<font size=12><b>Quantidade Executada:</b> {}</font>'.format(row[10]), style) if contratada else ""
                except:
                    quantidade_exec = Paragraph('<font size=12><b>Quantidade Executada:</b> {}</font>'.format(invalido), style) if contratada else ""
                execucao_fisica = Paragraph('<font size=12><b>Execução Física:</b> {} %</font>'.format(round(row[10]/row[7]*100,0)), style) if contratada else ""
                try:
                    valor = Paragraph('<font size=12><b>Valor Planejado:</b> R$ {}</font>'.format(moeda(row[8])), style)
                except:
                    valor = Paragraph('<font size=12><b>Valor Planejado:</b> {}</font>'.format(invalido), style)
                try:
                    valor_exec = Paragraph('<font size=12><b>Valor Executado:</b> R$ {}</font>'.format(moeda(row[11])), style) if contratada else ""
                except:
                    valor_exec = Paragraph('<font size=12><b>Valor Executado:</b> R$ {}</font>'.format(invalido), style) if contratada else ""
                execucao_financeira = Paragraph('<font size=12><b>Execução Financeira:</b> {} %</font>'.format(round(row[11]/row[8]*100,0)), style) if contratada else ""
                status = Paragraph('<font size=12><b>Status da Ação:</b> {}</font>'.format(row[9]), styles['Normal'])
                motivo = Paragraph('<font size=12><b>Motivo:</b> {}</font>'.format(row[12]), styles['Normal']) if cancelada else ""

                data = [
                        [acao, ''],
                        [contrato, ''],
                        [quantidade, valor],
                        [quantidade_exec, valor_exec],
                        [execucao_fisica, execucao_financeira],
                        [status, motivo],
                    ]

                t = Table(data, colWidths=[335, 335], rowHeights=[70, 40, 40, 40, 40, 40])
                t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                    ('SPAN', (0, 0), (1, 0)),
                                    ('SPAN', (0, 1), (1, 1)),
                                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                    ]))
                data_len = len(data)

                for each in range(data_len):
                    if each % 2 == 0:
                        bg_color = colors.white
                    else:
                        bg_color = colors.Color(red=(204.0 / 255), green=(229.0 / 255), blue=(255.0 / 255))

                    t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

                aW = 440
                aH = 530

                w, h = nomerelatorio.wrap(aW, aH)
                w, h = nomeorgao.wrap(aW, aH)
                w, h = ano.wrap(aW, aH)
                w, h = t.wrap(aW, aH)
                aH = aH - h

                img = Image("patic/core/static/img/topo_report_acao.jpg", width=673, height=80)
                img.drawOn(canv, 72 - 2, 490)
                nomerelatorio.drawOn(canv, 72 + 26, 510)
                nomeorgao.drawOn(canv, 460, 540)
                ano.drawOn(canv, 660, 540)
                t.drawOn(canv, 72, 210)
                canv.drawString(400, 40, "Ação {}".format(index + 1))
                canv.showPage()

            canv.save()

            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='Relatório de Execução {} {}.pdf'.format(orgao, ano_value))

    else:
        form = Reports2Form()
        return render(request, 'report2/form_report2.html', {'form': form})
