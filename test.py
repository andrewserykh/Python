from docx import Document

document = Document('/Users/andrew.serykh/Python/v1.docx')

sections = document.sections
for section in sections:
    print(section.start_type)