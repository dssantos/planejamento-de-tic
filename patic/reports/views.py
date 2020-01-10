import io

from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Image

from patic.reports.models import dadospa, filepath, moeda


def report(request):
    buffer = io.BytesIO()
    buffer.name = 'report'
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas(buffer, pagesize=landscape(letter))

    filename = filepath().split("/")[-1].split("\\")[-1].split(".")[0]
    orgao = filename.replace('PA ', '').replace('  ', ' ').replace(' 2020 (ultimo)', '').replace(' 2020', '')
    df = dadospa()

    for index, row in df.iterrows():

        nomerelatorio = Paragraph("<bold><font size=20 color='white'>Relatório de Ações</font></bold>", style)
        nomeorgao = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(orgao), style)
        ano = Paragraph("<bold><font size=25 color='white'>2020</font></bold>", style)

        acao = Paragraph('<font size=12><b>Ação:</b><br /><br />{}</font>'.format(row[0]), style)
        justificativa = Paragraph('<font size=12><b>Justificativa:</b><br /><br />{}</font>'.format(row[1]), styles['Normal'])
        especificacao = Paragraph('<font size=12><b>Especificação do item:</b><br /><br />{}</font>'.format(row[2]), styles['Normal'])
        objeto = Paragraph('<font size=12><b>Objeto de aquisição:</b><br /><br />{}</font>'.format(row[3]), styles['Normal'])
        contrato = Paragraph('<font size=12><b>{}</b></font>'.format(row[5]), style)
        duracao = Paragraph('<font size=12><b>Duração do contrato:</b> {} meses</font>'.format(row[4]), style)
        quantidade = Paragraph('<font size=12><b>Quantidade:</b> {}</font>'.format(row[6]), style)
        valor = Paragraph('<font size=12><b>Valor:</b> R$ {}</font>'.format(moeda(row[7])), style)

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
    return FileResponse(buffer, as_attachment=True, filename='Relatório de Ações {} 2020.pdf'.format(orgao))
