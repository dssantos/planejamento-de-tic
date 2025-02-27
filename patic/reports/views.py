import io

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Image

from patic.core.models import moeda
from patic.reports.models import file_acoes_to_df
from patic.reports.forms import ReportsForm


def report(request):
    if request.method == 'POST':
        form = ReportsForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['planilha_de_acao']
            buffer = io.BytesIO()
            buffer.name = 'report'
            styles = getSampleStyleSheet()
            style = styles["BodyText"]

            canv = Canvas(buffer, pagesize=landscape(letter))

            filename = docfile.name[:-5]
            orgao = filename.replace('  ', ' ').replace('PA ', '').replace(' (ultimo)', '')[:-5]
            ano_value = filename.replace('  ', ' ').replace('PA ', '').replace(' (ultimo)', '')[-4:]
            df = file_acoes_to_df(docfile)

            for index, row in df.iterrows():

                nomerelatorio = Paragraph("<bold><font size=20 color='white'>Relatório de Ações</font></bold>", style)
                nomeorgao = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(orgao), style)
                ano = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(ano_value), style)

                unidade = '{} - '.format(row[1]) if str(row[1]) != 'nan' else ''
                acao = Paragraph('<font size=12><b>Ação:</b><br /><br />{}{}</font>'.format(unidade, row[2]), style)
                justificativa = Paragraph('<font size=12><b>Justificativa:</b><br /><br />{}</font>'.format(row[3]), styles['Normal'])
                especificacao = Paragraph('<font size=12><b>Especificação do item:</b><br /><br />{}</font>'.format(row[4]), styles['Normal'])
                objeto = Paragraph('<font size=12><b>Objeto de aquisição:</b><br /><br />{}</font>'.format(row[5]), styles['Normal'])
                contrato = Paragraph('<font size=12><b>{}</b></font>'.format(row[7]), style)
                duracao = Paragraph('<font size=12><b>Duração do contrato:</b> {} meses</font>'.format(row[6]), style)
                quantidade = Paragraph('<font size=12><b>Quantidade:</b> {}</font>'.format(row[8]), style)
                valor = Paragraph('<font size=12><b>Valor:</b> R$ {}</font>'.format(moeda(row[9])), style)

                data = [
                        [acao, ''],
                        [justificativa, ''],
                        [especificacao, objeto],
                        [contrato, duracao],
                        [quantidade, valor]
                    ]

                t = Table(data, colWidths=[420, 250], rowHeights=[70, 195, 80, 30, 30])
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
                t.drawOn(canv, 72, 70)
                canv.drawString(400, 40, "Ação {}".format(index + 1))
                canv.showPage()

            canv.save()

            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='Relatório de Ações {} {}.pdf'.format(orgao, ano_value))

    else:
        form = ReportsForm()
        return render(request, 'report/form_report.html', {'form': form})
        