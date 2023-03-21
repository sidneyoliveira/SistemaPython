import docx

doc = docx.Document()
tabela = doc.add_table(rows=2, cols=2)
celula = tabela.cell(0, 0)
p = celula.paragraphs[0]
p.add_run("Texto em vermelho").font.color.rgb = docx.shared.RGBColor(255, 0, 0)
doc.save("documento.docx")
