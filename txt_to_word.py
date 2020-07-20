import docx
from docx import Document
from docx.shared import Pt
from docx2pdf import convert
import os
from docx.shared import Inches
from docx.oxml.ns import qn, nsdecls
from docx.enum.section import WD_ORIENTATION
from docx.enum.section import WD_SECTION_START
from docx.enum.section import WD_HEADER_FOOTER_INDEX



WNS_COLS_NUM = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}num"




def set_number_of_columns(section, cols):
    # column 설정해주는 함수
    section._sectPr.xpath("./w:cols")[0].set(WNS_COLS_NUM, str(cols))


def trans():
    print("Enter the txt file name")
    txt_name = input()

    try:
        f = open(txt_name, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print("Cannot find the file")
        return

    test = f.read()
    f.close()
    # 텍스트파일에 있는 내용을 받아옴

    document = Document()
    list = test.split('\n')
    for i in list:
        if (i[0] == '○'):
            para = document.add_paragraph()
            run = para.add_run(i)
            run.bold = True

        else:
            document.add_paragraph(i)
    # "○김성원 위원"같은 태그가 붙을시 글씨체 bold 로 바꿔주고 붙혀넣어줌


    style = document.styles['Normal']
    font = style.font
    font.name = '함초롱바탕'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '함초롱바탕')
    font.size = Pt(10)
    # 글씨크기 변경 및 폰트 변경


    document.add_page_break()
    section = document.sections[0]
    set_number_of_columns(section, 2)
    # 다단 설정(layout 설정)

    filename = os.path.splitext(txt_name)[0]
    docxfilename = filename + ".docx"
    document.save(docxfilename)
    # 저장,원래 파일이름 그대로로 확장자만 바꿔서 저장

    convert(docxfilename)
    #pdf로 변환



trans()



