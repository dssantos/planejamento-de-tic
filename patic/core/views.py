import io

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Image

from patic.core.models import dadospa, filepath, moeda


def home(request):
    return render(request, 'index.html')


def report(request):
    buffer = io.BytesIO()
    buffer.name = 'report'
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas(buffer, pagesize=landscape(letter))

    filename = filepath().split("/")[-1].split("\\")[-1].split(".")[0]
    orgao = filename.replace('PA ', '').replace(' 2020 (ultimo)', '').replace(' 2020', '')
    df = dadospa()

    for index, row in df.iterrows():

        nomerelatorio = Paragraph("<bold><font size=20 color='white'>Relatório de Ações</font></bold>", style)
        nomeorgao = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(orgao), style)
        ano = Paragraph("<bold><font size=25 color='white'>2020</font></bold>", style)

        data = [[Paragraph('Ação:<br /><br />{}'.format(row[0]), style), ''],
                [Paragraph('Justificativa:<br /><br />{}'.format(row[1]), styles['Normal']), ''],
                [Paragraph('Especificação do item:<br /><br />{}'.format(row[2]), styles['Normal']),
                 Paragraph('Objeto de aquisição:<br /><br />{}'.format(row[3]), styles['Normal'])],
                ['{}'.format(row[5]), 'Duração do contrato: {} meses'.format(row[4])],
                ['Quantidade: {}'.format(row[6]), 'Valor: R$ {}'.format(moeda(row[7]))]
                ]

        t = Table(data, colWidths=[420, 250], rowHeights=[60, 120, 60, 60, 60])
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
                bg_color = colors.Color(red=(153.0 / 255), green=(204.0 / 255), blue=(255.0 / 255))

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
        nomeorgao.drawOn(canv, 510, 540)
        ano.drawOn(canv, 660, 540)
        t.drawOn(canv, 72, 100)
        canv.drawString(400, 40, "Ação {}".format(index + 1))
        canv.showPage()

    canv.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='{}.pdf'.format(filename))
