from docx import Document
from docx.shared import RGBColor, Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_table_border(table, border_style="dashDot", border_width=6, border_color=(255, 0, 0)):
    """
    Define o estilo, a largura e a cor das bordas da tabela.
    """
    table.style = 'Table Grid'
    tblPr = table._element.xpath('.//w:tblPr')[0]
    tblBorders = OxmlElement('w:tblBorders')
    for edge in ('w:top', 'w:left', 'w:bottom', 'w:right', 'w:insideH', 'w:insideV'):
        element = OxmlElement(edge)
        element.set(qn('w:val'), border_style)
        element.set(qn('w:sz'), str(border_width))
        element.set(qn('w:color'), '#{:02X}{:02X}{:02X}'.format(*border_color))
        tblBorders.append(element)
    tblPr.append(tblBorders)

# cria o documento
document = Document()

# cria a tabela
table = document.add_table(rows=3, cols=3, style='Table Grid')

# define o estilo da tabela
set_table_border(table, border_style='dashDot', border_width=6, border_color=(255, 0, 0))

# preenche a tabela com conteúdo
for i in range(3):
    row = table.rows[i]
    row.cells[0].text = 'Texto {}'.format(i + 1)
    row.cells[1].text = 'Texto {}'.format(i + 4)
    row.cells[2].text = 'Texto {}'.format(i + 7)

# define o estilo do conteúdo da tabela
for row in table.rows:
    for cell in row.cells:
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 0, 0)
        cell.paragraphs[0].runs[0].font.size = Pt(12)

# salva o documento
document.save('tabela.docx')