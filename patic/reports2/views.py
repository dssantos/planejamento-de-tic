import io

from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Image

from patic.reports2.models import dadospa, filepath, moeda


def report2(request):
    buffer = io.BytesIO()
    buffer.name = 'report2'
    styles = getSampleStyleSheet()
    style = styles["BodyText"]

    canv = Canvas(buffer, pagesize=landscape(letter))

    filename = filepath().split("/")[-1].split("\\")[-1].split(".")[0]
    orgao = filename.replace('  ', ' ').replace('Execução PA ', '').replace('Execucao PA ', '').replace(' 2019 (ultimo)', '').replace(' 2019', '')
    df = dadospa()

    for index, row in df.iterrows():

        contratada = row[8] == "Contratada/Adquirida"
        cancelada = (row[8] == "Cancelada") or (row[8] == "Suspensa")
        nomerelatorio = Paragraph("<bold><font size=20 color='white'>Relatório de Execução</font></bold>", style)
        nomeorgao = Paragraph("<bold><font size=25 color='white'>{}</font></bold>".format(orgao), style)
        ano = Paragraph("<bold><font size=25 color='white'>2019</font></bold>", style)

        acao = Paragraph('<font size=12><b>Ação:</b><br /><br />{}</font>'.format(row[0]), style)
        contrato = Paragraph('<font size=12><b>{}</b></font>'.format(row[5]), style)
        quantidade = Paragraph('<font size=12><b>Quantidade Planejada:</b> {}</font>'.format(row[6]), style)
        quantidade_exec = Paragraph('<font size=12><b>Quantidade Executada:</b> {}</font>'.format(row[9]), style) if contratada else ""
        execucao_fisica = Paragraph('<font size=12><b>Execução Física:</b> {} %</font>'.format(round(row[9]/row[6]*100,0)), style) if contratada else ""
        valor = Paragraph('<font size=12><b>Valor Planejado:</b> R$ {}</font>'.format(moeda(row[7])), style)
        valor_exec = Paragraph('<font size=12><b>Valor Executado:</b> R$ {}</font>'.format(moeda(row[10])), style) if contratada else ""
        execucao_financeira = Paragraph('<font size=12><b>Execução Financeira:</b> {} %</font>'.format(round(row[10]/row[7]*100,0)), style) if contratada else ""
        status = Paragraph('<font size=12><b>Status da Ação:</b> {}</font>'.format(row[8]), styles['Normal'])
        motivo = Paragraph('<font size=12><b>Motivo:</b> {}</font>'.format(row[11]), styles['Normal']) if cancelada else ""

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
    return FileResponse(buffer, as_attachment=True, filename='Relatório de Execução {} 2019.pdf'.format(orgao))
